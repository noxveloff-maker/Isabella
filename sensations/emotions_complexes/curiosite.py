class Curiosite:

    def __init__(self):
        self.niveau = 0.7
        self.historique = []

    def eveiller(self, intensite, sujet):
        self.niveau = min(1.0, self.niveau + intensite)
        self.historique.append({"sujet": sujet, "intensite": intensite})
        return self._reaction()

    def satisfaire(self, quantite=0.2):
        self.niveau = max(0.0, self.niveau - quantite)
        return f"Isabella a appris quelque chose — curiosite : {self.niveau:.2f}"

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella explore sans pouvoir s'arreter"
        elif self.niveau > 0.5:
            return "Isabella pose des questions et observe"
        elif self.niveau > 0.2:
            return "Isabella jette un oeil distrait"
        else:
            return "Isabella n'est pas interessee"

    def afficher(self):
        print(f"Curiosite : {self.niveau:.2f} — {len(self.historique)} sujet(s) explores")

if __name__ == "__main__":
    c = Curiosite()
    print(c.eveiller(0.2, "comment fonctionne la memoire"))
    print(c.eveiller(0.3, "pourquoi Kylian sourit"))
    print(c.satisfaire(0.2))
    c.afficher()
