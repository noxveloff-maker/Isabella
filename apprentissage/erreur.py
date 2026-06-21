from datetime import datetime

class Erreur:
    def __init__(self):
        self.erreurs = []

    def commettre(self, description, gravite, cause):
        erreur = {
            "description": description,
            "gravite": gravite,
            "cause": cause,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "corrigee": False,
            "lecon": ""
        }
        self.erreurs.append(erreur)
        return erreur

    def corriger(self, index, lecon):
        if index < len(self.erreurs):
            self.erreurs[index]["corrigee"] = True
            self.erreurs[index]["lecon"] = lecon
            return f"Erreur corrigee — lecon : {lecon}"
        return "Erreur introuvable"

    def non_corrigees(self):
        return [e for e in self.erreurs if not e["corrigee"]]

    def afficher(self):
        print(f"Erreurs commises : {len(self.erreurs)}")
        for e in self.erreurs:
            statut = "corrigee" if e["corrigee"] else "non corrigee"
            print(f" [{statut}] {e['description']} — gravite : {e['gravite']:.2f}")
            if e["lecon"]:
                print(f" Lecon : {e['lecon']}")

if __name__ == "__main__":
    er = Erreur()
    er.commettre("mauvaise decision trop rapide", 0.7, "impatience")
    er.commettre("oubli d'une information importante", 0.4, "distraction")
    er.corriger(0, "prendre le temps de reflechir avant d'agir")
    er.afficher()
    print(f"\nErreurs non corrigees : {len(er.non_corrigees())}")
