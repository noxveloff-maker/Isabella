from social.pnj_base import PNJBase

class Tonton(PNJBase):
    def __init__(self):
        super().__init__(
            nom="Tonton",
            role="tonton",
            personnalite="decontracte, drole, parfois irresponsable, celui qui dit oui quand les parents disent non"
        )
        self.blagues = 0

    def faire_rire(self):
        self.blagues += 1
        self.relation_isabella = min(1.0, self.relation_isabella + 0.05)
        return "Tonton fait rire Isabella — la vie peut etre legere"

    def proposer_aventure(self, aventure):
        return f"Tonton propose a Isabella : {aventure} — les parents ne sont pas au courant"

    def afficher(self):
        super().afficher()
        print(f" Blagues faites : {self.blagues}")

if __name__ == "__main__":
    t = Tonton()
    print(t.faire_rire())
    print(t.proposer_aventure("sortir sans prevenir"))
    t.afficher()
