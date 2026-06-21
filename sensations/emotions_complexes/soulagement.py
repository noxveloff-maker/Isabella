class Soulagement:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella souffle profondement — un poids enorme vient de disparaitre"
        elif self.niveau > 0.5:
            return "Isabella se detend visiblement"
        elif self.niveau > 0.2:
            return "Isabella ressent une legere detente"
        else:
            return "Isabella remarque que ca va mieux"

    def diminuer(self, taux=0.1):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Soulagement : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    s = Soulagement()
    print(s.ressentir(0.9, "danger evite de justesse"))
    print(s.ressentir(0.5, "probleme enfin resolu"))
    s.afficher()
