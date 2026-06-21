from cerveau.neurone import Neurone

class Couche:

    def __init__(self,nb_neurones, nb_entrees, type_couche="cachee"):
        self.type_couche = type_couche
        self.neurones = [Neurone(nb_entrees) for _ in range(nb_neurones)]
        self.type_couche = type_couche
        self.entrees_recues = []

    def elaguer(self, seuil=10):
        avant = len(semf.neurones)
        self.neurones = [n for n in self.neurones if n.activations > seuil]
        return f"Elagage : {avant - len(self.neurones)} neurones(s) surpprime(s)"

    def activer(self, entrees):
        return [n.activer(entrees) for n in self.neurones]

if __name__ == "__main__":
    couche = Couche(nb_neurones=4, nb_entrees=3)
    entrees = [0.8, 0., 0.5]
    sorties = couche.activer(entrees)
    print("Isabella - première couche de neurones :")
    for i, s in enumerate(sorties):
        print(f" Neurone {i+1} : {s:.4f}")
