class Culpabilite:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est rongee par la culpabilite — elle doit reparer"
        elif self.niveau > 0.5:
            return "Isabella se sent responsable et mal a l'aise"
        elif self.niveau > 0.2:
            return "Isabella ressent un leger remords"
        else:
            return "Isabella remarque qu'elle aurait pu faire mieux"

    def diminuer(self, taux=0.03):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Culpabilite : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    c = Culpabilite()
    print(c.ressentir(0.8, "erreur qui a blesse quelqu'un"))
    print(c.ressentir(0.3, "oubli involontaire"))
    c.afficher()
