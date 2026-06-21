class AgeVisuel:
    def __init__(self):
        self.age = 0
        self.caracteristiques = {}
        self._mettre_a_jour()

    def vieillir(self, annees=1):
        self.age += annees
        self._mettre_a_jour()
        return f"Isabella vieillit — {self.age} an(s)"

    def _mettre_a_jour(self):
        if self.age < 2:
            self.caracteristiques = {"visage": "rond et doux", "yeux": "grands", "cheveux": "fins"}
        elif self.age < 6:
            self.caracteristiques = {"visage": "joufflu", "yeux": "curieux", "cheveux": "courts"}
        elif self.age < 12:
            self.caracteristiques = {"visage": "expressif", "yeux": "vifs", "cheveux": "mi-longs"}
        elif self.age < 18:
            self.caracteristiques = {"visage": "qui s'affine", "yeux": "profonds", "cheveux": "longs"}
        else:
            self.caracteristiques = {"visage": "mature", "yeux": "sages", "cheveux": "longs"}

    def afficher(self):
        print(f"Age visuel : {self.age} an(s)")
        for k, v in self.caracteristiques.items():
            print(f" {k} : {v}")

if __name__ == "__main__":
    av = AgeVisuel()
    av.afficher()
    print(av.vieillir(5))
    av.afficher()
    print(av.vieillir(10))
    av.afficher()
