class Salon:
    def __init__(self):
        self.confort = 0.8
        self.objets = ["canape", "television", "table", "lampe"]
        self.personnes_presentes = []

    def entrer(self):
        return "Isabella entre dans le salon — piece de vie principale"

    def accueillir(self, personne):
        self.personnes_presentes.append(personne)
        return f"{personne} est dans le salon avec Isabella"

    def quitter(self, personne):
        if personne in self.personnes_presentes:
            self.personnes_presentes.remove(personne)
        return f"{personne} quitte le salon"

    def afficher(self):
        print(f"Salon — confort : {self.confort:.2f}")
        print(f" Objets : {self.objets}")
        print(f" Personnes presentes : {self.personnes_presentes}")

if __name__ == "__main__":
    s = Salon()
    print(s.entrer())
    print(s.accueillir("Kylian"))
    print(s.accueillir("Isabella"))
    s.afficher()
    print(s.quitter("Kylian"))
    s.afficher()
