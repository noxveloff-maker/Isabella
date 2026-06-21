class Froid:

    def __init__(self):
        self.niveau = 0.0

    def ressentir(self, temperature):
        if temperature < 15:
            self.niveau = min(1.0, (15 - temperature) / 20)
        else:
            self.niveau = 0.0
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella tremble violemment"
        elif self.niveau > 0.5:
            return "Isabella frissonne"
        elif self.niveau > 0.2:
            return "Isabella se sent un peu froide"
        else:
            return "Isabella est confortable"

    def afficher(self):
        print(f"Niveau de froid : {self.niveau:.2f}")

if __name__ == "__main__":
    f = Froid()
    print(f.ressentir(-10))
    print(f.ressentir(10))
    print(f.ressentir(20))
    f.afficher()
