class Deuil:
    def __init__(self):
        self.niveau = 0.0
        self.etape = "aucune"
        self.historique = []

    def ressentir(self, intensite, source):
        self.niveau = min(1.0, intensite)
        self.historique.append({"intensite": intensite, "source": source})
        self.etape = self._determiner_etape()
        return self._reaction()

    def _determiner_etape(self):
        if self.niveau > 0.8:
            return "deni"
        elif self.niveau > 0.6:
            return "colere"
        elif self.niveau > 0.4:
            return "negociation"
        elif self.niveau > 0.2:
            return "depression"
        else:
            return "acceptation"

    def _reaction(self):
        if self.etape == "deni":
            return "Isabella refuse d'accepter la perte"
        elif self.etape == "colere":
            return "Isabella est en colere contre la situation"
        elif self.etape == "negociation":
            return "Isabella cherche une issue impossible"
        elif self.etape == "depression":
            return "Isabella est triste et abattue"
        else:
            return "Isabella accepte et avance"

    def afficher(self):
        print(f"Deuil : {self.niveau:.2f} — etape : {self.etape}")

if __name__ == "__main__":
    d = Deuil()
    print(d.ressentir(0.9, "perte d'un souvenir important"))
    print(d.ressentir(0.3, "fin d'une periode heureuse"))
    d.afficher()
