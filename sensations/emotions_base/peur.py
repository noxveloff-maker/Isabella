class Peur:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est paralysee de peur"
        elif self.niveau > 0.5:
            return "Isabella recule et cherche a fuir"
        elif self.niveau > 0.2:
            return "Isabella est sur ses gardes"
        else:
            return "Isabella est vigilante"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Peur : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    p = Peur()
    print(p.ressentir(0.9, "bruit fort et inconnu"))
    print(p.ressentir(0.4, "situation nouvelle"))
    p.afficher()
