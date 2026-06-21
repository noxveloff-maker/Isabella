class Inconfort:

    def __init__(self):
        self.niveau = 0.0
        self.sources = []

    def ajouter_source(self, source, intensite):
        self.sources.append({"source": source, "intensite": intensite})
        self.niveau = min(1.0, self.niveau + intensite)
        return self._reaction()

    def retirer_source(self, source):
        self.sources = [s for s in self.sources if s["source"] != source]
        self.niveau = sum(s["intensite"] for s in self.sources)
        self.niveau = min(1.0, self.niveau)

    def _reaction(self):
        if self.niveau > 0.8:
            return "Isabella ne supporte plus la situation"
        elif self.niveau > 0.5:
            return "Isabella est clairement genee"
        elif self.niveau > 0.2:
            return "Isabella ressent un leger inconfort"
        else:
            return "Isabella va bien"

    def afficher(self):
        print(f"Inconfort : {self.niveau:.2f}")
        for s in self.sources:
            print(f" Source : {s['source']} ({s['intensite']:.2f})")

if __name__ == "__main__":
    i = Inconfort()
    print(i.ajouter_source("bruit fort", 0.4))
    print(i.ajouter_source("temperature trop haute", 0.3))
    i.retirer_source("bruit fort")
    i.afficher()
