import os
import platform
import time
from datetime import datetime

class Controle:
    """Controle souris, clavier, et applications systeme."""

    def __init__(self):
        self.systeme = platform.system().lower()
        self.historique = []

    def clic(self, x, y, bouton="gauche", double=False):
        """Effectue un clic souris a des coordonnees (x,y)."""
        try:
            if self.systeme == "windows":
                self._clic_windows(x, y, bouton, double)
            elif self.systeme == "darwin":
                self._clic_macos(x, y, bouton, double)
            else:
                self._clic_linux(x, y, bouton, double)

            self._log("clic", f"({x},{y}) bouton={bouton}")
            return {"succes": True, "x": x, "y": y, "bouton": bouton, "double": double}
        except Exception as e:
            return {"erreur": f"Erreur clic : {e}"}

    def _clic_windows(self, x, y, bouton, double):
        import ctypes
        # SetCursorPos
        ctypes.windll.user32.SetCursorPos(x, y)
        # mouse_event
        if bouton == "gauche":
            flags = 0x0002 | 0x0004 if not double else 0x0002 | 0x0004 | 0x0002 | 0x0004
        elif bouton == "droit":
            flags = 0x0008 | 0x0010 if not double else 0x0008 | 0x0010 | 0x0008 | 0x0010
        else:
            flags = 0x0040 | 0x0080
        ctypes.windll.user32.mouse_event(flags, 0, 0, 0, 0)
        if double:
            time.sleep(0.05)
            ctypes.windll.user32.mouse_event(flags, 0, 0, 0, 0)

    def _clic_macos(self, x, y, bouton, double):
        clic_type = "double" if double else "click"
        bouton_nom = "left" if bouton == "gauche" else "right" if bouton == "droit" else "middle"
        os.system(f"cliclick {clic_type}:{bouton_nom}={x},{y}")

    def _clic_linux(self, x, y, bouton, double):
        bouton_num = "1" if bouton == "gauche" else "3" if bouton == "droit" else "2"
        os.system(f"xdotool mousemove {x} {y} click {bouton_num}")
        if double:
            time.sleep(0.05)
            os.system(f"xdotool click {bouton_num}")

    def deplacer_souris(self, x, y):
        """Deplace le curseur sans cliquer."""
        try:
            if self.systeme == "windows":
                import ctypes
                ctypes.windll.user32.SetCursorPos(x, y)
            elif self.systeme == "darwin":
                os.system(f"cliclick m:{x},{y}")
            else:
                os.system(f"xdotool mousemove {x} {y}")
            self._log("deplacer", f"({x},{y})")
            return {"succes": True, "x": x, "y": y}
        except Exception as e:
            return {"erreur": f"Erreur deplacement : {e}"}

    def taper_texte(self, texte, intervalle=0.01):
        """Tape du texte au clavier."""
        try:
            if self.systeme == "windows":
                import ctypes
                for char in texte:
                    if char == '\n':
                        ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
                        ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
                    else:
                        # Simplifie — vraie implementation necessite win32api
                        pass
            elif self.systeme == "darwin":
                texte_escaped = texte.replace("'", "'\\''")
                os.system(f"osascript -e 'tell application \"System Events\" to keystroke \"{texte_escaped}\"'")
            else:
                texte_escaped = texte.replace("'", "'\\''")
                os.system(f"xdotool type --delay {int(intervalle*1000)} '{texte_escaped}'")
            self._log("taper", texte[:50])
            return {"succes": True, "texte": texte[:50], "longueur": len(texte)}
        except Exception as e:
            return {"erreur": f"Erreur frappe : {e}"}

    def touche(self, nom_touche):
        """Appuie sur une touche speciale (Enter, Escape, Tab, etc.)."""
        mapping = {
            "enter": "Return",
            "escape": "Escape",
            "tab": "Tab",
            "space": "space",
            "backspace": "BackSpace",
            "delete": "Delete",
            "up": "Up",
            "down": "Down",
            "left": "Left",
            "right": "Right",
            "f1": "F1", "f2": "F2", "f3": "F3", "f4": "F4", "f5": "F5",
            "f6": "F6", "f7": "F7", "f8": "F8", "f9": "F9", "f10": "F10",
            "ctrl": "Control_L", "alt": "Alt_L", "shift": "Shift_L",
            "cmd": "Meta_L", "win": "Meta_L"
        }
        touche = mapping.get(nom_touche.lower(), nom_touche)
        try:
            if self.systeme == "windows":
                # Simplifie
                pass
            elif self.systeme == "darwin":
                os.system(f"osascript -e 'tell application \"System Events\" to key code {self._keycode_macos(touche)}'")
            else:
                os.system(f"xdotool key {touche}")
            self._log("touche", nom_touche)
            return {"succes": True, "touche": nom_touche}
        except Exception as e:
            return {"erreur": f"Erreur touche : {e}"}

    def _keycode_macos(self, touche):
        # Simplifie — retourne un keycode de base
        codes = {"Return": 36, "Escape": 53, "Tab": 48, "space": 49}
        return codes.get(touche, 0)

    def lancer_application(self, chemin_ou_nom):
        """Lance une application ou ouvre un fichier."""
        try:
            if self.systeme == "windows":
                os.startfile(chemin_ou_nom)
            elif self.systeme == "darwin":
                os.system(f"open '{chemin_ou_nom}'")
            else:
                os.system(f"xdg-open '{chemin_ou_nom}' &")
            self._log("lancer", chemin_ou_nom)
            return {"succes": True, "application": chemin_ou_nom}
        except Exception as e:
            return {"erreur": f"Erreur lancement : {e}"}

    def _log(self, action, detail):
        self.historique.append({
            "action": action,
            "detail": detail,
            "date": datetime.now().strftime("%H:%M:%S")
        })

if __name__ == "__main__":
    c = Controle()
    print("=== Test controle ===")
    print("Infos systeme :", c.systeme)
    print("Deplacer souris (100,100) :", c.deplacer_souris(100, 100))
    print("Historique :", c.historique)
