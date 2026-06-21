class Anxiete:
    def __init__(self):
        self.niveau = 0.0
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        return self._reaction()

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella est paralyseé par l'anxiete"
        elif self.niveau > 0.5:
            return "Isabella s'inquiete et tourne en rond"
        elif self.niveau > 0.2:
            return "Isabella ressent une tension diffuse"
        else:
            return "Isabella est un peu nerveuse"

    def diminuer(self, taux=0.05):
        self.niveau = max(0.0, self.niveau - taux)

    def afficher(self):
        print(f"Anxiete : {self.niveau:.2f} — {len(self.historique)} experience(s)")

if __name__ == "__main__":
    a = Anxiete()
    print(a.ressentir(0.8, "situation inconnue et menaçante"))
    print(a.ressentir(0.3, "attente d'un resultat"))
    a.afficher()
