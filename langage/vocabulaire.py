class Vocabulaire:
    def __init__(self):
        self.mots = {}
        self._charger_base()

    def _charger_base(self):
        mots_base = ["bonjour", "merci", "oui", "non", "aide", "comprends", "veux", "peux", "suis", "Isabella"]
        for mot in mots_base:
            self.mots[mot] = {"connu": True, "utilisation": 0}

    def apprendre(self, mot):
        if mot not in self.mots:
            self.mots[mot] = {"connu": True, "utilisation": 0}
            return f"Isabella apprend le mot : {mot}"
        return f"Isabella connait deja : {mot}"

    def utiliser(self, mot):
        if mot in self.mots:
            self.mots[mot]["utilisation"] += 1
            return True
        return False

    def connait(self, mot):
        return mot in self.mots

    def afficher(self):
        print(f"Vocabulaire : {len(self.mots)} mot(s)")
        for mot, info in list(self.mots.items())[:5]:
            print(f" {mot} — utilise {info['utilisation']} fois")

if __name__ == "__main__":
    v = Vocabulaire()
    print(v.apprendre("Python"))
    print(v.apprendre("neurone"))
    print(v.apprendre("bonjour"))
    v.utiliser("bonjour")
    v.utiliser("Python")
    v.afficher()
