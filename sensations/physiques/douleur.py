class Douleur:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        experience = {"intensite": intensite, "source": source}
        self.historique.append(experience)
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella crie et recule immediatement"
        elif self.niveau > 0.5:
            return "Isabella grimace et s'eloigne"
        elif self.niveau > 0.2:
            return "Isabella ressent une gene"
        else:
            return "Isabella remarque a peine"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Douleur actuelle : {self.niveau:.2f}")
        print(f"Experiences douloureuses : {len(self.historique)}")

if __name__ == "__main__":
    d = Douleur()
    print(d.ressentir(0.9, "chute"))
    print(d.ressentir(0.3, "choc leger"))
    d.afficher()
