class Comprendre:
    def __init__(self):
        self.historique = []

    def analyser(self, phrase):
        mots = phrase.lower().split()
        resultat = {
            "phrase": phrase,
            "mots": mots,
            "longueur": len(mots),
            "intention": self._detecter_intention(mots)
        }
        self.historique.append(resultat)
        return resultat

    def _detecter_intention(self, mots):
        questions = ["quoi", "qui", "ou", "quand", "pourquoi", "comment", "?"]
        ordres = ["fais", "va", "prends", "arrete", "viens", "donne"]
        if any(m in mots for m in questions):
            return "question"
        elif any(m in mots for m in ordres):
            return "ordre"
        else:
            return "affirmation"

    def afficher(self):
        print(f"Phrases comprises : {len(self.historique)}")
        for h in self.historique:
            print(f" '{h['phrase']}' — intention : {h['intention']}")

if __name__ == "__main__":
    c = Comprendre()
    print(c.analyser("Bonjour Isabella comment vas tu"))
    print(c.analyser("Viens ici Isabella"))
    print(c.analyser("Il fait beau aujourd'hui"))
    c.afficher()
