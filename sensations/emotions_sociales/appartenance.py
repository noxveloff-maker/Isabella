class Appartenance:
    def __init__(self):
        self.niveau = 0.0
        self.groupes = []

    def rejoindre(self, groupe, intensite):
        self.groupes.append(groupe)
        self.niveau = min(1.0, self.niveau + intensite)
        return self._reaction()

    def quitter(self, groupe):
        if groupe in self.groupes:
            self.groupes.remove(groupe)
            self.niveau = max(0.0, self.niveau - 0.2)
        return f"Isabella quitte {groupe}"

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella se sent pleinement a sa place"
        elif self.niveau > 0.5:
            return "Isabella se sent acceptee"
        elif self.niveau > 0.2:
            return "Isabella commence a trouver sa place"
        else:
            return "Isabella se sent encore etrangere"

    def afficher(self):
        print(f"Appartenance : {self.niveau:.2f} — groupes : {self.groupes}")

if __name__ == "__main__":
    a = Appartenance()
    print(a.rejoindre("famille Isabella", 0.8))
    print(a.rejoindre("cercle Kylian", 0.5))
    a.afficher()
