import os
import platform
import subprocess
from datetime import datetime

class VisionEcran:
    """
    Capture et analyse l'ecran pour trouver du texte, des boutons, des elements.
    Utilise l'OCR (Tesseract) si disponible, sinon fait de la reconnaissance basique.
    """

    def __init__(self, ecran=None):
        self.systeme = platform.system().lower()
        self.dossier_captures = os.path.expanduser("~/captures_isabella")
        os.makedirs(self.dossier_captures, exist_ok=True)
        self.ecran = ecran  # Instance de systeme.ecran.Ecran
        self.cache_elements = {}  # texte -> {x, y, largeur, hauteur, date}
        self._detecter_tesseract()

    def _detecter_tesseract(self):
        """Verifie si Tesseract OCR est installe."""
        try:
            result = subprocess.run(["tesseract", "--version"], capture_output=True, text=True, timeout=3)
            self.tesseract_dispo = result.returncode == 0
        except:
            self.tesseract_dispo = False

    def capture_et_analyser(self, nom=None):
        """
        Capture l'ecran et analyse son contenu.
        Retourne les elements trouves (texte, positions).
        """
        if self.ecran:
            resultat_capture = self.ecran.capture(nom)
            chemin = resultat_capture.get("chemin")
        else:
            chemin = self._capture_simple(nom)

        if not chemin or not os.path.exists(chemin):
            return {"erreur": "Impossible de capturer l'ecran"}

        elements = self._analyser_image(chemin)
        self.cache_elements = {e["texte"]: e for e in elements}

        return {
            "succes": True,
            "chemin": chemin,
            "elements_trouves": len(elements),
            "elements": elements
        }

    def _capture_simple(self, nom=None):
        """Capture simple sans dependance externe."""
        if not nom:
            nom = f"vision_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        chemin = os.path.join(self.dossier_captures, f"{nom}.png")

        if self.systeme == "windows":
            try:
                import PIL.ImageGrab as ImageGrab
                img = ImageGrab.grab()
                img.save(chemin)
            except:
                return None
        elif self.systeme == "darwin":
            subprocess.run(["screencapture", "-x", chemin], check=True)
        else:
            subprocess.run(f"gnome-screenshot -f '{chemin}' 2>/dev/null || import -window root '{chemin}' 2>/dev/null", shell=True)
        return chemin

    def _analyser_image(self, chemin_image):
        """
        Analyse une image pour trouver du texte.
        Utilise Tesseract si disponible, sinon retourne des infos basiques.
        """
        elements = []

        if self.tesseract_dispo:
            try:
                # Tesseract avec sortie TSV (position + texte)
                result = subprocess.run(
                    ["tesseract", chemin_image, "stdout", "--psm", "6", "-c", "tessedit_create_tsv=1"],
                    capture_output=True, text=True, timeout=30
                )
                elements = self._parser_tsv_tesseract(result.stdout)
            except Exception as e:
                elements = [{"texte": f"OCR erreur: {e}", "x": 0, "y": 0, "largeur": 0, "hauteur": 0}]
        else:
            # Sans Tesseract, on retourne un element avec les dimensions de l'ecran
            elements = [{
                "texte": "(Tesseract non installe - OCR indisponible)",
                "x": 0, "y": 0, "largeur": 1920, "hauteur": 1080,
                "info": "Installe Tesseract: sudo apt install tesseract-ocr (Linux) ou brew install tesseract (macOS)"
            }]

        return elements

    def _parser_tsv_tesseract(self, tsv_output):
        """Parse la sortie TSV de Tesseract pour extraire texte et positions."""
        elements = []
        lignes = tsv_output.strip().split('\n')

        if len(lignes) <= 1:
            return elements

        # Premiere ligne = headers
        headers = lignes[0].split('\t')
        try:
            idx_text = headers.index('text')
            idx_left = headers.index('left')
            idx_top = headers.index('top')
            idx_width = headers.index('width')
            idx_height = headers.index('height')
            idx_conf = headers.index('conf')
        except ValueError:
            return elements

        for ligne in lignes[1:]:
            cols = ligne.split('\t')
            if len(cols) < len(headers):
                continue
            try:
                texte = cols[idx_text].strip()
                conf = int(cols[idx_conf]) if cols[idx_conf].isdigit() else 0
                if texte and conf > 30:  # Filtre le bruit
                    elements.append({
                        "texte": texte,
                        "x": int(cols[idx_left]),
                        "y": int(cols[idx_top]),
                        "largeur": int(cols[idx_width]),
                        "hauteur": int(cols[idx_height]),
                        "confiance": conf
                    })
            except (ValueError, IndexError):
                continue

        return elements

    def trouver_texte(self, texte_recherche, seuil_confiance=30):
        """
        Trouve un texte a l'ecran et retourne sa position.
        Capture d'abord l'ecran si le cache est vide.
        """
        # Si pas dans le cache, capture et analyse
        if not self.cache_elements or texte_recherche not in self.cache_elements:
            resultat = self.capture_et_analyser()
            if resultat.get("erreur"):
                return resultat

        # Cherche dans le cache (correspondance exacte ou partielle)
        for texte, element in self.cache_elements.items():
            if texte_recherche.lower() in texte.lower():
                return {
                    "succes": True,
                    "texte_trouve": texte,
                    "x": element["x"] + element["largeur"] // 2,  # Centre
                    "y": element["y"] + element["hauteur"] // 2,
                    "largeur": element["largeur"],
                    "hauteur": element["hauteur"],
                    "confiance": element.get("confiance", 0)
                }

        return {"erreur": f"Texte '{texte_recherche}' non trouve a l'ecran"}

    def trouver_plusieurs(self, texte_recherche):
        """Trouve toutes les occurrences d'un texte a l'ecran."""
        if not self.cache_elements:
            self.capture_et_analyser()

        trouves = []
        for texte, element in self.cache_elements.items():
            if texte_recherche.lower() in texte.lower():
                trouves.append({
                    "texte": texte,
                    "x": element["x"] + element["largeur"] // 2,
                    "y": element["y"] + element["hauteur"] // 2,
                    "largeur": element["largeur"],
                    "hauteur": element["hauteur"]
                })

        return trouves

    def lister_elements_visibles(self, n_max=20):
        """Liste les elements textuels visibles a l'ecran."""
        if not self.cache_elements:
            self.capture_et_analyser()
        return [
            {"texte": e["texte"], "x": e["x"], "y": e["y"]}
            for e in list(self.cache_elements.values())[:n_max]
        ]

if __name__ == "__main__":
    v = VisionEcran()
    print(f"Tesseract disponible: {v.tesseract_dispo}")
    print(f"Systeme: {v.systeme}")
    
    if v.tesseract_dispo:
        print("\n=== Test capture + analyse ===")
        resultat = v.capture_et_analyser("test_vision")
        print(f"Elements trouves: {resultat.get('elements_trouves', 0)}")
        for e in resultat.get('elements', [])[:5]:
            print(f"  '{e['texte']}' en ({e['x']},{e['y']}) [{e['largeur']}x{e['hauteur']}]")
    else:
        print("Installe Tesseract pour tester l'OCR:")
        print("  Linux: sudo apt install tesseract-ocr")
        print("  macOS: brew install tesseract")
        print("  Windows: https://github.com/UB-Mannheim/tesseract/wiki")
