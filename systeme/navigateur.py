import os
import platform
import webbrowser
from datetime import datetime

class Navigateur:
    """Ouvre des URLs, des fichiers, et interagit avec le web."""

    def __init__(self):
        self.historique = []
        self.systeme = platform.system().lower()

    def ouvrir_url(self, url):
        """Ouvre une URL dans le navigateur par defaut."""
        if not url.startswith(("http://", "https://", "file://")):
            url = "https://" + url

        try:
            webbrowser.open(url)
            self._log("ouvrir_url", url)
            return {"succes": True, "url": url}
        except Exception as e:
            return {"erreur": f"Impossible d'ouvrir : {e}"}

    def ouvrir_fichier(self, chemin):
        """Ouvre un fichier avec l'application associee."""
        chemin = os.path.expanduser(chemin)
        if not os.path.exists(chemin):
            return {"erreur": f"Fichier introuvable : {chemin}"}

        try:
            if self.systeme == "windows":
                os.startfile(chemin)
            elif self.systeme == "darwin":
                os.system(f"open '{chemin}'")
            else:
                os.system(f"xdg-open '{chemin}' &")
            self._log("ouvrir_fichier", chemin)
            return {"succes": True, "chemin": chemin}
        except Exception as e:
            return {"erreur": f"Erreur ouverture : {e}"}

    def rechercher_web(self, requete, moteur="google"):
        """Construit une URL de recherche web."""
        import urllib.parse
        requete_enc = urllib.parse.quote(requete)
        moteurs = {
            "google": f"https://www.google.com/search?q={requete_enc}",
            "duckduckgo": f"https://duckduckgo.com/?q={requete_enc}",
            "bing": f"https://www.bing.com/search?q={requete_enc}",
            "youtube": f"https://www.youtube.com/results?search_query={requete_enc}",
            "wikipedia": f"https://fr.wikipedia.org/wiki/Special:Search?search={requete_enc}"
        }
        url = moteurs.get(moteur, moteurs["google"])
        return self.ouvrir_url(url)

    def historique_navigation(self, n=10):
        return self.historique[-n:]

    def _log(self, action, cible):
        self.historique.append({
            "action": action,
            "cible": cible,
            "date": datetime.now().strftime("%H:%M:%S")
        })

if __name__ == "__main__":
    n = Navigateur()
    print("=== Test navigateur ===")
    print("Systeme :", n.systeme)
    print("\nRecherche web :")
    print(n.rechercher_web("python tutoriel", "duckduckgo"))
