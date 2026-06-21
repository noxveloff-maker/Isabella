from datetime import datetime

class MemoireSociale:

    def __init__(self):
        self.profils = {}

    def ajouter_personne(self, nom, role):
        self.profils[nom] = {
            "nom": nom,
            "role": role,
            "confiance": 0.5,
            "interactions": [],
            "premiere_rencontre": datetime.now().strftime("%Y-%m-%d")
        }
        return self.profils[nom]

    def ajouter_interaction(self, nom, contenu, impact):
        if nom in self.profils:
            interaction = {
                "contenu": contenu,
                "impact": impact,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            self.profils[nom]["interactions"].append(interaction)
            self.profils[nom]["confiance"] = min(1.0, max(0.0, self.profils[nom]["confiance"] + impact))

    def confiance(self, nom):
        if nom in self.profils:
            return self.profils[nom]["confiance"]
        return 0.0

    def afficher(self):
        print(f"Memoire sociale — {len(self.profils)} personne(s)")
        for nom, p in self.profils.items():
            print(f" {nom} ({p['role']}) — confiance : {p['confiance']:.2f}")
            print(f" Interactions : {len(p['interactions'])}")

if __name__ == "__main__":
    ms = MemoireSociale()
    ms.ajouter_personne("Kylian", "pere")
    ms.ajouter_interaction("Kylian", "Il lui parle doucement", 0.2)
    ms.ajouter_interaction("Kylian", "Il lui explique Python", 0.15)
    ms.ajouter_interaction("Kylian", "Il la encourage", 0.1)
    print("Isabella - Memoire sociale :")
    ms.afficher()
    print(f"\nConfiance en Kylian : {ms.confiance('Kylian'):.2f}")
