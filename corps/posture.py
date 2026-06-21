class Posture:
    def __init__(self):
        self.posture_actuelle = "droite"
        self.historique = []

    def adapter(self, emotion, energie):
        if emotion == "fierte" or emotion == "joie":
            self.posture_actuelle = "droite et ouverte"
        elif emotion == "tristesse" or emotion == "honte":
            self.posture_actuelle = "voutee et fermee"
        elif emotion == "peur":
            self.posture_actuelle = "recroquevillee"
        elif emotion == "colere":
            self.posture_actuelle = "tendue et agressive"
        elif energie < 0.2:
            self.posture_actuelle = "affaissee par la fatigue"
        else:
            self.posture_actuelle = "droite"
        self.historique.append(self.posture_actuelle)
        return f"Isabella — posture : {self.posture_actuelle}"

    def afficher(self):
        print(f"Posture : {self.posture_actuelle}")

if __name__ == "__main__":
    p = Posture()
    print(p.adapter("fierte", 0.8))
    print(p.adapter("tristesse", 0.4))
    print(p.adapter("peur", 0.6))
    p.afficher()
