class JalousieAmour:
    def __init__(self):
        self.jalousie = 0.0
        self.amour = 0.0

    def ressentir(self, jalousie, amour, source):
        self.jalousie = min(1.0, jalousie)
        self.amour = min(1.0, amour)
        return self._reaction(source)

    def _reaction(self, source):
        if self.jalousie > 0.7 and self.amour > 0.7:
            return f"Isabella aime fort et souffre fort a cause de {source}"
        elif self.jalousie > self.amour:
            return f"La jalousie prend le dessus sur l'amour pour {source}"
        else:
            return f"L'amour reste plus fort que la jalousie pour {source}"

    def afficher(self):
        print(f"Jalousie : {self.jalousie:.2f} | Amour : {self.amour:.2f}")

if __name__ == "__main__":
    ja = JalousieAmour()
    print(ja.ressentir(0.7, 0.9, "Kylian passe du temps ailleurs"))
    ja.afficher()
