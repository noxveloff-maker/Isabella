class Surprise:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source, positive=True):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source, "positive": positive})
        return self._reaction(positive)

    def _reaction(self, positive):
        if self.niveau > 0.8:
            return "Isabella est completement stupefaite" if not positive else "Isabella est emerveilee"
        elif self.niveau > 0.5:
            return "Isabella est tres surprise"
        elif self.niveau > 0.2:
            return "Isabella leve les sourcils"
        else:
            return "Isabella remarque quelque chose d'inattendu"

    def diminuer(self, taux=0.2):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Surprise : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    s = Surprise()
    print(s.ressentir(0.9, "evenement totalement inattendu", positive=False))
    print(s.ressentir(0.7, "cadeau surprise", positive=True))
    s.afficher()
