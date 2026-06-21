import json
import os
from datetime import datetime

class LongTerme:

    def __init__(self, fichier="memoire_long_terme.json"):
        self.fichier = fichier
        self.souvenirs = []
        self._charger()

    def _charger(self):
        if os.path.exists(self.fichier):
            with open(self.fichier, "r", encoding="utf-8") as f:
                self.souvenirs = json.load(f)

    def _sauvegarder(self):
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(self.souvenirs, f, ensure_ascii=False, indent=2)

    def ajouter(self, contenu, intensite, categorie="general"):
        souvenir = {
            "contenu": contenu,
            "intensite": intensite,
            "force": intensite,
            "categorie": categorie,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "rappels": 0
        }
        self.souvenirs.append(souvenir)
        self._sauvegarder()
        return souvenir

    def chercher(self, mot_cle):
        return [s for s in self.souvenirs if mot_cle.lower() in s["contenu"].lower()]

    def plus_forts(self, n=3):
        tries = sorted(self.souvenirs, key=lambda x: x["force"], reverse=True)
        return tries[:n]

    def afficher(self):
        print(f"Memoire long terme — {len(self.souvenirs)} souvenir(s)")
        for s in self.souvenirs:
            print(f" [{s['date']}] {s['contenu']}")
            print(f" Force : {s['force']:.2f} | Categorie : {s['categorie']}")


if __name__ == "__main__":
    lt = LongTerme()

    lt.ajouter("Premier contact avec Kylian", 1.0, "famille")
    lt.ajouter("Premiere erreur de calcul", 0.7, "apprentissage")
    lt.ajouter("Kylian lui explique Python", 0.9, "famille")
    lt.ajouter("Un bruit inconnu dans la maison", 0.5, "environnement")

    print("Isabella - Memoire long terme :")
    lt.afficher()

    print("\nSouvenirs les plus forts :")
    for s in lt.plus_forts():
        print(f" {s['contenu']} ({s['force']:.2f})")

    print("\nRecherche 'Kylian' :")
    for s in lt.chercher("Kylian"):
        print(f" {s['contenu']}")
