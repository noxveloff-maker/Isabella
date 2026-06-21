class FierteHonte:
    def __init__(self):
        self.fierte = 0.0
        self.honte = 0.0

    def ressentir(self, fierte, honte, source):
        self.fierte = min(1.0, fierte)
        self.honte = min(1.0, honte)
        return self._reaction(source)

    def _reaction(self, source):
        if self.fierte > self.honte:
            return f"Isabella est fiere malgre tout de {source}"
        elif self.honte > self.fierte:
            return f"Isabella a honte meme si elle est un peu fiere de {source}"
        else:
            return f"Isabella est partagee entre fierte et honte pour {source}"

    def afficher(self):
        print(f"Fierte : {self.fierte:.2f} | Honte : {self.honte:.2f}")

if __name__ == "__main__":
    fh = FierteHonte()
    print(fh.ressentir(0.7, 0.4, "avoir essaye meme en echouant"))
    print(fh.ressentir(0.3, 0.8, "erreur commise par impulsivite"))
    fh.afficher()
