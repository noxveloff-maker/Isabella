import random

class Inconnus:
    def __init__(self):
        self.rencontres = []
        self.personnalites_possibles = [
            "bienveillant et souriant",
            "indifferent et presse",
            "curieux et bavard",
            "froid et distant",
            "imprévisible et etrange",
            "chaleureux et ouvert"
        ]

    def rencontrer(self, contexte):
        personnalite = random.choice(self.personnalites_possibles)
        inconnu = {
            "contexte": contexte,
            "personnalite": personnalite,
            "impact": random.uniform(-0.3, 0.5)
        }
        self.rencontres.append(inconnu)
        return self._reaction(inconnu)

    def _reaction(self, inconnu):
        if inconnu["impact"] > 0.3:
            return f"Isabella rencontre quelqu'un de {inconnu['personnalite']} — impact positif"
        elif inconnu["impact"] < 0:
            return f"Isabella rencontre quelqu'un de {inconnu['personnalite']} — impact negatif"
        else:
            return f"Isabella croise quelqu'un de {inconnu['personnalite']} — sans grand impact"

    def afficher(self):
        print(f"Inconnus rencontres : {len(self.rencontres)}")
        for r in self.rencontres[-3:]:
            print(f" [{r['contexte']}] {r['personnalite']} — impact : {r['impact']:.2f}")

if __name__ == "__main__":
    i = Inconnus()
    print(i.rencontrer("dans la rue"))
    print(i.rencontrer("dans un magasin"))
    print(i.rencontrer("chez un voisin"))
    i.afficher()
