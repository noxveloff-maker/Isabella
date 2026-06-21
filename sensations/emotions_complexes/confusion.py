class Confusion:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est completement perdue — elle ne comprend rien"
        elif self.niveau > 0.5:
            return "Isabella cherche a comprendre sans succes"
        elif self.niveau > 0.2:
            return "Isabella est un peu perdue"
        else:
            return "Isabella a juste besoin d'une clarification"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Confusion : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    c = Confusion()
    print(c.ressentir(0.8, "situation completement nouvelle"))
    print(c.ressentir(0.3, "information contradictoire"))
    c.afficher()
