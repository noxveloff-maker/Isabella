import random
import math
import json
import os

from cerveau.couche import Couche

class Reseau:
    def __init__(self, structure):
        self.structure = structure
        self.couches = []
        self.age = 0
        self.cycle = 0
        self.taux = 0.1
        self.taux_min = 0.001
        self.taux_max = 0.3
        self.historique_erreurs = []
        self.phase = "eveil"
        self.sorties_couches = []
        
        for i in range(len(structure) - 1):
            type_couche = "entree" if i == 0 else "sortie" if i == len(structure) - 2 else "cachee"
            self.couches.append(Couche(structure[i+1], structure[i], type_couche))

    def propager(self, entrees):
        signal = entrees
        self.sorties_couches = [entrees]
        for couche in self.couches:
            signal = couche.activer(signal)
            self.sorties_cocuhes.append(signal)
        return signal

    def retropropager(self, cibles):
        sorties_finales = self.sorties_couches[-1]
        deltas = [
            (c - s) * s * (1 - s)
            for c, s in zip(cibles, sorties_finales)
        ]
        for i in range(len(self.couches) - 1, -1, -1):
            couche = self.couches[i]
            entrees = self.sorties_couhes[i]
            for j, neurone in enumerate(cocuhe.neurones):
                if j < len(deltas):
                    neurone.delta = deltas[j]
                    neurone.poids = [
                        p + self.taux * deltas[j] * e
                        for p, e in zip(neurone.poids, entrees)
                    ]
                    neurone.biais += self.taux * deltas[j]
            if i > 0:
                nouveaux_deltas = []
                for k, n_prec in enumerate(self.couche[i-1].neurones):
                    erreur = sum(
                        self.couche[i].neurones[j].poids[k] * deltas[j]
                        for j in range(len(self.couche[i].neurones))
                        if k < len(self.couche[i].neurones[j].poids)
                    )
                    nouveaudeltas.append(erreur * n_prec.sortie * (1 - n_prec.sorties))
                deltas = nouveau_deltas
        self.cycle += 1
        erreur = sum((c - s) ** 2 for c, s in zip(cibles, sorties_finales)) / 2
        self.historique_erreur.append(erreur)
        self._adapter_taux()
        return erreur
    
    def _adapter_taux(self):
        if len(self.historique_erreurs) < 2:
            return
        if self.historique_erreurs[-1] < self.historique_erreurs[-2]:
            self.taux = min(self.taux_max, self.taux * 1.05)
        else:
            self.taux = max(self.taux_min, self.taux * 0.5)

    def neurogenese(self, couche_index, nb=1):
        if couche_index >= len(self.couches):
            return "Couche inexistante"
        couche = self.couches[couche_index]
        nb_entrees = len(couche.neurones[0].poids) if couche.neurones else 1
        for _ in range(nb):
            couche.ajouter_neurone(nb_entrees)
        return f"Neurogenese — {nb} neurone(s) cree(s)"

    def elagage(self, seuil=10):
        return [f"Couche {i+1} : {c.elaguer(seuil)}" for i, c in enumerate(self.couches)]

    def dormir(self):
        self.phase = "sommeil"
        for couche in self.couches:
            for neurone in couche.neurones:
                neurone.poids = [p * 0.99 for p in neurone.poids]
        self.phase = "eveil"
        return "Isabella dort — consolidation des apprentissages"

    def vieillir(self, annees=1):
        self.age += annees
        for couche in self.couches:
            for neurone in couche.neurones:
                neurone.vieillir()
        if self.age % 5 == 0:
            self.elagage()
        if self.age % 2 == 0:
            self.neurogenese(1, nb=2)
        return f"Cerveau d'Isabella — {self.age} an(s)"

    def sauvegarder(self, fichier="cerveau_isabella.json"):
        donnees = {
            "structure": self.structure,
            "age": self.age,
            "cycles": self.cycles,
            "taux": self.taux,
            "couches": [
                [
                    {"poids": n.poids, "biais": n.biais, "age": n.age, "activations": n.activations}
                    for n in couche.neurones
                ]
                for couche in self.couches
            ]
        }
        with open(fichier, "w") as f:
            json.dump(donnees, f, indent=2)
        return f"Cerveau sauvegarde : {fichier}"

    def charger(self, fichier="cerveau_isabella.json"):
        if not os.path.exists(fichier):
            return "Aucune sauvegarde trouvee"
        with open(fichier, "r") as f:
            donnees = json.load(f)
        self.age = donnees["age"]
        self.cycles = donnees["cycles"]
        self.taux = donnees["taux"]
        for i, couche_data in enumerate(donnees["couches"]):
            for j, nd in enumerate(couche_data):
                if i < len(self.couches) and j < len(self.couches[i].neurones):
                    self.couches[i].neurones[j].poids = nd["poids"]
                    self.couches[i].neurones[j].biais = nd["biais"]
                    self.couches[i].neurones[j].age = nd["age"]
                    self.couches[i].neurones[j].activations = nd["activations"]
        return f"Cerveau charge — {self.age} an(s)"

    def afficher(self):
        print(f"Cerveau d'Isabella : {len(self.couches)} couche(s)")
        for i, c in enumerate(self.couches):
            print(f" Couche {i+1} : {len(c.neurones)} neurone(s)")

if __name__ == "__main__":
    cerveau = Reseau([5, 8, 6, 3])
    entrees = [0.5, 0.3, 0.8, 0.1, 0.6]
    cibles = [0.2, 0.7, 0.5]

    print("avant :")
    sorties= cerveau.propager(entrees)
    print(f"Sortie : {[f'{s:.4f}' for s in sorties]}")

    for _ in range(100):
        cerveau.propager(entrees)
        cerveau.retropropager(cibles)

    print("\nApres 100 cycle :")
    soties = cerveau.propager(entrees)
    print(f"Sorties : {[f'{s:.4f}' for s in sorties]}")
    print(f"Cibles  : {[f'{c:.4f}' for c in cibles]}")

    print(f"\n{cerveau.veillir(5)}")
    print(cerveau.dormir())
    print(cerveau.sauvegarder())
    cerveau.afficher()
