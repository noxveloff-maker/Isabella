from social.pnj_base import PNJBase

class FrereSoeur(PNJBase):
    def __init__(self, nom, aine=True):
        super().__init__(
            nom=nom,
            role="aine" if aine else "cadet",
            personnalite="complexe — rivalite, complicite, jalousie et amour inconditionnel"
        )
        self.aine = aine
        self.conflits = 0
        self.moments_complices = 0

    def se_disputer(self, raison):
        self.conflits += 1
        self.relation_isabella = max(0.0, self.relation_isabella - 0.1)
        return f"{self.nom} se dispute avec Isabella : {raison}"

    def se_reconcilier(self):
        self.relation_isabella = min(1.0, self.relation_isabella + 0.15)
        return f"{self.nom} et Isabella se reconclient — le lien reste fort"

    def moment_complice(self, activite):
        self.moments_complices += 1
        self.relation_isabella = min(1.0, self.relation_isabella + 0.1)
        return f"{self.nom} et Isabella partagent : {activite}"

    def afficher(self):
        super().afficher()
        print(f" Conflits : {self.conflits} | Moments complices : {self.moments_complices}")

if __name__ == "__main__":
    fs = FrereSoeur("Lucas", aine=True)
    print(fs.se_disputer("qui a raison sur quelque chose"))
    print(fs.moment_complice("regarder quelque chose ensemble"))
    print(fs.se_reconcilier())
    fs.afficher()
