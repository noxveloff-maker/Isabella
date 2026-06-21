class Objets:
    def __init__(self):
        self.inventaire = {}

    def ajouter(self, nom, description, interactif=True):
        self.inventaire[nom] = {
            "description": description,
            "interactif": interactif,
            "interactions": 0,
            "connu": False
        }
        return f"Objet ajoute : {nom}"

    def decouvrir(self, nom):
        if nom in self.inventaire:
            self.inventaire[nom]["connu"] = True
            return f"Isabella decouvre : {nom} — {self.inventaire[nom]['description']}"
        return f"Objet inconnu : {nom}"

    def interagir(self, nom):
        if nom not in self.inventaire:
            return f"Isabella ne connait pas : {nom}"
        if not self.inventaire[nom]["interactif"]:
            return f"Isabella ne peut pas interagir avec : {nom}"
        self.inventaire[nom]["interactions"] += 1
        return f"Isabella interagit avec : {nom} — interaction numero {self.inventaire[nom]['interactions']}"

    def connus(self):
        return [n for n, o in self.inventaire.items() if o["connu"]]

    def afficher(self):
        print(f"Objets : {len(self.inventaire)} total | {len(self.connus())} connus")
        for nom, info in self.inventaire.items():
            connu = "connu" if info["connu"] else "inconnu"
            print(f" {nom} [{connu}] — {info['description']}")

if __name__ == "__main__":
    o = Objets()
    print(o.ajouter("canape", "grand et confortable", True))
    print(o.ajouter("fenetre", "donne sur l'exterieur", True))
    print(o.ajouter("mur", "blanc et lisse", False))
    print(o.decouvrir("canape"))
    print(o.interagir("canape"))
    print(o.interagir("canape"))
    print(o.interagir("mur"))
    o.afficher()
