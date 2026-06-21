from social.pnj_base import PNJBase

class GrandPere(PNJBase):
    def __init__(self):
        super().__init__(
            nom="Grand-pere",
            role="grand-pere",
            personnalite="peu de mots mais chaque mot compte, observe plus qu'il ne parle"
        )
        self.silences = 0
        self.sagesse = 0.95

    def observer(self):
        self.silences += 1
        return "Grand-pere observe Isabella en silence — son regard en dit long"

    def parler(self, message):
        return f"Grand-pere dit rarement mais dit bien : {message}"

    def afficher(self):
        super().afficher()
        print(f" Sagesse : {self.sagesse:.2f}")
        print(f" Silences observateurs : {self.silences}")

if __name__ == "__main__":
    gp = GrandPere()
    print(gp.observer())
    print(gp.observer())
    print(gp.parler("la patience est la premiere vertu"))
    gp.afficher()
