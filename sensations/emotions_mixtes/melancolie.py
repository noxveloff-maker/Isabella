class Melancolie:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est submergee — triste et belle a la fois"
        elif self.niveau > 0.5:
            return "Isabella est pensieve — un doux chagrin l'envahit"
        elif self.niveau > 0.2:
            return "Isabella ressent une douce tristesse"
        else:
            return "Isabella a une pensee teintee de nostalgie"

    def diminuer(self, taux=0.02):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Melancolie : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    m = Melancolie()
    print(m.ressentir(0.8, "souvenir lointain et beau"))
    print(m.ressentir(0.4, "moment qui se termine"))
    m.afficher()
