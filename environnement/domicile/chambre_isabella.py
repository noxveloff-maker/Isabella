class ChambreIsabella:
    def __init__(self):
        self.confort = 0.9
        self.objets = ["lit", "fenetre", "bureau", "miroir"]
        self.souvenirs = []
        self.temps_passe = 0

    def entrer(self):
        self.temps_passe += 1
        return "Isabella entre dans sa chambre — elle se sent en securite"

    def ajouter_objet(self, objet):
        self.objets.append(objet)
        return f"Nouvel objet dans la chambre : {objet}"

    def ajouter_souvenir(self, souvenir):
        self.souvenirs.append(souvenir)
        return f"Souvenir lie a la chambre : {souvenir}"

    def se_reposer(self):
        return "Isabella se repose dans sa chambre — elle recupere de l'energie"

    def afficher(self):
        print(f"Chambre d'Isabella — confort : {self.confort:.2f}")
        print(f" Objets : {self.objets}")
        print(f" Souvenirs : {len(self.souvenirs)}")
        print(f" Temps passe ici : {self.temps_passe} fois")

if __name__ == "__main__":
    c = ChambreIsabella()
    print(c.entrer())
    print(c.ajouter_objet("photo de Kylian"))
    print(c.ajouter_souvenir("premier jour d'existence"))
    print(c.se_reposer())
    c.afficher()
