import random

class Poids:

    def __init__(self, nb_entrees, nb_sorties):
        self.matrice = [
            [random.uniform(-1, 1) for _ in range(nb_entrees)]
            for _ in range(nb_sorties)
        ]
        self.nb_entrees = nb_entrees
        self.nb_sorties = nb_sorties

    def obtenir(self, neurone_sortie, neurone_entree):
        return self.matrice[neurone_sortie][neurone_entree]

    def modifier(self, neurone_sortie, neurone_entree, nouvelle_valeur):
        ancien = self.matrice[neurone_sortie][neurone_entree]
        self.matrice[neurone_sortie][neurone_entree] = nouvelle_valeur
        return ancien, nouvelle_valeur

    def renforcer(self, neurone_sortie, neurone_entree, taux=0.1):
        self.matrice[neurone_sortie][neurone_entree] += taux
        return self.matrice[neurone_sortie][neurone_entree]

    def affaiblir(self, neurone_sortie, neurone_entree, taux=0.1):
        self.matrice[neurone_sortie][neurone_entree] -= taux
        return self.matrice[neurone_sortie][neurone_entree]

    def afficher(self):
        print(f"Connexions d'Isabella : {self.nb_entrees} entrees, {self.nb_sorties} sorties")
        for i, ligne in enumerate(self.matrice):
            valeur = [f"{p:.3f}" for p in ligne]
            print(f"Neurone {i+1} : {valeur}")

if __name__ == "__main__":
    poids = Poids(nb_entrees=3, nb_sorties=2)

    print("Isabella - etat initial des connexions :")
    poids.afficher()

    print("\nIsabella - Renforcement d'une connexion :")
    avant = poids.obtenir(0, 0)
    apres = poids.renforcer(0, 0)
    print(f" connexion 1->1 : {avant:.3f} ---> {apres:.3f}")

    print("\nIsabella - Afaiblissement d'une connexion peu utiliee :")
    avant = poids.obtenir(1, 2)
    apres = poids.affaiblir(1, 2)
    print(f" connexion 2->3 : {avant:.3f} ---> {apres:.3f}")
