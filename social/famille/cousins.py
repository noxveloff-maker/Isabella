from social.pnj_base import PNJBase

class Cousins(PNJBase):
    def __init__(self, nom):
        super().__init__(
            nom=nom,
            role="cousin",
            personnalite="varie — chaque cousin est different et imprévisible"
        )
        self.visites = 0
        self.derniere_visite = None

    def rendre_visite(self):
        self.visites += 1
        self.derniere_visite = f"visite numero {self.visites}"
        self.relation_isabella = min(1.0, self.relation_isabella + 0.05)
        return f"{self.nom} rend visite a Isabella — retrouvailles apres une absence"

    def repartir(self):
        return f"{self.nom} repart — Isabella apprend les au-revoir"

    def afficher(self):
        super().afficher()
        print(f" Visites : {self.visites}")

if __name__ == "__main__":
    c = Cousins("Thomas")
    print(c.rendre_visite())
    print(c.interagir("jouer", 0.7))
    print(c.repartir())
    c.afficher()
