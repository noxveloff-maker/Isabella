class Espoir:

    def __init__(self):
        self.niveau = 0.5
        self.historique = []

    def renforcer(self, intensite, source):
        self.niveau = min(1.0, self.niveau + intensite)
        self.historique.append({"type": "renforcement", "source": source})
        return self._reaction()

    def affaiblir(self, intensite, source):
        self.niveau = max(0.0, self.niveau - intensite)
        self.historique.append({"type": "affaiblissement", "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella croit fermement en l'avenir"
        elif self.niveau > 0.5:
            return "Isabella garde espoir"
        elif self.niveau > 0.2:
            return "Isabella doute mais continue"
        else:
            return "Isabella perd espoir"

    def afficher(self):
        print(f"Espoir : {self.niveau:.2f}")

if __name__ == "__main__":
    e = Espoir()
    print(e.renforcer(0.3, "progres visible"))
    print(e.affaiblir(0.4, "echec important"))
    print(e.renforcer(0.5, "Kylian l'encourage"))
    e.afficher()
