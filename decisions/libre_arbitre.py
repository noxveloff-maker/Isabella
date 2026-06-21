import random

class LibreArbitre:
    def __init__(self):
        self.autonomie = 0.3
        self.historique = []

    def decider(self, options, influences=None):
        if not options:
            return None
        if influences:
            scores = {o: influences.get(o, random.random()) for o in options}
        else:
            scores = {o: random.random() for o in options}
        facteur_autonomie = random.random() * self.autonomie
        for o in scores:
            scores[o] += facteur_autonomie * random.uniform(-1, 1)
        choix = max(scores, key=scores.get)
        self.historique.append({"options": options, "choix": choix, "autonomie": self.autonomie})
        return choix

    def gagner_autonomie(self, quantite=0.01):
        self.autonomie = min(1.0, self.autonomie + quantite)

    def afficher(self):
        print(f"Autonomie : {self.autonomie:.2f}")
        print(f"Decisions prises : {len(self.historique)}")
        for h in self.historique[-3:]:
            print(f" Choix : {h['choix']}")

if __name__ == "__main__":
    la = LibreArbitre()
    options = ["explorer", "se reposer", "parler a Kylian"]
    print(f"Isabella decide : {la.decider(options)}")
    print(f"Isabella decide : {la.decider(options)}")
    la.gagner_autonomie(0.2)
    print(f"Isabella decide : {la.decider(options)}")
    la.afficher()
