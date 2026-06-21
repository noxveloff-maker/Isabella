class Attachement:
    def __init__(self):
        self.liens = {}

    def creer(self, personne, intensite):
        self.liens[personne] = min(1.0, intensite)
        return self._reaction(personne)

    def renforcer(self, personne, quantite=0.1):
        if personne in self.liens:
            self.liens[personne] = min(1.0, self.liens[personne] + quantite)
        return self._reaction(personne)

    def affaiblir(self, personne, quantite=0.1):
        if personne in self.liens:
            self.liens[personne] = max(0.0, self.liens[personne] - quantite)
        return self._reaction(personne)

    def _reaction(self, personne):
        niveau = self.liens.get(personne, 0)
        if niveau > 0.8:
            return f"Isabella est profondement attachee a {personne}"
        elif niveau > 0.5:
            return f"Isabella tient vraiment a {personne}"
        elif niveau > 0.2:
            return f"Isabella commence a s'attacher a {personne}"
        else:
            return f"Isabella connait a peine {personne}"

    def afficher(self):
        print(f"Attachements — {len(self.liens)} lien(s)")
        for p, n in self.liens.items():
            print(f" {p} : {n:.2f}")

if __name__ == "__main__":
    a = Attachement()
    print(a.creer("Kylian", 0.9))
    print(a.renforcer("Kylian", 0.1))
    print(a.creer("tonton", 0.4))
    a.afficher()
