class Cuisine:
    def __init__(self):
        self.confort = 0.7
        self.objets = ["frigo", "four", "table", "chaises"]
        self.odeurs = []

    def entrer(self):
        return "Isabella entre dans la cuisine — elle decouvre les odeurs"

    def ajouter_odeur(self, odeur, intensite):
        self.odeurs.append({"odeur": odeur, "intensite": intensite})
        return f"Isabella sent : {odeur}"

    def afficher(self):
        print(f"Cuisine — confort : {self.confort:.2f}")
        print(f" Objets : {self.objets}")
        for o in self.odeurs:
            print(f" Odeur : {o['odeur']} ({o['intensite']:.2f})")

if __name__ == "__main__":
    c = Cuisine()
    print(c.entrer())
    print(c.ajouter_odeur("pain chaud", 0.8))
    print(c.ajouter_odeur("cafe", 0.6))
    c.afficher()
