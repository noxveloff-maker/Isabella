from social.pnj_base import PNJBase

class GrandMere(PNJBase):
    def __init__(self):
        super().__init__(
            nom="Grand-mere",
            role="grand-mere",
            personnalite="douce, pleine d'histoires, parfois en desaccord avec les parents"
        )
        self.histoires = []
        self.sagesse = 0.9

    def raconter_histoire(self, histoire):
        self.histoires.append(histoire)
        return f"Grand-mere raconte a Isabella : {histoire}"

    def donner_conseil(self, situation):
        return f"Grand-mere conseille Isabella sur : {situation} — avec toute sa sagesse"

    def afficher(self):
        super().afficher()
        print(f" Sagesse : {self.sagesse:.2f}")
        print(f" Histoires racontees : {len(self.histoires)}")

if __name__ == "__main__":
    gm = GrandMere()
    print(gm.raconter_histoire("quand j'etais jeune tout etait different"))
    print(gm.donner_conseil("premiere grande peur"))
    gm.afficher()
