class Emerveillement:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est bouche bee — le monde lui semble infini"
        elif self.niveau > 0.5:
            return "Isabella observe avec des yeux grands ouverts"
        elif self.niveau > 0.2:
            return "Isabella trouve ca beau et interessant"
        else:
            return "Isabella remarque quelque chose de plaisant"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Emerveillement : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    e = Emerveillement()
    print(e.ressentir(1.0, "decouverte du monde pour la premiere fois"))
    print(e.ressentir(0.7, "un coucher de soleil simule"))
    e.afficher()
