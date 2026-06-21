import json
import os

class Chargement:
    def __init__(self, dossier="sauvegardes"):
        self.dossier = dossier

    def charger(self, fichier):
        chemin = f"{self.dossier}/{fichier}"
        if not os.path.exists(chemin):
            return None
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)

    def lister_disponibles(self, prefixe=None):
        if not os.path.exists(self.dossier):
            return []
        fichiers = os.listdir(self.dossier)
        if prefixe:
            fichiers = [f for f in fichiers if f.startswith(prefixe)]
        return sorted(fichiers)

    def afficher(self, prefixe=None):
        fichiers = self.lister_disponibles(prefixe)
        print(f"Fichiers disponibles : {len(fichiers)}")
        for f in fichiers:
            print(f" {f}")

if __name__ == "__main__":
    c = Chargement()
    c.afficher()
    fichiers = c.lister_disponibles("isabella")
    if fichiers:
        dernier = fichiers[-1]
        donnees = c.charger(dernier)
        print(f"Charge : {donnees}")
    else:
        print("Aucune sauvegarde trouvee — lance sauvegarde.py d'abord")
