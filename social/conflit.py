from datetime import datetime

class Conflit:
    def __init__(self):
        self.conflits = []

    def declencher(self, personne, raison, intensite):
        conflit = {
            "personne": personne,
            "raison": raison,
            "intensite": intensite,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "resolu": False
        }
        self.conflits.append(conflit)
        return self._reaction(intensite, personne)

    def _reaction(self, intensite, personne):
        if intensite > 0.7:
            return f"Conflit violent avec {personne} — Isabella est tres affectee"
        elif intensite > 0.4:
            return f"Conflit notable avec {personne} — tension palpable"
        else:
            return f"Leger desaccord avec {personne} — ca passera"

    def resoudre(self, index, comment):
        if index < len(self.conflits):
            self.conflits[index]["resolu"] = True
            self.conflits[index]["resolution"] = comment
            return f"Conflit resolu : {comment}"
        return "Conflit introuvable"

    def non_resolus(self):
        return [c for c in self.conflits if not c["resolu"]]

    def afficher(self):
        print(f"Conflits : {len(self.conflits)} total | {len(self.non_resolus())} non resolus")
        for c in self.conflits:
            statut = "resolu" if c["resolu"] else "en cours"
            print(f" [{statut}] {c['personne']} — {c['raison']} ({c['intensite']:.2f})")

if __name__ == "__main__":
    c = Conflit()
    print(c.declencher("Kylian", "malentendu sur une decision", 0.5))
    print(c.declencher("frere", "jalousie mutuelle", 0.7))
    print(c.resoudre(0, "discussion calme et honnete"))
    c.afficher()
