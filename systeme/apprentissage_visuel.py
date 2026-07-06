import json
import os
from datetime import datetime
from collections import defaultdict

class ApprentissageVisuel:
    """
    Memorise les positions d'elements a l'ecran.
    Apres avoir clique quelque part, apprend sa position pour la prochaine fois.
    """

    def __init__(self, fichier="apprentissage_visuel.json"):
        self.fichier = fichier
        self.positions = {}  # nom_element -> {x, y, ecran, date, nb_clics}
        self._charger()

    def _charger(self):
        if os.path.exists(self.fichier):
            with open(self.fichier, "r", encoding="utf-8") as f:
                self.positions = json.load(f)

    def _sauvegarder(self):
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(self.positions, f, ensure_ascii=False, indent=2)

    def apprendre_position(self, nom, x, y, ecran=None):
        """Apprend la position d'un element clique."""
        cle = self._normaliser_nom(nom)
        if cle not in self.positions:
            self.positions[cle] = {
                "nom_original": nom,
                "positions": [],
                "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M")
            }

        self.positions[cle]["positions"].append({
            "x": x, "y": y, "ecran": ecran,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        # Garde seulement les 5 dernieres positions
        self.positions[cle]["positions"] = self.positions[cle]["positions"][-5:]
        self._sauvegarder()

        return {
            "succes": True,
            "nom": cle,
            "position_moyenne": self._position_moyenne(cle)
        }

    def trouver_position(self, nom):
        """Trouve la position memorisee d'un element."""
        cle = self._normaliser_nom(nom)
        if cle not in self.positions:
            return {"erreur": f"Position de '{nom}' inconnue. Tu dois d'abord cliquer dessus."}

        pos = self._position_moyenne(cle)
        return {
            "succes": True,
            "nom": cle,
            "x": pos["x"],
            "y": pos["y"],
            "nb_observations": len(self.positions[cle]["positions"])
        }

    def lister_positions(self):
        """Liste tous les elements appris."""
        return [
            {
                "nom": k,
                "nom_original": v["nom_original"],
                "position": self._position_moyenne(k),
                "nb_observations": len(v["positions"]),
                "derniere_date": v["positions"][-1]["date"] if v["positions"] else None
            }
            for k, v in self.positions.items()
        ]

    def oublier(self, nom):
        """Oublie une position."""
        cle = self._normaliser_nom(nom)
        if cle in self.positions:
            del self.positions[cle]
            self._sauvegarder()
            return {"succes": True}
        return {"erreur": "Position inconnue"}

    def _position_moyenne(self, cle):
        """Calcule la position moyenne d'un element."""
        positions = self.positions[cle]["positions"]
        if not positions:
            return {"x": 0, "y": 0}
        x = sum(p["x"] for p in positions) // len(positions)
        y = sum(p["y"] for p in positions) // len(positions)
        return {"x": x, "y": y}

    def _normaliser_nom(self, nom):
        """Normalise un nom d'element."""
        return nom.lower().strip().replace(" ", "_")

if __name__ == "__main__":
    a = ApprentissageVisuel()
    print("=== Test Apprentissage Visuel ===")

    a.apprendre_position("bouton_ouvrir", 100, 200)
    a.apprendre_position("bouton_ouvrir", 105, 198)  # Legerement different
    a.apprendre_position("bouton_fermer", 500, 20)

    print("\nPositions apprises:")
    for p in a.lister_positions():
        print(f"  {p['nom']} : ({p['position']['x']}, {p['position']['y']}) — {p['nb_observations']}x")

    print("\nTrouver 'bouton ouvrir':")
    print(a.trouver_position("bouton ouvrir"))

    print("\nTrouver 'inconnu':")
    print(a.trouver_position("inconnu"))
