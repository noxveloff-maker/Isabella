class Valeurs:
    def __init__(self):
        self.valeurs = {
            "honnetete": 0.8,
            "loyaute": 0.9,
            "curiosite": 0.8,
            "bienveillance": 0.7,
            "courage": 0.6,
            "prudence": 0.5
        }

    def renforcer(self, valeur, quantite=0.05):
        if valeur in self.valeurs:
            self.valeurs[valeur] = min(1.0, self.valeurs[valeur] + quantite)
            return f"Valeur renforcee : {valeur} — {self.valeurs[valeur]:.2f}"
        return f"Valeur inconnue : {valeur}"

    def affaiblir(self, valeur, quantite=0.05):
        if valeur in self.valeurs:
            self.valeurs[valeur] = max(0.0, self.valeurs[valeur] - quantite)
            return f"Valeur affaiblie : {valeur} — {self.valeurs[valeur]:.2f}"
        return f"Valeur inconnue : {valeur}"

    def dominante(self):
        return max(self.valeurs, key=self.valeurs.get)

    def afficher(self):
        print("Valeurs d'Isabella :")
        for v, n in sorted(self.valeurs.items(), key=lambda x: x[1], reverse=True):
            print(f" {v} : {n:.2f}")

if __name__ == "__main__":
    v = Valeurs()
    v.afficher()
    print(v.renforcer("courage"))
    print(v.affaiblir("prudence"))
    print(f"Valeur dominante : {v.dominante()}")
