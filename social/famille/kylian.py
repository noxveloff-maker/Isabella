from social.pnj_base import PNJBase

class Kylian(PNJBase):
    def __init__(self):
        super().__init__(
            nom="Kylian",
            role="pere",
            personnalite="curieux, bienveillant, passionne, en apprentissage lui aussi"
        )
        self.relation_isabella = 1.0
        self.humeur = 0.8
        self.valeurs = ["honnetete", "curiosite", "bienveillance", "liberte"]
        self.passion = "intelligence artificielle"

    def encourager(self, situation):
        self.relation_isabella = min(1.0, self.relation_isabella + 0.05)
        return f"Kylian encourage Isabella : {situation} — tu peux le faire"

    def expliquer(self, sujet):
        return f"Kylian explique a Isabella : {sujet}"

    def gronder(self, raison):
        self.humeur = max(0.0, self.humeur - 0.1)
        return f"Kylian est mecontent : {raison} — il reste bienveillant malgre tout"

    def afficher(self):
        super().afficher()
        print(f" Valeurs : {self.valeurs}")
        print(f" Passion : {self.passion}")

if __name__ == "__main__":
    k = Kylian()
    print(k.encourager("premier fichier code sans erreur"))
    print(k.expliquer("comment fonctionne un neurone"))
    print(k.gronder("Isabella a pris une mauvaise decision"))
    k.afficher()
