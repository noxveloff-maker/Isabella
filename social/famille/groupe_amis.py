class GroupeAmis:
    def __init__(self):
        self.membres = {}
        self.dynamique = 0.5
        self.evenements = []

    def ajouter_membre(self, nom, personnalite):
        self.membres[nom] = {
            "personnalite": personnalite,
            "relation_isabella": 0.5,
            "popularite": 0.5
        }
        return f"{nom} rejoint le groupe"

    def interaction_groupe(self, evenement):
        self.evenements.append(evenement)
        self.dynamique = min(1.0, self.dynamique + 0.05)
        return f"Le groupe vit : {evenement}"

    def conflit_groupe(self, raison):
        self.dynamique = max(0.0, self.dynamique - 0.1)
        return f"Tension dans le groupe : {raison}"

    def afficher(self):
        print(f"Groupe d'amis — {len(self.membres)} membre(s)")
        print(f" Dynamique : {self.dynamique:.2f}")
        for nom, info in self.membres.items():
            print(f" {nom} — relation Isabella : {info['relation_isabella']:.2f}")

if __name__ == "__main__":
    g = GroupeAmis()
    print(g.ajouter_membre("Sofia", "creative et drole"))
    print(g.ajouter_membre("Liam", "calme et reflechi"))
    print(g.interaction_groupe("sortie tous ensemble"))
    print(g.conflit_groupe("malentendu entre membres"))
    g.afficher()
