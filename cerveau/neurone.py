import math

class Neurone:
    def __init__(self, nb_entrees):
        self.poids = [0.5] * nb_entrees
        self.biais = 0.5

    def activer(self, entrees):
        total = sum(e * p for e, p in zip(entrees, self.poids))
        total += self.biais
        return self._sigmoid(total)

    def _sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

if __name__ == "__main__":
    n = Neurone(nb_entrees=3)
    entrees = [0.8, 0.2, 0.5]
    sortie = n.activer(entrees)
    print(f"Isabella - Premier neurone : {sortie:.4f}")
