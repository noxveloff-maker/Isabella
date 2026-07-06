import re
import os
from datetime import datetime

class Orchestrateur:
    """
    Traduit les intentions en actions systeme.
    C'est le cerveau qui decide quels outils utiliser.
    """

    def __init__(self, fichiers, terminal, ecran, controle, navigateur, vision_ecran=None, selection=None, apprentissage_visuel=None):
        self.fichiers = fichiers
        self.terminal = terminal
        self.ecran = ecran
        self.controle = controle
        self.navigateur = navigateur
        self.vision = vision_ecran
        self.selection = selection
        self.apprentissage_visuel = apprentissage_visuel
        self.historique = []

    def analyser_commande(self, texte):
        """
        Analyse le texte et determine quelle action systeme executer.
        Retourne un dictionnaire avec l'action et les parametres.
        """
        texte = texte.lower().strip()

        # --- Vision / Apprentissage visuel (avant les matches generaux) ---
        if any(m in texte for m in ["liste les elements", "que vois-tu", "decris l'ecran", "analyse l'ecran", "scanne l'ecran"]):
            return {"action": "lister_elements", "module": "vision", "parametres": {}}

        elif any(m in texte for m in ["liste les positions", "montre les positions apprises", "elements appris", "positions memorisees"]):
            return {"action": "lister_positions", "module": "apprentissage_visuel", "parametres": {}}

        # --- Fichiers ---
        elif any(m in texte for m in ["liste", "contenu", "dossier", "repertoire", "fichier dans"]):
            chemin = self._extraire_chemin(texte) or "."
            return {"action": "lister", "module": "fichiers", "parametres": {"chemin": chemin}}

        elif any(m in texte for m in ["lis", "ouvre le fichier", "affiche le contenu", "regarde dans"]):
            chemin = self._extraire_chemin(texte)
            if chemin:
                return {"action": "lire_fichier", "module": "fichiers", "parametres": {"chemin": chemin}}
            return {"action": "info", "message": "Precise le chemin du fichier a lire."}

        elif any(m in texte for m in ["cherche un fichier", "trouve le fichier", "fichier nomme"]):
            dossier = self._extraire_chemin(texte) or "."
            mots = texte.split()
            # Cherche un pattern apres "fichier" ou "nomme"
            pattern = "*"
            for i, m in enumerate(mots):
                if m in ["fichier", "nomme", "appelle"] and i+1 < len(mots):
                    pattern = mots[i+1]
                    break
            return {"action": "chercher_fichier", "module": "fichiers", "parametres": {"dossier": dossier, "pattern": pattern}}

        elif any(m in texte for m in ["ecris", "crée un fichier", "sauvegarde dans", "note dans"]):
            chemin = self._extraire_chemin(texte)
            contenu = self._extraire_contenu(texte)
            if chemin:
                return {"action": "ecrire_fichier", "module": "fichiers", "parametres": {"chemin": chemin, "contenu": contenu}}
            return {"action": "info", "message": "Precise le chemin du fichier a creer."}

        elif any(m in texte for m in ["supprime", "efface", "retire"]):
            chemin = self._extraire_chemin(texte)
            if chemin:
                return {"action": "supprimer", "module": "fichiers", "parametres": {"chemin": chemin, "confirmation": True}}
            return {"action": "info", "message": "Precise le chemin du fichier a supprimer."}

        # --- Terminal (detecte processus avant les matchs generaux) ---
        if any(m in texte for m in ["processus", "programme en cours", "quoi tourne", "applications ouvertes", "logiciels ouverts", "quels sont les programmes", "quels sont les apps"]):
            return {"action": "liste_processus", "module": "terminal", "parametres": {}}

        elif any(m in texte for m in ["execute", "lance la commande", "dans le terminal", "commande shell"]):
            commande = self._extraire_commande(texte)
            if commande:
                return {"action": "executer", "module": "terminal", "parametres": {"commande": commande}}
            return {"action": "info", "message": "Quelle commande veux-tu executer ?"}

        # --- Ecran ---
        elif any(m in texte for m in ["capture l'ecran", "screenshot", "photo de l'ecran", "regarde mon ecran"]):
            return {"action": "capture", "module": "ecran", "parametres": {}}

        elif any(m in texte for m in ["taille ecran", "resolution", "dimension ecran"]):
            return {"action": "infos_ecran", "module": "ecran", "parametres": {}}

        # --- Controle + Vision ---
        elif any(m in texte for m in ["clique sur le texte", "clique sur l'element", "clique sur", "clic sur"]):
            texte_cible = self._extraire_texte_entre_guillemets(texte) or self._extraire_texte_apres_mot(texte, ["clique sur", "clic sur", "clique sur le texte", "clique sur l'element"])
            if texte_cible:
                if self.apprentissage_visuel:
                    pos = self.apprentissage_visuel.trouver_position(texte_cible)
                    if pos.get("succes"):
                        return {"action": "clic", "module": "controle", "parametres": {"x": pos["x"], "y": pos["y"]}}
                if self.vision:
                    return {"action": "clic_texte", "module": "vision", "parametres": {"texte": texte_cible}}
            coords = self._extraire_coordonnees(texte)
            if coords:
                return {"action": "clic", "module": "controle", "parametres": {"x": coords[0], "y": coords[1]}}
            return {"action": "info", "message": "Sur quoi cliquer ? (texte, coordonnees x,y, ou element appris)"}

        elif any(m in texte for m in ["clic", "clique en", "clique a"]):
            coords = self._extraire_coordonnees(texte)
            if coords:
                return {"action": "clic", "module": "controle", "parametres": {"x": coords[0], "y": coords[1]}}
            return {"action": "info", "message": "Donne les coordonnees x,y (ex: clic a 500,300)"}

        elif any(m in texte for m in ["apprends la position", "apprend la position", "memorise la position"]):
            nom = self._extraire_texte_apres_mot(texte, ["apprends la position de", "apprend la position de", "memorise la position de", "position de"])
            coords = self._extraire_coordonnees(texte)
            if nom and coords:
                return {"action": "apprendre_position", "module": "apprentissage_visuel", "parametres": {"nom": nom, "x": coords[0], "y": coords[1]}}
            return {"action": "info", "message": "Dis 'apprends la position de [nom] en x,y'"}

        elif any(m in texte for m in ["copie le texte de", "copie de", "selectionne le texte", "selectionne de", "selectionne entre"]):
            textes = self._extraire_texte_de_a(texte)
            if textes:
                return {"action": "selectionner_texte", "module": "selection", "parametres": textes}
            return {"action": "info", "message": "Precise le texte de debut et de fin : 'copie le texte de \"xxx\" a \"yyy\"'"}

        elif any(m in texte for m in ["selectionne tout", "selectionne tout le texte", "ctrl a"]):
            return {"action": "selectionner_tout", "module": "selection", "parametres": {}}

        elif any(m in texte for m in ["copie", "copier la selection", "ctrl c"]):
            return {"action": "copier", "module": "selection", "parametres": {}}

        elif any(m in texte for m in ["colle", "coller", "ctrl v"]):
            return {"action": "coller", "module": "selection", "parametres": {}}

        elif any(m in texte for m in ["trouve le texte", "trouve \"", "cherche le texte", "ou est le texte", "montre moi le texte"]):
            texte_cible = self._extraire_texte_entre_guillemets(texte) or self._extraire_contenu(texte)
            if texte_cible:
                return {"action": "trouver_texte", "module": "vision", "parametres": {"texte": texte_cible}}
            return {"action": "info", "message": "Quel texte trouver ?"}

        elif any(m in texte for m in ["oublie la position", "supprime la position"]):
            nom = self._extraire_texte_apres_mot(texte, ["position de", "la position de"])
            if nom:
                return {"action": "oublier_position", "module": "apprentissage_visuel", "parametres": {"nom": nom}}
            return {"action": "info", "message": "Quelle position oublier ?"}

        # --- Controle standard ---

        elif any(m in texte for m in ["deplace la souris", "souris a", "curseur a"]):
            coords = self._extraire_coordonnees(texte)
            if coords:
                return {"action": "deplacer_souris", "module": "controle", "parametres": {"x": coords[0], "y": coords[1]}}
            return {"action": "info", "message": "Donne les coordonnees x,y."}

        elif any(m in texte for m in ["tape", "ecris avec le clavier", "saisis"]):
            texte_a_taper = self._extraire_contenu(texte)
            return {"action": "taper_texte", "module": "controle", "parametres": {"texte": texte_a_taper}}

        elif any(m in texte for m in ["appuie sur", "touche ", "presse "]):
            touche = self._extraire_touche(texte)
            if touche:
                return {"action": "touche", "module": "controle", "parametres": {"touche": touche}}
            return {"action": "info", "message": "Quelle touche appuyer ? (Enter, Escape, Tab, etc.)"}

        elif any(m in texte for m in ["ouvre l'application", "lance le programme", "demarre ", "ouvrir ", "ouvrir l'application", "ouvrir le programme", "ouvrir le fichier", "ouvrir un "]):
            app = self._extraire_application(texte)
            if app:
                return {"action": "lancer_app", "module": "controle", "parametres": {"chemin": app}}
            return {"action": "info", "message": "Quelle application lancer ?"}

        # --- Navigateur ---
        elif any(m in texte for m in ["ouvre youtube"]):
            return {"action": "ouvrir_url", "module": "navigateur", "parametres": {"url": "https://youtube.com"}}
        elif any(m in texte for m in ["ouvre google"]):
            return {"action": "ouvrir_url", "module": "navigateur", "parametres": {"url": "https://google.com"}}
        elif any(m in texte for m in ["ouvre le site", "va sur", "navigue vers", "url ", "site web"]):
            url = self._extraire_url(texte)
            if url:
                return {"action": "ouvrir_url", "module": "navigateur", "parametres": {"url": url}}
            return {"action": "info", "message": "Quelle URL ouvrir ?"}

        elif any(m in texte for m in ["cherche sur internet", "recherche sur internet", "cherche sur le web", "recherche sur le web", "google "]):
            requete = self._extraire_contenu(texte) or texte
            return {"action": "rechercher_web", "module": "navigateur", "parametres": {"requete": requete, "moteur": "duckduckgo"}}
        elif any(m in texte for m in ["cherche ", "recherche "]):
            # Si le contexte precedent mentionne youtube, google, etc., c'est une recherche web
            # Sinon on peut chercher un fichier ou sur le web
            requete = self._extraire_contenu(texte) or texte
            # Par defaut : recherche web
            return {"action": "rechercher_web", "module": "navigateur", "parametres": {"requete": requete, "moteur": "duckduckgo"}}

        elif any(m in texte for m in ["ouvre le fichier avec", "ouvre avec", "application par defaut"]):
            chemin = self._extraire_chemin(texte)
            if chemin:
                return {"action": "ouvrir_fichier", "module": "navigateur", "parametres": {"chemin": chemin}}
            return {"action": "info", "message": "Quel fichier ouvrir ?"}

        return {"action": "inconnu", "message": "Je ne comprends pas quelle action systeme tu veux. Essaie d'etre plus precis."}

    def executer(self, instruction):
        """Execute une instruction et retourne le resultat."""
        action = instruction.get("action")
        module = instruction.get("module")
        params = instruction.get("parametres", {})

        resultat = None

        if module == "fichiers":
            if action == "lister":
                resultat = self.fichiers.lister(params.get("chemin", "."))
            elif action == "lire_fichier":
                resultat = self.fichiers.lire(params.get("chemin"))
            elif action == "chercher_fichier":
                resultat = self.fichiers.chercher(params.get("dossier", "."), pattern=params.get("pattern", "*"))
            elif action == "ecrire_fichier":
                resultat = self.fichiers.ecrire(params.get("chemin"), params.get("contenu", ""))
            elif action == "supprimer":
                resultat = self.fichiers.supprimer(params.get("chemin"), confirmation=params.get("confirmation", True))
            elif action == "info_fichier":
                resultat = self.fichiers.info(params.get("chemin"))

        elif module == "terminal":
            if action == "executer":
                resultat = self.terminal.executer(params.get("commande", ""))
            elif action == "liste_processus":
                resultat = self.terminal.liste_processus()

        elif module == "ecran":
            if action == "capture":
                resultat = self.ecran.capture()
            elif action == "infos_ecran":
                resultat = self.ecran.infos_ecran()

        elif module == "controle":
            if action == "clic":
                resultat = self.controle.clic(params.get("x", 0), params.get("y", 0))
            elif action == "deplacer_souris":
                resultat = self.controle.deplacer_souris(params.get("x", 0), params.get("y", 0))
            elif action == "taper_texte":
                resultat = self.controle.taper_texte(params.get("texte", ""))
            elif action == "touche":
                resultat = self.controle.touche(params.get("touche", ""))
            elif action == "lancer_app":
                resultat = self.controle.lancer_application(params.get("chemin", ""))

        elif module == "navigateur":
            if action == "ouvrir_url":
                resultat = self.navigateur.ouvrir_url(params.get("url", ""))
            elif action == "rechercher_web":
                resultat = self.navigateur.rechercher_web(params.get("requete", ""), params.get("moteur", "duckduckgo"))
            elif action == "ouvrir_fichier":
                resultat = self.navigateur.ouvrir_fichier(params.get("chemin", ""))

        elif module == "vision":
            if action == "clic_texte":
                if self.vision:
                    trouve = self.vision.trouver_texte(params.get("texte", ""))
                    if trouve.get("succes"):
                        resultat = self.controle.clic(trouve["x"], trouve["y"])
                        # Apprend la position si apprentissage visuel est disponible
                        if self.apprentissage_visuel:
                            self.apprentissage_visuel.apprendre_position(params.get("texte", ""), trouve["x"], trouve["y"])
                    else:
                        resultat = trouve
                else:
                    resultat = {"erreur": "Vision ecran non disponible. Installe Tesseract."}
            elif action == "trouver_texte":
                if self.vision:
                    resultat = self.vision.trouver_texte(params.get("texte", ""))
                else:
                    resultat = {"erreur": "Vision ecran non disponible. Installe Tesseract."}
            elif action == "lister_elements":
                if self.vision:
                    resultat = {"elements": self.vision.lister_elements_visibles()}
                else:
                    resultat = {"erreur": "Vision ecran non disponible. Installe Tesseract."}

        elif module == "selection":
            if action == "selectionner_texte":
                if self.selection:
                    p = params.get("debut"), params.get("fin")
                    if p[0] and p[1]:
                        resultat = self.selection.selectionner_texte(p[0], p[1])
                    else:
                        resultat = {"erreur": "Precise le texte de debut et de fin."}
                else:
                    resultat = {"erreur": "Selection non disponible."}
            elif action == "selectionner_tout":
                if self.selection:
                    resultat = self.selection.selectionner_tout()
                else:
                    resultat = {"erreur": "Selection non disponible."}
            elif action == "copier":
                if self.selection:
                    resultat = self.selection.copier_selection()
                else:
                    resultat = {"erreur": "Selection non disponible."}
            elif action == "coller":
                if self.selection:
                    resultat = self.selection.coller()
                else:
                    resultat = {"erreur": "Selection non disponible."}

        elif module == "apprentissage_visuel":
            if action == "apprendre_position":
                if self.apprentissage_visuel:
                    resultat = self.apprentissage_visuel.apprendre_position(
                        params.get("nom", ""), params.get("x", 0), params.get("y", 0)
                    )
                else:
                    resultat = {"erreur": "Apprentissage visuel non disponible."}
            elif action == "oublier_position":
                if self.apprentissage_visuel:
                    resultat = self.apprentissage_visuel.oublier(params.get("nom", ""))
                else:
                    resultat = {"erreur": "Apprentissage visuel non disponible."}
            elif action == "lister_positions":
                if self.apprentissage_visuel:
                    resultat = {"positions": self.apprentissage_visuel.lister_positions()}
                else:
                    resultat = {"erreur": "Apprentissage visuel non disponible."}

        self.historique.append({
            "instruction": instruction,
            "resultat": resultat,
            "date": datetime.now().strftime("%H:%M:%S")
        })

        return resultat

    # --- Extracteurs ---
    def _extraire_chemin(self, texte):
        """Extrait un chemin de fichier/dossier du texte."""
        # Cherche entre guillemets ou apostrophes
        for delim in ['"', "'", "`"]:
            if delim in texte:
                parties = texte.split(delim)
                if len(parties) >= 3:
                    return parties[1]
        # Cherche un chemin avec / ou \
        mots = texte.split()
        for mot in mots:
            if mot.startswith(("/", "~", ".", "C:", "D:", "Users", "Desktop", "Documents")):
                return mot
            if "/" in mot or "\\" in mot:
                return mot
        return None

    def _extraire_commande(self, texte):
        """Extrait une commande shell du texte."""
        # Cherche apres "execute" ou "commande"
        for marqueur in ["execute :", "commande :", "lance la commande", "dans le terminal", "execute "]:
            if marqueur in texte.lower():
                idx = texte.lower().find(marqueur) + len(marqueur)
                return texte[idx:].strip().strip('"').strip("'")
        return None

    def _extraire_coordonnees(self, texte):
        """Extrait des coordonnees x,y du texte."""
        # Cherche des nombres separes par virgule
        import re
        match = re.search(r'(\d+)[,\s]+(\d+)', texte)
        if match:
            return int(match.group(1)), int(match.group(2))
        return None

    def _extraire_contenu(self, texte):
        """Extrait du contenu texte (entre guillemets ou apres un marqueur)."""
        for delim in ['"', "'", "`"]:
            if delim in texte:
                parties = texte.split(delim)
                if len(parties) >= 3:
                    return parties[1]
        return texte

    def _extraire_touche(self, texte):
        """Extrait le nom d'une touche."""
        mots = texte.split()
        for i, mot in enumerate(mots):
            if mot.lower() in ["touche", "appuie", "presse"] and i+1 < len(mots):
                return mots[i+1]
        return None

    def _extraire_application(self, texte):
        """Extrait le nom d'une application."""
        for marqueur in ["lance le programme", "demarre", "ouvre l'application", "ouvre le programme", "ouvrir l'application", "ouvrir le programme", "ouvrir un ", "ouvrir le ", "ouvrir "]:
            if marqueur in texte.lower():
                idx = texte.lower().find(marqueur) + len(marqueur)
                reste = texte[idx:].strip().strip('"').strip("'")
                # Arrete au premier "et" ou "puis"
                for fin in [" et ", " puis ", " ensuite ", ","]:
                    if fin in reste.lower():
                        reste = reste[:reste.lower().find(fin)].strip()
                return reste
        return None

    def _extraire_url(self, texte):
        """Extrait une URL du texte."""
        import re
        urls = re.findall(r'https?://[^\s]+', texte)
        if urls:
            return urls[0]
        # Cherche un nom de domaine
        mots = texte.split()
        for mot in mots:
            if "." in mot and not mot.endswith((",", ".", "!", "?")):
                # Retire la ponctuation de fin
                mot = mot.strip(".,!?;:")
                if "." in mot and len(mot) > 3:
                    return mot
        return None

    def _extraire_texte_entre_guillemets(self, texte):
        """Extrait du texte entre guillemets doubles ou simples."""
        import re
        match = re.search(r'["\']([^"\']+)["\']', texte)
        if match:
            return match.group(1)
        return None

    def _extraire_texte_apres_mot(self, texte, mots_cles):
        """Extrait le texte qui suit un mot-cle."""
        for mot in mots_cles:
            if mot in texte.lower():
                idx = texte.lower().find(mot) + len(mot)
                reste = texte[idx:].strip()
                # Arrete au premier marqueur de fin (en, a, pour, depuis, etc.)
                for fin in [" en ", " a ", " pour ", " depuis ", " et ", " puis ", ",", ";"]:
                    if fin in reste.lower():
                        reste = reste[:reste.lower().find(fin)].strip()
                # Nettoie les guillemets
                reste = reste.strip('"').strip("'")
                return reste
        return None

    def _extraire_texte_de_a(self, texte):
        """Extrait deux textes: 'de "xxx" a "yyy"'."""
        import re
        # Cherche : de "..." a "..." ou de ... a ...
        match = re.search(r'de\s+["\']?([^"\']+)["\']?\s+a\s+["\']?([^"\']+)["\']?', texte, re.IGNORECASE)
        if match:
            return {"debut": match.group(1).strip(), "fin": match.group(2).strip()}
        # Cherche : de ... jusqu'a ...
        match = re.search(r'de\s+["\']?([^"\']+)["\']?\s+jusqu[\'\']?\s+a?\s+["\']?([^"\']+)["\']?', texte, re.IGNORECASE)
        if match:
            return {"debut": match.group(1).strip(), "fin": match.group(2).strip()}
        return None

    def historique_actions(self, n=10):
        return self.historique[-n:]

if __name__ == "__main__":
    from systeme.fichiers import Fichiers
    from systeme.terminal import Terminal
    from systeme.ecran import Ecran
    from systeme.controle import Controle
    from systeme.navigateur import Navigateur

    o = Orchestrateur(Fichiers(), Terminal(), Ecran(), Controle(), Navigateur())
    tests = [
        "liste le contenu du dossier /workspace",
        "lis le fichier isabella.py",
        "cherche un fichier nomme *.py dans /workspace",
        "execute la commande : echo 'hello'",
        "capture l'ecran",
        "clique en 500,300",
        "ouvre le site google.com",
        "recherche sur internet python tutorial",
        "appuie sur Enter"
    ]
    for t in tests:
        print(f"\n>>> {t}")
        instruction = o.analyser_commande(t)
        print(f"Action detectee : {instruction}")
        if instruction.get("action") not in ["inconnu", "info"]:
            resultat = o.executer(instruction)
            print(f"Resultat : {resultat}")
