class Retropropagation:

    def __init__(self, taux=0.1):
        self.taux = taux

    def derivee_sigmoid(self, sortie):
        return sortie * (1 - sortie)

    def delta_sortie(self, sortie, cible):
        erreur = cible - sortie
        return erreur * self.derivee_sigmoid(sortie)

    def delta_cache(self, sortie, deltas_suivants, poids_suivants):
        erreur_remontee = sum(d * p for d, p in zip(deltas_suivants, poids_suivants))
        return erreur * self.derivee_sigmoid(sortie)

    def maj_poids(self, poids, delta, entree):
        return poids + self.taux * delta * entree

    def corriger_couche(self, couche, deltas, entrees):
        for neurone, delta in zip(couche.neurones, deltas):
            neurone.poids = [
                self.maj_poids(p, delta, e)
                for p, e in zip(neurone.poids, entrees)
            ]
            neurone.biais = neurone.biais + self.taux * delta

if __name__ == "__main__":
    from cerveau.reseau import Reseau

    retro = Retropropagation(taux=0.1)

    cerveau = Reseau([3, 4, 2])
    entrees = [0.8, 0.2, 0.5]
    cibles = [0.3, 0.7]

    sorties_avant = cerveau.propager(entrees)
    print("Isabella - Avant apprentissage :")
    for i, s in enumerate(sorties_avant):
        print(f" Sortie {i+1} : {s:.4f} (cible : {cibles[i]})")

    deltas_sortie = [
        retro.delta_sortie(s, c)
        for s, c in zip(sorties_avant, cibles)
    ]

    sorties_couche_precedente = cerveau.couches[-2].activer(entrees)
    retro.corriger_couche(cerveau.couches[-1], deltas_sortie, sorties_couche_precedente)

    sorties_apres = cerveau.propager(entrees)
    print("\nIsabella - Après apprentissage :")
    for i, s in enumerate(sorties_apres):
        print(f" Sortie {i+1} : {s:.4f} (cible : {cibles[i]})")

    print("\nIsabella apprend - elle se rapproche de la cible.")
