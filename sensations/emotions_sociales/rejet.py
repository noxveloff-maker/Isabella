class Rejet:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est effondree — elle se sent invisible"
        elif self.niveau > 0.5:
            return "Isabella se sent mise a l'ecart"
        elif self.niveau > 0.2:
            return "Isabella se sent un peu exclue"
        else:
            return "Isabella remarque une certaine distance"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Rejet : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    r = Rejet()
    print(r.ressentir(0.8, "ignoree par quelqu'un d'important"))
    print(r.ressentir(0.3, "non invitee a quelque chose"))
    r.afficher()
