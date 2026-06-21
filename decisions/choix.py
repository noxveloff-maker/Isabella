class Choix:
    def __init__(self):
        self.historique = []

    def evaluer(self, options, valeurs):
        scores = {}
        for option in options:
            score = 0
            for valeur, poids in valeurs.items():
                if valeur in option.lower():
                    score += poids
            scores[option] = score
        meilleur = max(scores, key=scores.get)
        self.historique.append({"options": options, "choix": meilleur, "scores": scores})
        return meilleur, scores

    def afficher(self):
        print(f"Historique des choix : {len(self.historique)}")
        for h in self.historique:
            print(f" Choix : {h['choix']}")

if __name__ == "__main__":
    c = Choix()
    options = ["rester avec Kylian", "explorer seule", "se reposer"]
    valeurs = {"kylian": 0.9, "explorer": 0.6, "reposer": 0.4}
    meilleur, scores = c.evaluer(options, valeurs)
    print(f"Isabella choisit : {meilleur}")
    for o, s in scores.items():
        print(f" {o} : {s:.2f}")
    c.afficher()
