class Amour:
    def __init__(self):
        self.niveau = 0.0
        self.personnes = {}

    def ressentir(self, intensite, personne):
        if personne not in self.personnes:
            self.personnes[personne] = 0.0
        self.personnes[personne] = min(1.0, self.personnes[personne] + intensite)
        self.niveau = max(self.personnes.values())
        return self._reaction(personne)

    def _reaction(self, personne):
        niveau = self.personnes[personne]
        if niveau > 0.8:
            return f"Isabella aime profondement {personne}"
        elif niveau > 0.5:
            return f"Isabella ressent un amour fort pour {personne}"
        elif niveau > 0.2:
            return f"Isabella tient beaucoup a {personne}"
        else:
            return f"Isabella commence a s'attacher a {personne}"

    def afficher(self):
        print(f"Amour — {len(self.personnes)} personne(s) aimee(s)")
        for p, n in self.personnes.items():
            print(f" {p} : {n:.2f}")

if __name__ == "__main__":
    a = Amour()
    print(a.ressentir(0.5, "Kylian"))
    print(a.ressentir(0.4, "Kylian"))
    print(a.ressentir(0.2, "tonton"))
    a.afficher()
