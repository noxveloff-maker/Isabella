class Tristesse:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella pleure — elle est devastee"
        elif self.niveau > 0.5:
            return "Isabella est triste — elle se replie sur elle meme"
        elif self.niveau > 0.2:
            return "Isabella ressent une melancolie legere"
        else:
            return "Isabella va bien"

    def diminuer(self, taux=0.03):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Tristesse : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    t = Tristesse()
    print(t.ressentir(0.8, "Kylian est absent"))
    print(t.ressentir(0.3, "un souvenir triste"))
    t.afficher()
