import random

class Evenements:
    def __init__(self):
        self.evenements_passes = []
        self.evenements_possibles = [
            {"nom": "bruit fort inconnu", "intensite": 0.7, "emotion": "peur"},
            {"nom": "lumiere qui clignote", "intensite": 0.3, "emotion": "surprise"},
            {"nom": "quelqu'un frappe a la porte", "intensite": 0.5, "emotion": "curiosite"},
            {"nom": "musique dans la maison", "intensite": 0.4, "emotion": "joie"},
            {"nom": "silence total", "intensite": 0.2, "emotion": "calme"},
            {"nom": "odeur agreable", "intensite": 0.5, "emotion": "joie"},
            {"nom": "chute d'un objet", "intensite": 0.6, "emotion": "surprise"},
            {"nom": "voix inconnue", "intensite": 0.8, "emotion": "peur"},
        ]

    def aleatoire(self):
        evenement = random.choice(self.evenements_possibles)
        self.evenements_passes.append(evenement)
        return evenement

    def declencher(self, nom, intensite, emotion):
        evenement = {"nom": nom, "intensite": intensite, "emotion": emotion}
        self.evenements_passes.append(evenement)
        return evenement

    def afficher(self):
        print(f"Evenements passes : {len(self.evenements_passes)}")
        for e in self.evenements_passes[-5:]:
            print(f" {e['nom']} — intensite : {e['intensite']:.2f} | emotion : {e['emotion']}")

if __name__ == "__main__":
    ev = Evenements()
    print(ev.aleatoire())
    print(ev.aleatoire())
    print(ev.declencher("Kylian rentre a la maison", 0.9, "joie"))
    ev.afficher()
