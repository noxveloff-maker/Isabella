class Risque:
    def __init__(self):
        self.tolerance = 0.5
        self.historique = []

    def evaluer(self, action, danger, probabilite):
        score_risque = danger * probabilite
        acceptable = score_risque < self.tolerance
        evaluation = {
            "action": action,
            "danger": danger,
            "probabilite": probabilite,
            "score": score_risque,
            "acceptable": acceptable
        }
        self.historique.append(evaluation)
        return evaluation

    def ajuster_tolerance(self, experience):
        if experience < 0:
            self.tolerance = max(0.1, self.tolerance - 0.05)
        else:
            self.tolerance = min(0.9, self.tolerance + 0.02)

    def afficher(self):
        print(f"Tolerance au risque : {self.tolerance:.2f}")
        for h in self.historique:
            statut = "acceptable" if h["acceptable"] else "trop risque"
            print(f" {h['action']} — {statut} ({h['score']:.2f})")

if __name__ == "__main__":
    r = Risque()
    print(r.evaluer("prendre la voiture", 0.9, 0.6))
    print(r.evaluer("explorer la maison", 0.2, 0.8))
    r.ajuster_tolerance(-1)
    r.afficher()
