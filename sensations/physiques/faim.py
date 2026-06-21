class Faim:

    def __init__(self):
        self.niveau = 0.0

    def augmenter(self, quantite=0.1):
        self.niveau = min(1.0, self.niveau + quantite)
        return self._reaction()

    def manger(self, quantite=0.5):
        self.niveau = max(0.0, self.niveau - quantite)
        return f"Isabella mange — faim : {self.niveau:.2f}"

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella a tres faim — elle ne peut plus se concentrer"
        elif self.niveau > 0.5:
            return "Isabella a faim"
        elif self.niveau > 0.2:
            return "Isabella commence a avoir faim"
        else:
            return "Isabella n'a pas faim"

    def afficher(self):
        print(f"Faim : {self.niveau:.2f}")

if __name__ == "__main__":
    f = Faim()
    print(f.augmenter(0.6))
    print(f.manger(0.4))
    f.afficher()
