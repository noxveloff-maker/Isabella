class Chaleur:

    def __init__(self):
        self.temperature = 20.0
        self.confort_min = 15.0
        self.confort_max = 28.0

    def ressentir(self, temperature):
        self.temperature = temperature
        return self._reaction()

    def _reaction(self):
        if self.temperature > 40:
            return "Isabella souffre de la chaleur extreme"
        elif self.temperature > 28:
            return "Isabella se sent trop chaude"
        elif self.temperature >= self.confort_min:
            return "Isabella est confortable"
        elif self.temperature > 5:
            return "Isabella se sent froide"
        else:
            return "Isabella souffre du froid extreme"

    def afficher(self):
        print(f"Temperature ressentie : {self.temperature}c")

if __name__ == "__main__":
    c = Chaleur()
    print(c.ressentir(35))
    print(c.ressentir(22))
    print(c.ressentir(-5))
    c.afficher()
