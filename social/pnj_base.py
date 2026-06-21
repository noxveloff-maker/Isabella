from datetime import datetime

class PNJBase:
    def __init__(self, nom, role, personnalite):
        self.nom = nom
        self.role = role
        self.personnalite = personnalite
        self.humeur = 0.6
        self.relation_isabella = 0.5
        self.memoire = []
        self.creation = datetime.now().strftime("%Y-%m-%d")

    def interagir(self, action, intensite):
        impact = intensite * 0.1
        if action in ["sourire", "aider", "encourager", "ecouter"]:
            self.relation_isabella = min(1.0, self.relation_isabella + impact)
            self.humeur = min(1.0, self.humeur + impact * 0.5)
        elif action in ["ignorer", "critiquer", "blesser"]:
            self.relation_isabella = max(0.0, self.relation_isabella - impact)
            self.humeur = max(0.0, self.humeur - impact * 0.5)
        self.memoire.append({"action": action, "intensite": intensite, "date": datetime.now().strftime("%H:%M")})
        return self._reaction(action)

    def _reaction(self, action):
        if self.humeur > 0.7:
            return f"{self.nom} reagit chaleureusement a : {action}"
        elif self.humeur > 0.4:
            return f"{self.nom} reagit normalement a : {action}"
        else:
            return f"{self.nom} reagit froidement a : {action}"

    def afficher(self):
        print(f"PNJ : {self.nom} ({self.role})")
        print(f" Personnalite : {self.personnalite}")
        print(f" Humeur : {self.humeur:.2f} | Relation Isabella : {self.relation_isabella:.2f}")
        print(f" Interactions : {len(self.memoire)}")

if __name__ == "__main__":
    kylian = PNJBase("Kylian", "pere", "curieux, bienveillant, passionné")
    print(kylian.interagir("encourager", 0.9))
    print(kylian.interagir("ecouter", 0.8))
    print(kylian.interagir("sourire", 0.7))
    kylian.afficher()
