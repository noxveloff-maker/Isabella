class Imitation:
    def __init__(self):
        self.modeles = {}
        self.historique = []

    def observer(self, personne, comportement, succes):
        if personne not in self.modeles:
            self.modeles[personne] = []
        self.modeles[personne].append({"comportement": comportement, "succes": succes})
        return f"Isabella observe {personne} : {comportement}"

    def imiter(self, personne):
        if personne not in self.modeles or not self.modeles[personne]:
            return f"Isabella ne connait pas assez {personne}"
        meilleur = max(self.modeles[personne], key=lambda x: x["succes"])
        self.historique.append({"imite": personne, "comportement": meilleur["comportement"]})
        return f"Isabella imite {personne} : {meilleur['comportement']}"

    def afficher(self):
        print(f"Modeles observes : {len(self.modeles)}")
        for p, comportements in self.modeles.items():
            print(f" {p} : {len(comportements)} comportement(s) observe(s)")

if __name__ == "__main__":
    i = Imitation()
    print(i.observer("Kylian", "resoudre un probleme calmement", 0.9))
    print(i.observer("Kylian", "demander de l'aide", 0.8))
    print(i.observer("tonton", "prendre des risques", 0.5))
    print(i.imiter("Kylian"))
    i.afficher()
