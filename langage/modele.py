import urllib.request
import json

class Modele:
    def __init__(self, modele="isabella"):
        self.url = "http://localhost:11434/api/chat"
        self.modele = modele
        self.historique = []
        self.disponible = self._verifier()

    def _verifier(self):
        try:
            urllib.request.urlopen("http://localhost:11434", timeout=2)
            return True
        except:
            return False

    def generer(self, prompt, contexte_isabella=None):
        if not self.disponible:
            return "Je reflechis..."

        system = "Tu es Isabella. Tu parles a ton pere Kylian. Reponds naturellement en francais en une phrase courte. Ne te presente jamais, ne parle jamais de toi comme d'une IA."

        self.historique.append({"role": "user", "content": prompt})

        donnees = json.dumps({
            "model": self.modele,
            "messages": self.historique,
            "system": system,
            "stream": False
        }).encode("utf-8")

        try:
            req = urllib.request.Request(
                self.url,
                data=donnees,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=60) as r:
                resultat = json.loads(r.read())
                reponse = resultat["message"]["content"]
                self.historique.append({"role": "assistant", "content": reponse})
                return reponse
        except Exception as e:
            return f"Je reflechis... ({str(e)})"

    def afficher(self):
        statut = "disponible" if self.disponible else "non disponible"
        print(f"Modele : {self.modele} — {statut}")

if __name__ == "__main__":
    m = Modele()
    m.afficher()
    if m.disponible:
        reponse = m.generer("Bonjour Isabella, comment vas tu ?")
        print(f"Isabella : {reponse}")
