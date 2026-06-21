class Visualisation:
    def __init__(self):
        self.largeur = 40

    def barre(self, nom, valeur, maximum=1.0):
        proportion = valeur / maximum
        nb_barres = int(proportion * self.largeur)
        barre = "█" * nb_barres + "░" * (self.largeur - nb_barres)
        return f"{nom:<20} [{barre}] {valeur:.2f}"

    def etat_emotions(self, emotions):
        print("=== Etat emotionnel d'Isabella ===")
        for nom, valeur in sorted(emotions.items(), key=lambda x: x[1], reverse=True):
            print(self.barre(nom, valeur))

    def etat_memoire(self, memoire):
        print("=== Etat de la memoire ===")
        for nom, valeur in memoire.items():
            print(self.barre(nom, valeur))

    def afficher(self):
        print(f"Visualisation active — largeur : {self.largeur}")

if __name__ == "__main__":
    v = Visualisation()
    emotions = {
        "joie": 0.8,
        "curiosite": 0.7,
        "anxiete": 0.2,
        "tendresse": 0.6,
        "fierte": 0.5
    }
    v.etat_emotions(emotions)
    print()
    memoire = {
        "court terme": 0.6,
        "long terme": 0.4,
        "emotionnelle": 0.8
    }
    v.etat_memoire(memoire)
