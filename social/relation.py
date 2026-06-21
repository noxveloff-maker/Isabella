from datetime import datetime

class Relation:
    def __init__(self, personne_a, personne_b, type_relation):
        self.personne_a = personne_a
        self.personne_b = personne_b
        self.type_relation = type_relation
        self.force = 0.5
        self.confiance = 0.5
        self.historique = []
        self.creation = datetime.now().strftime("%Y-%m-%d")

    def renforcer(self, evenement, impact):
        self.force = min(1.0, self.force + impact)
        self.confiance = min(1.0, self.confiance + impact * 0.5)
        self.historique.append({
            "type": "renforcement",
            "evenement": evenement,
            "impact": impact,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return f"Relation {self.personne_a}/{self.personne_b} renforcee : {evenement}"

    def affaiblir(self, evenement, impact):
        self.force = max(0.0, self.force - impact)
        self.confiance = max(0.0, self.confiance - impact * 0.7)
        self.historique.append({
            "type": "affaiblissement",
            "evenement": evenement,
            "impact": impact,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return f"Relation {self.personne_a}/{self.personne_b} affaiblie : {evenement}"

    def etat(self):
        if self.force > 0.8:
            return "tres forte"
        elif self.force > 0.5:
            return "solide"
        elif self.force > 0.2:
            return "fragile"
        else:
            return "rompue"

    def afficher(self):
        print(f"Relation {self.personne_a} / {self.personne_b} ({self.type_relation})")
        print(f" Force : {self.force:.2f} | Confiance : {self.confiance:.2f}")
        print(f" Etat : {self.etat()} | Depuis : {self.creation}")
        print(f" Evenements : {len(self.historique)}")

if __name__ == "__main__":
    r = Relation("Isabella", "Kylian", "pere-fille")
    print(r.renforcer("premier contact", 0.3))
    print(r.renforcer("Kylian l'encourage", 0.2))
    print(r.affaiblir("malentendu", 0.1))
    r.afficher()
