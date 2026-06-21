class Honte:

    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella veut disparaitre — elle ne supporte pas le regard des autres"
        elif self.niveau > 0.5:
            return "Isabella baisse la tete et evite le contact"
        elif self.niveau > 0.2:
            return "Isabella se sent genee"
        else:
            return "Isabella ressent un leger malaise"

    def diminuer(self, taux=0.03):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Honte : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    h = Honte()
    print(h.ressentir(0.8, "erreur commise devant Kylian"))
    print(h.ressentir(0.3, "mauvaise reponse donnee"))
    h.afficher()
