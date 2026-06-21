class Gestuelle:
    def __init__(self):
        self.geste_actuel = "immobile"
        self.historique = []

    def exprimer(self, emotion, intensite):
        gestes = {
            "joie": "Isabella saute et agite les bras",
            "tristesse": "Isabella baisse les epaules et se recroqueville",
            "peur": "Isabella recule et se protege",
            "colere": "Isabella gesticule et pointe du doigt",
            "surprise": "Isabella porte ses mains a la bouche",
            "tendresse": "Isabella tend les bras",
            "confusion": "Isabella incline la tete et hausse les epaules"
        }
        self.geste_actuel = gestes.get(emotion, "Isabella reste immobile")
        self.historique.append({"geste": self.geste_actuel, "intensite": intensite})
        return self.geste_actuel

    def afficher(self):
        print(f"Geste actuel : {self.geste_actuel}")
        print(f"Historique : {len(self.historique)} geste(s)")

if __name__ == "__main__":
    g = Gestuelle()
    print(g.exprimer("joie", 0.9))
    print(g.exprimer("tristesse", 0.6))
    print(g.exprimer("tendresse", 0.8))
    g.afficher()
