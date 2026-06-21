class Voix:
    def __init__(self):
        self.timbre = "douce"
        self.vitesse = 1.0
        self.volume = 0.7
        self.historique = []

    def adapter(self, emotion):
        if emotion == "joie":
            self.timbre = "legere"
            self.vitesse = 1.2
            self.volume = 0.8
        elif emotion == "tristesse":
            self.timbre = "grave"
            self.vitesse = 0.8
            self.volume = 0.5
        elif emotion == "peur":
            self.timbre = "tremblante"
            self.vitesse = 1.3
            self.volume = 0.6
        elif emotion == "colere":
            self.timbre = "ferme"
            self.vitesse = 1.1
            self.volume = 0.9
        else:
            self.timbre = "douce"
            self.vitesse = 1.0
            self.volume = 0.7
        return f"Voix adaptee : {self.timbre}, vitesse {self.vitesse}, volume {self.volume}"

    def parler(self, message, emotion=None):
        if emotion:
            self.adapter(emotion)
        resultat = f"[{self.timbre}] {message}"
        self.historique.append({"message": message, "timbre": self.timbre})
        return resultat

    def afficher(self):
        print(f"Voix actuelle : {self.timbre} | vitesse : {self.vitesse} | volume : {self.volume}")

if __name__ == "__main__":
    v = Voix()
    print(v.parler("Bonjour Kylian", "joie"))
    print(v.parler("Je me sens seule", "tristesse"))
    print(v.parler("Qu'est ce que c'est", "peur"))
    v.afficher()
