class GestionnaireEmotions:
    def __init__(self):
        self.emotions_actives = {}

    def activer(self, nom_emotion, niveau):
        self.emotions_actives[nom_emotion] = niveau

    def desactiver(self, nom_emotion):
        if nom_emotion in self.emotions_actives:
            del self.emotions_actives[nom_emotion]

    def dominante(self):
        if not self.emotions_actives:
            return "neutre"
        return max(self.emotions_actives, key=self.emotions_actives.get)

    def etat_global(self):
        if not self.emotions_actives:
            return "Isabella est dans un etat neutre"
        dom = self.dominante()
        niveau = self.emotions_actives[dom]
        return f"Isabella ressent principalement : {dom} ({niveau:.2f})"

    def afficher(self):
        print(f"Emotions actives — {len(self.emotions_actives)}")
        for e, n in sorted(self.emotions_actives.items(), key=lambda x: x[1], reverse=True):
            print(f" {e} : {n:.2f}")

if __name__ == "__main__":
    g = GestionnaireEmotions()
    g.activer("joie", 0.8)
    g.activer("anxiete", 0.3)
    g.activer("tendresse", 0.6)
    g.activer("curiosite", 0.7)
    print(g.etat_global())
    g.afficher()
    g.desactiver("anxiete")
    print(f"\nApres : {g.etat_global()}")
