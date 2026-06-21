class Visage:
    def __init__(self):
        self.expression = "neutre"
        self.intensite = 0.0
        self.historique = []

    def exprimer(self, emotion, intensite):
        self.expression = emotion
        self.intensite = min(1.0, intensite)
        self.historique.append({"expression": emotion, "intensite": intensite})
        return self._decrire()

    def _decrire(self):
        descriptions = {
            "joie": f"Isabella sourit — intensite {self.intensite:.2f}",
            "tristesse": f"Isabella a les yeux baissés — intensite {self.intensite:.2f}",
            "peur": f"Isabella a les yeux ecarquilles — intensite {self.intensite:.2f}",
            "colere": f"Isabella fronce les sourcils — intensite {self.intensite:.2f}",
            "surprise": f"Isabella ouvre grand les yeux — intensite {self.intensite:.2f}",
            "degout": f"Isabella plisse le nez — intensite {self.intensite:.2f}",
            "neutre": "Isabella a une expression calme"
        }
        return descriptions.get(self.expression, f"Isabella exprime {self.expression}")

    def afficher(self):
        print(f"Expression : {self.expression} ({self.intensite:.2f})")

if __name__ == "__main__":
    v = Visage()
    print(v.exprimer("joie", 0.9))
    print(v.exprimer("tristesse", 0.6))
    print(v.exprimer("surprise", 0.8))
    v.afficher()
