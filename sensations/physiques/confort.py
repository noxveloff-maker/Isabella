class Confort:

    def __init__(self):
        self.niveau = 0.5

    def ajuster(self, valeur):
        self.niveau = min(1.0, max(0.0, valeur))
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella se sent parfaitement bien"
        elif self.niveau > 0.5:
            return "Isabella est a l'aise"
        elif self.niveau > 0.2:
            return "Isabella est un peu inconfortable"
        else:
            return "Isabella est tres mal a l'aise"

    def afficher(self):
        print(f"Confort : {self.niveau:.2f}")

if __name__ == "__main__":
    c = Confort()
    print(c.ajuster(0.9))
    print(c.ajuster(0.3))
    c.afficher()
