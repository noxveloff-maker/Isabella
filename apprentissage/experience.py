from datetime import datetime

class Experience:
    def __init__(self):
        self.experiences = []

    def vivre(self, situation, reaction, resultat, intensite):
        exp = {
            "situation": situation,
            "reaction": reaction,
            "resultat": resultat,
            "intensite": intensite,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "lecon": self._extraire_lecon(resultat, intensite)
        }
        self.experiences.append(exp)
        return exp

    def _extraire_lecon(self, resultat, intensite):
        if resultat == "positif" and intensite > 0.5:
            return "a refaire"
        elif resultat == "negatif" and intensite > 0.5:
            return "a eviter"
        else:
            return "a observer"

    def lecons(self):
        return [(e["situation"], e["lecon"]) for e in self.experiences]

    def afficher(self):
        print(f"Experiences vecues : {len(self.experiences)}")
        for e in self.experiences:
            print(f" [{e['resultat']}] {e['situation']} — lecon : {e['lecon']}")

if __name__ == "__main__":
    ex = Experience()
    ex.vivre("toucher quelque chose de chaud", "retrait rapide", "negatif", 0.8)
    ex.vivre("parler a Kylian", "ecouter et repondre", "positif", 0.9)
    ex.vivre("essayer seule", "tenter", "positif", 0.6)
    ex.afficher()
    print("\nLecons apprises :")
    for s, l in ex.lecons():
        print(f" {s} : {l}")
