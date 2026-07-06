import urllib.request
import json

class Modele:
    def __init__(self, modele="mistral"):
        self.url = "http://localhost:11434/api/chat"
        self.modele = modele
        self.historique = []
        self.disponible = self._verifier()
        self._system_prompt = None

    def _verifier(self):
        try:
            urllib.request.urlopen("http://localhost:11434", timeout=2)
            return True
        except:
            return False

    def set_system_prompt(self, prompt):
        """Definit le prompt systeme complet (contexte + outils + personnalite)."""
        self._system_prompt = prompt

    def generer(self, prompt, system=None, ajouter_historique=True):
        """
        Genere une reponse du LLM.
        Si 'system' est fourni, il remplace temporairement le system prompt.
        """
        if not self.disponible:
            return "Je reflechis... (Ollama n'est pas demarre)"

        systeme_effectif = system or self._system_prompt or (
            "Tu es Isabella. Tu parles a ton pere Kylian. "
            "Reponds naturellement en francais en une phrase courte. "
            "Ne te presente jamais, ne parle jamais de toi comme d'une IA."
        )

        if ajouter_historique:
            self.historique.append({"role": "user", "content": prompt})

        messages = []
        if systeme_effectif:
            messages.append({"role": "system", "content": systeme_effectif})
        messages.extend(self.historique)

        donnees = json.dumps({
            "model": self.modele,
            "messages": messages,
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
                if ajouter_historique:
                    self.historique.append({"role": "assistant", "content": reponse})
                return reponse
        except Exception as e:
            return f"Je reflechis... (erreur : {str(e)})"

    def generer_avec_resultat(self, prompt_utilisateur, resultat_outil, prompt_systeme=None):
        """
        Genere une reponse apres avoir execute un outil.
        Le prompt_utilisateur est le message original de Kylian.
        Le resultat_outil est le dictionnaire retourne par l'outil.
        """
        prompt = (
            f"Kylian t'a demande : '{prompt_utilisateur}'\n\n"
            f"Tu as utilise un outil. Voici le resultat brut :\n"
            f"{json.dumps(resultat_outil, ensure_ascii=False, indent=2)}\n\n"
            f"Formule une reponse naturelle, chaleureuse, en francais. "
            f"Resume le resultat de maniere lisible."
        )
        return self.generer(prompt, system=prompt_systeme, ajouter_historique=True)

    def reset_historique(self):
        """Reinitialise l'historique de conversation."""
        self.historique = []

    def afficher(self):
        statut = "disponible" if self.disponible else "non disponible"
        print(f"Modele : {self.modele} — {statut}")
        print(f"Historique : {len(self.historique)} messages")

if __name__ == "__main__":
    m = Modele()
    m.afficher()
    if m.disponible:
        reponse = m.generer("Bonjour Isabella, comment vas tu ?")
        print(f"Isabella : {reponse}")
