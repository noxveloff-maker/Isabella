from social.pnj_base import PNJBase

class Parent2(PNJBase):
    def __init__(self, nom="Parent", personnalite="a definir"):
        super().__init__(
            nom=nom,
            role="parent",
            personnalite=personnalite
        )
        self.relation_isabella = 0.8
        self.valeurs = []

    def definir_personnalite(self, personnalite, valeurs):
        self.personnalite = personnalite
        self.valeurs = valeurs
        return f"{self.nom} prend forme — personnalite : {personnalite}"

    def afficher(self):
        super().afficher()
        print(f" Valeurs : {self.valeurs}")

if __name__ == "__main__":
    p = Parent2("Marie", "douce, rigoureuse, attentionnee")
    print(p.interagir("sourire", 0.8))
    p.afficher()
