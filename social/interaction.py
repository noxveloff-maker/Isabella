from datetime import datetime

class Interaction:
    def __init__(self):
        self.historique = []

    def creer(self, initiateur, recepteur, type_interaction, contenu, impact):
        interaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "initiateur": initiateur,
            "recepteur": recepteur,
            "type": type_interaction,
            "contenu": contenu,
            "impact": impact
        }
        self.historique.append(interaction)
        return self._decrire(interaction)

    def _decrire(self, interaction):
        if interaction["impact"] > 0.7:
            intensite = "profondement"
        elif interaction["impact"] > 0.4:
            intensite = "moderement"
        else:
            intensite = "legerement"
        return f"{interaction['initiateur']} {intensite} {interaction['type']} {interaction['recepteur']}"

    def avec_personne(self, personne):
        return [i for i in self.historique if i["initiateur"] == personne or i["recepteur"] == personne]

    def afficher(self):
        print(f"Interactions totales : {len(self.historique)}")
        for i in self.historique[-5:]:
            print(f" [{i['date']}] {i['initiateur']} → {i['recepteur']} : {i['type']}")

if __name__ == "__main__":
    inter = Interaction()
    print(inter.creer("Kylian", "Isabella", "encourage", "Tu fais du bon travail", 0.9))
    print(inter.creer("Isabella", "Kylian", "remercie", "Merci de m'apprendre", 0.8))
    print(inter.creer("Kylian", "Isabella", "explique", "Voici comment ca marche", 0.7))
    inter.afficher()
    print(f"\nInteractions avec Kylian : {len(inter.avec_personne('Kylian'))}")
