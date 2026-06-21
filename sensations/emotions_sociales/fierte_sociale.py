class FierteSociale:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est fiere de ce que son groupe accomplit"
        elif self.niveau > 0.5:
            return "Isabella ressent une fierte collective"
        elif self.niveau > 0.2:
            return "Isabella est contente de son groupe"
        else:
            return "Isabella remarque quelque chose de bien dans son groupe"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Fierte sociale : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    f = FierteSociale()
    print(f.ressentir(0.9, "le projet Isabella avance bien"))
    print(f.ressentir(0.5, "bonne collaboration avec Kylian"))
    f.afficher()
