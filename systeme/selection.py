import time

class Selection:
    """
    Selectionne du texte ou des elements a l'ecran en cliquant-glissant.
    Copie la selection dans le presse-papier.
    """

    def __init__(self, controle, vision_ecran=None):
        self.controle = controle
        self.vision = vision_ecran

    def selectionner_texte(self, texte_debut, texte_fin=None):
        """
        Selectionne du texte a l'ecran en cliquant sur le debut et glissant jusqu'a la fin.
        Si texte_fin est None, fait un double-clic sur le texte (selectionne le mot).
        """
        if not self.vision:
            return {"erreur": "Vision ecran non disponible"}

        # Trouve le texte de debut
        resultat_debut = self.vision.trouver_texte(texte_debut)
        if resultat_debut.get("erreur"):
            return resultat_debut

        x1 = resultat_debut["x"]
        y1 = resultat_debut["y"]

        if texte_fin is None:
            # Double-clic pour selectionner le mot
            self.controle.clic(x1, y1, double=True)
            time.sleep(0.2)
            self.copier_selection()
            return {
                "succes": True,
                "action": "double_clic",
                "texte": texte_debut,
                "position": (x1, y1)
            }

        # Trouve le texte de fin
        resultat_fin = self.vision.trouver_texte(texte_fin)
        if resultat_fin.get("erreur"):
            return resultat_fin

        x2 = resultat_fin["x"]
        y2 = resultat_fin["y"]

        # Clic au debut, maintien, glisse jusqu'a la fin, relache
        self._clic_glisser(x1, y1, x2, y2)
        time.sleep(0.2)
        self.copier_selection()

        return {
            "succes": True,
            "action": "selection_glisser",
            "texte_debut": texte_debut,
            "texte_fin": texte_fin,
            "debut": (x1, y1),
            "fin": (x2, y2)
        }

    def selectionner_zone(self, x1, y1, x2, y2):
        """Selectionne une zone en cliquant-glissant entre deux coordonnees."""
        self._clic_glisser(x1, y1, x2, y2)
        time.sleep(0.2)
        self.copier_selection()
        return {
            "succes": True,
            "action": "selection_zone",
            "debut": (x1, y1),
            "fin": (x2, y2)
        }

    def selectionner_tout(self):
        """Selectionne tout (Ctrl+A)."""
        self._touche_combinaison("ctrl", "a")
        time.sleep(0.1)
        self.copier_selection()
        return {"succes": True, "action": "selection_tout"}

    def copier_selection(self):
        """Copie la selection dans le presse-papier (Ctrl+C)."""
        self._touche_combinaison("ctrl", "c")
        return {"succes": True, "action": "copier"}

    def coller(self):
        """Colle le contenu du presse-papier (Ctrl+V)."""
        self._touche_combinaison("ctrl", "v")
        return {"succes": True, "action": "coller"}

    def _clic_glisser(self, x1, y1, x2, y2):
        """Effectue un clic-glisser entre deux points."""
        # Deplace la souris au point de depart
        self.controle.deplacer_souris(x1, y1)
        time.sleep(0.1)
        # Appuie sur le bouton gauche
        self._mouse_down()
        time.sleep(0.1)
        # Glisse jusqu'au point d'arrivee
        self._mouse_move(x2, y2)
        time.sleep(0.1)
        # Relache
        self._mouse_up()
        time.sleep(0.1)

    def _mouse_down(self):
        """Appuie sur le bouton gauche de la souris."""
        import ctypes
        if self.controle.systeme == "windows":
            ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
        elif self.controle.systeme == "darwin":
            import os
            os.system("cliclick dd")
        else:
            import os
            os.system("xdotool mousedown 1")

    def _mouse_up(self):
        """Relache le bouton gauche de la souris."""
        import ctypes
        if self.controle.systeme == "windows":
            ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
        elif self.controle.systeme == "darwin":
            import os
            os.system("cliclick du")
        else:
            import os
            os.system("xdotool mouseup 1")

    def _mouse_move(self, x, y):
        """Deplace la souris (pendant le glissement)."""
        self.controle.deplacer_souris(x, y)

    def _touche_combinaison(self, touche1, touche2):
        """Appuie sur une combinaison de touches (Ctrl+C, Ctrl+V, etc.)."""
        systeme = self.controle.systeme

        if systeme == "windows":
            # Utilise pyautogui ou keybd_event
            try:
                import pyautogui
                pyautogui.keyDown(touche1)
                pyautogui.keyDown(touche2)
                pyautogui.keyUp(touche2)
                pyautogui.keyUp(touche1)
            except ImportError:
                pass
        elif systeme == "darwin":
            import os
            mod = "cmd" if touche1 in ["ctrl", "cmd"] else touche1
            os.system(f"osascript -e 'tell application \"System Events\" to key down {mod}' -e 'tell application \"System Events\" to keystroke \"{touche2}\"' -e 'tell application \"System Events\" to key up {mod}'")
        else:
            import os
            os.system(f"xdotool key {touche1}+{touche2}")

if __name__ == "__main__":
    from systeme.controle import Controle
    from systeme.vision_ecran import VisionEcran

    c = Controle()
    v = VisionEcran()
    s = Selection(c, v)

    print("=== Test Selection ===")
    print(f"Systeme: {c.systeme}")
    print("Pour tester:")
    print("  1. Ouvre un fichier texte avec 'Bonjour le monde' visible")
    print("  2. s.selectionner_texte('Bonjour')")
    print("  3. s.selectionner_texte('Bonjour', 'monde')")
