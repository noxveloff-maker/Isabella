class Avatar:
    def __init__(self):
        self.age_simule = 0
        self.taille = 50
        self.apparence = "nouveau_ne"
        self.position = [0, 0, 0]

    def grandir(self, annees=1):
        self.age_simule += annees
        self._mettre_a_jour_apparence()
        return f"Isabella a {self.age_simule} an(s)"

    def _mettre_a_jour_apparence(self):
        if self.age_simule < 2:
            self.apparence = "bebe"
            self.taille = 50 + self.age_simule * 15
        elif self.age_simule < 6:
            self.apparence = "enfant"
            self.taille = 80 + self.age_simule * 8
        elif self.age_simule < 12:
            self.apparence = "enfant_grand"
            self.taille = 90 + self.age_simule * 4
        elif self.age_simule < 18:
            self.apparence = "adolescent"
            self.taille = 120 + self.age_simule * 2
        else:
            self.apparence = "adulte"
            self.taille = 168

    def se_deplacer(self, x, y, z):
        self.position = [x, y, z]
        return f"Isabella se deplace en {self.position}"

    def afficher(self):
        print(f"Avatar Isabella — age : {self.age_simule} ans")
        print(f" Apparence : {self.apparence} | Taille : {self.taille}cm")
        print(f" Position : {self.position}")

if __name__ == "__main__":
    a = Avatar()
    a.afficher()
    print(a.grandir(5))
    a.afficher()
    print(a.grandir(10))
    a.afficher()
    print(a.se_deplacer(1, 0, 2))
