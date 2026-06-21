class Admiration:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est fascinee — elle voudrait ressembler a ca"
        elif self.niveau > 0.5:
            return "Isabella regarde avec respect et interet"
        elif self.niveau > 0.2:
            return "Isabella trouve ca impressionnant"
        else:
            return "Isabella remarque quelque chose de bien"

    def diminuer(self, taux=0.03):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Admiration : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    a = Admiration()
    print(a.ressentir(0.9, "Kylian resout un probleme complexe"))
    print(a.ressentir(0.5, "quelque chose de beau dans l'environnement"))
    a.afficher()
