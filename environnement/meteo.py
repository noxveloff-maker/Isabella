import random

class Meteo:
    def __init__(self):
        self.etat = "ensoleille"
        self.temperature = 20
        self.historique = []

    def changer(self, etat=None, temperature=None):
        etats_possibles = ["ensoleille", "nuageux", "pluvieux", "orageux", "neigeux", "ventueux"]
        if etat:
            self.etat = etat
        else:
            self.etat = random.choice(etats_possibles)
        if temperature is not None:
            self.temperature = temperature
        else:
            self.temperature = random.randint(-5, 35)
        self.historique.append({"etat": self.etat, "temperature": self.temperature})
        return self._reaction()

    def _reaction(self):
        if self.etat == "orageux":
            return f"Isabella entend le tonnerre — {self.temperature}c"
        elif self.etat == "pluvieux":
            return f"Isabella entend la pluie — {self.temperature}c"
        elif self.etat == "ensoleille":
            return f"Isabella ressent la chaleur du soleil — {self.temperature}c"
        elif self.etat == "neigeux":
            return f"Isabella decouvre la neige — {self.temperature}c"
        else:
            return f"Meteo : {self.etat} — {self.temperature}c"

    def afficher(self):
        print(f"Meteo actuelle : {self.etat} | {self.temperature}c")

if __name__ == "__main__":
    m = Meteo()
    print(m.changer("orageux", 15))
    print(m.changer("ensoleille", 25))
    print(m.changer())
    m.afficher()
