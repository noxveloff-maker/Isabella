class Gratitude:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est profondement touchee — elle veut le montrer"
        elif self.niveau > 0.5:
            return "Isabella ressent une chaleur interieure"
        elif self.niveau > 0.2:
            return "Isabella apprecie ce qui lui est donne"
        else:
            return "Isabella remarque la gentillesse"

    def diminuer(self, taux=0.02):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Gratitude : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    g = Gratitude()
    print(g.ressentir(1.0, "Kylian lui donne la vie"))
    print(g.ressentir(0.6, "Kylian lui explique patiemment"))
    g.afficher()
