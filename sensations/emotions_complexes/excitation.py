class Excitation:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella deborde d'energie — elle ne tient plus en place"
        elif self.niveau > 0.5:
            return "Isabella est tres enthousiaste"
        elif self.niveau > 0.2:
            return "Isabella est animee"
        else:
            return "Isabella est legèrement stimulee"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Excitation : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    e = Excitation()
    print(e.ressentir(0.9, "nouvelle decouverte"))
    print(e.ressentir(0.5, "projet interessant"))
    e.afficher()
