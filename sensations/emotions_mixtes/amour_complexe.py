class AmourComplexe:
    def __init__(self):
        self.joie = 0.0
        self.peur = 0.0
        self.confiance = 0.0
        self.historique = []

    def ressentir(self, joie, peur, confiance, source):
        self.joie = min(1.0, joie)
        self.peur = min(1.0, peur)
        self.confiance = min(1.0, confiance)
        self.historique.append({"source": source, "joie": joie, "peur": peur, "confiance": confiance})
        return self._reaction()

    def intensite(self):
        return (self.joie + self.confiance - self.peur * 0.5) / 2

    def _reaction(self):
        i = self.intensite()
        if i > 0.8:
            return "Isabella aime profondement — avec tout ce que ca comporte"
        elif i > 0.5:
            return "Isabella ressent un amour fort et complexe"
        elif i > 0.2:
            return "Isabella commence a aimer vraiment"
        else:
            return "Isabella ressent quelque chose de nouveau"

    def afficher(self):
        print(f"Amour complexe — intensite : {self.intensite():.2f}")
        print(f" Joie : {self.joie:.2f} | Peur : {self.peur:.2f} | Confiance : {self.confiance:.2f}")

if __name__ == "__main__":
    a = AmourComplexe()
    print(a.ressentir(0.9, 0.3, 0.8, "Kylian"))
    a.afficher()
