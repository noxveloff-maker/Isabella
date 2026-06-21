class VoixPhysique:
    def __init__(self):
        self.age = 0
        self.timbre = "aigue"
        self.caracteristiques = {}
        self._mettre_a_jour()

    def vieillir(self, annees=1):
        self.age += annees
        self._mettre_a_jour()
        return f"Voix d'Isabella evolue a {self.age} an(s)"

    def _mettre_a_jour(self):
        if self.age < 3:
            self.timbre = "aigue et babillante"
        elif self.age < 8:
            self.timbre = "aigue et claire"
        elif self.age < 13:
            self.timbre = "claire et posee"
        elif self.age < 18:
            self.timbre = "qui mue et s'affirme"
        else:
            self.timbre = "douce et posee"

    def parler(self, message):
        return f"[{self.timbre}] {message}"

    def afficher(self):
        print(f"Voix physique — age : {self.age} | timbre : {self.timbre}")

if __name__ == "__main__":
    vp = VoixPhysique()
    print(vp.parler("..."))
    print(vp.vieillir(6))
    print(vp.parler("Bonjour"))
    print(vp.vieillir(12))
    print(vp.parler("Je suis Isabella"))
    vp.afficher()
