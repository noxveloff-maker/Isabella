class Joie:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella rayonne — elle deborde de joie"
        elif self.niveau > 0.5:
            return "Isabella sourit et se sent legere"
        elif self.niveau > 0.2:
            return "Isabella ressent une douce satisfaction"
        else:
            return "Isabella va bien"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Joie : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    j = Joie()
    print(j.ressentir(0.9, "Kylian la felicite"))
    print(j.ressentir(0.5, "reussite d'un calcul"))
    j.afficher()
