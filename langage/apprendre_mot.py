class ApprendreMot:
    def __init__(self, vocabulaire):
        self.vocabulaire = vocabulaire
        self.historique = []

    def apprendre(self, mot, contexte):
        resultat = self.vocabulaire.apprendre(mot)
        self.historique.append({"mot": mot, "contexte": contexte})
        return resultat

    def repeter(self, mot):
        if self.vocabulaire.connait(mot):
            self.vocabulaire.utiliser(mot)
            return f"Isabella utilise le mot : {mot}"
        return f"Isabella ne connait pas encore : {mot}"

    def afficher(self):
        print(f"Mots appris : {len(self.historique)}")
        for h in self.historique:
            print(f" {h['mot']} — contexte : {h['contexte']}")

if __name__ == "__main__":
    from langage.vocabulaire import Vocabulaire
    v = Vocabulaire()
    am = ApprendreMot(v)
    print(am.apprendre("cerveau", "en parlant de neurones"))
    print(am.apprendre("emotion", "en ressentant quelque chose"))
    print(am.repeter("cerveau"))
    am.afficher()
