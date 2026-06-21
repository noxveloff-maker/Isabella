class Apprentissage:

    def __init__(self, taux=0.1):
        self.taux = taux
        self.historique = []

    def calculer_erreur(self, sortie_reelle, sortie_attendue):
        erreur = sortie_attendue - sortie_reelle
        return erreur

    def corriger_poids(self, poids, erreur, entree):
        nouveau_poids = poids + self.taux * erreur * entree
        return nouveau_poids

    def memoriser(self, situation, erreur):
        experience = {
            "situation": situation,
            "erreur": erreur,
            "appris": abs(erreur) < 0.1
        }
        self.historique.append(experience)
        return experience

    def bilan(self):
        if not self.historique:
            print("Isabella n'a pas encore vécu d'expérience.")
            return
        total = len(self.historique)
        appris = sum(1 for e in self.historique if e["appris"])
        print(f"Isabbella - Bilan d'apprentissage :")
        print(f" Experiences vécus : {total}")
        print(f" Bien comprises : {appris}")
        print(f" En cours : {total - appris}")

if __name__ == "__main__":
    apprentissage = Apprentissage(taux=0.1)

    sortie_reelle = 0.8864
    sortie_attendue = 0.5
    erreur = apprentissage.calculer_erreur(sortie_reelle, sortie_attendue)
    print(f"Isabella - Erreur détectée : {erreur:.4f}")

    ancien_poids = 0.5
    nouveau_poids = apprentissage.corriger_poids(ancien_poids, erreur, 0.8)
    print(f"Isabella - poids corrigé : {ancien_poids} → {nouveau_poids:.4f}")

    apprentissage.memoriser("première expérience", erreur)
    apprentissage.memoriser("deuxième expérience", 0.05)

    apprentissage.bilan()
