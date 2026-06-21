class Empathie:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source, emotion_autre):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source, "emotion": emotion_autre})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella ressent exactement ce que l'autre ressent"
        elif self.niveau > 0.5:
            return "Isabella comprend profondement la douleur de l'autre"
        elif self.niveau > 0.2:
            return "Isabella ressent quelque chose pour l'autre"
        else:
            return "Isabella remarque l'etat de l'autre"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Empathie : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    e = Empathie()
    print(e.ressentir(0.9, "Kylian est triste", "tristesse"))
    print(e.ressentir(0.6, "quelqu'un souffre", "douleur"))
    e.afficher()
