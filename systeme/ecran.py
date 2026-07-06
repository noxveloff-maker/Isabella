import os
import platform
from datetime import datetime

class Ecran:
    """Captures d'ecran, vision du bureau, et informations visuelles."""

    def __init__(self):
        self.historique_captures = []
        self._detecter_systeme()

    def _detecter_systeme(self):
        self.systeme = platform.system().lower()
        self.dossier_captures = os.path.expanduser("~/captures_isabella")
        os.makedirs(self.dossier_captures, exist_ok=True)

    def capture(self, nom=None, region=None):
        """Capture l'ecran entier ou une region (x, y, largeur, hauteur)."""
        if nom is None:
            nom = f"capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        chemin = os.path.join(self.dossier_captures, f"{nom}.png")

        try:
            if self.systeme == "windows":
                # Windows — utilise Pillow si dispo, sinon mss
                self._capture_windows(chemin, region)
            elif self.systeme == "darwin":
                # macOS
                self._capture_macos(chemin, region)
            else:
                # Linux
                self._capture_linux(chemin, region)

            self.historique_captures.append({
                "nom": nom,
                "chemin": chemin,
                "date": datetime.now().strftime("%H:%M:%S")
            })

            return {
                "succes": True,
                "chemin": chemin,
                "nom": nom,
                "taille": os.path.getsize(chemin) if os.path.exists(chemin) else 0
            }
        except Exception as e:
            return {"erreur": f"Erreur capture : {e}", "systeme": self.systeme}

    def _capture_windows(self, chemin, region=None):
        try:
            import PIL.ImageGrab as ImageGrab
            if region:
                x, y, w, h = region
                img = ImageGrab.grab(bbox=(x, y, x+w, y+h))
            else:
                img = ImageGrab.grab()
            img.save(chemin)
        except ImportError:
            # Fallback avec mss
            import mss
            with mss.mss() as sct:
                if region:
                    x, y, w, h = region
                    monitor = {"left": x, "top": y, "width": w, "height": h}
                else:
                    monitor = sct.monitors[1]
                sct_img = sct.grab(monitor)
                import mss.tools
                mss.tools.to_png(sct_img.rgb, sct_img.size, output=chemin)

    def _capture_macos(self, chemin, region=None):
        if region:
            x, y, w, h = region
            cmd = f"screencapture -x -R{x},{y},{w},{h} '{chemin}'"
        else:
            cmd = f"screencapture -x '{chemin}'"
        os.system(cmd)

    def _capture_linux(self, chemin, region=None):
        # Tente gnome-screenshot ou import (ImageMagick)
        if region:
            x, y, w, h = region
            cmd = f"gnome-screenshot -f '{chemin}' -a -x || import -window root -crop {w}x{h}+{x}+{y} '{chemin}'"
        else:
            cmd = f"gnome-screenshot -f '{chemin}' || import -window root '{chemin}'"
        os.system(cmd)

    def infos_ecran(self):
        """Retourne les infos sur les ecrans disponibles."""
        try:
            import tkinter as tk
            root = tk.Tk()
            root.withdraw()
            largeur = root.winfo_screenwidth()
            hauteur = root.winfo_screenheight()
            root.destroy()
            return {
                "largeur": largeur,
                "hauteur": hauteur,
                "systeme": self.systeme,
                "dossier_captures": self.dossier_captures
            }
        except:
            return {"erreur": "Impossible de detecter la taille ecran", "systeme": self.systeme}

    def liste_captures(self):
        """Liste les captures precedentes."""
        return self.historique_captures[-10:]

if __name__ == "__main__":
    e = Ecran()
    print("=== Infos ecran ===")
    print(e.infos_ecran())
    print("\n=== Test capture ===")
    print(e.capture("test"))
    print("\n=== Historique ===")
    print(e.liste_captures())
