import json
import os
from datetime import datetime

class Sauvegarde:
    def __init__(self, dossier="sauvegardes"):
        self.dossier = dossier
        if not os.path.exists(dossier):
            os.makedirs(dossier)

    def sauvegarder(self, nom, donnees):
        horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
        fichier = f"{self.dossier}/{nom}_{horodatage}.json"
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        return f"Sauvegarde : {fichier}"

    def lister(self):
        if not os.path.exists(self.dossier):
            return []
        return os.listdir(self.dossier)

    def charger_dernier(self, nom):
        fichiers = [f for f in self.lister() if f.startswith(nom)]
        if not fichiers:
            return None
        dernier = sorted(fichiers)[-1]
        with open(f"{self.dossier}/{dernier}", "r", encoding="utf-8") as f:
            return json.load(f)

    def afficher(self):
        print(f"Sauvegardes disponibles : {len(self.lister())}")
        for f in self.lister():
            print(f" {f}")

if __name__ == "__main__":
    s = Sauvegarde()
    print(s.sauvegarder("isabella_etat", {"age": 5, "niveau_sagesse": 0.3, "emotion": "joie"}))
    s.afficher()
    dernier = s.charger_dernier("isabella_etat")
    print(f"Dernier etat charge : {dernier}")
