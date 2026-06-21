# court_terme.py
# Ce qu'Isabella vient de vivre — les dernières secondes et minutes
# Kylian - Jour 2

from datetime import datetime

class CourtTerme:

    # === SECTION 1 : Initialisation ===
    def __init__(self, capacite=10):
        # Capacité limitée — comme l'attention humaine
        # On ne peut pas tout retenir en même temps
        self.capacite = capacite
        self.memoire = []

    # === SECTION 2 : Ajouter une information ===
    def ajouter(self, information, importance=0.5):
        entree = {
            "contenu": information,
            "importance": importance,
            "heure": datetime.now().strftime("%H:%M:%S"),
            "age": 0
        }
        self.memoire.append(entree)

        # Si la mémoire est pleine — on oublie la moins importante
        if len(self.memoire) > self.capacite:
            self._oublier_moins_important()

        return entree

    # === SECTION 3 : Oublier le moins important ===
    def _oublier_moins_important(self):
        if self.memoire:
            min_importance = min(self.memoire, key=lambda x: x["importance"])
            self.memoire.remove(min_importance)

    # === SECTION 4 : Vieillir les souvenirs ===
    def vieillir(self):
        for entree in self.memoire:
            entree["age"] += 1
            # Les souvenirs peu importants vieillissent plus vite
            if entree["importance"] < 0.5:
                entree["importance"] -= 0.1
                entree["importance"] = max(0, entree["importance"])

    # === SECTION 5 : Ce dont Isabella est consciente maintenant ===
    def conscience_actuelle(self):
        actifs = sorted(self.memoire, key=lambda x: x["importance"], reverse=True)
        return actifs[:3] # Les 3 plus importants en ce moment

    # === SECTION 6 : Afficher ===
    def afficher(self):
        print(f"Memoire court terme — {len(self.memoire)}/{self.capacite}")
        for e in self.memoire:
            print(f" [{e['heure']}] {e['contenu']}")
            print(f" Importance : {e['importance']:.2f} | Age : {e['age']}")


# === TEST ===
if __name__ == "__main__":
    ct = CourtTerme(capacite=5)

    ct.ajouter("Kylian lui parle", importance=0.9)
    ct.ajouter("Un bruit dans la maison", importance=0.3)
    ct.ajouter("Une lumiere s'allume", importance=0.2)
    ct.ajouter("Kylian sourit", importance=0.8)
    ct.ajouter("Silence", importance=0.1)

    print("Isabella - Memoire immediate :")
    ct.afficher()

    print("\nIsabella - Ce dont elle est consciente maintenant :")
    for e in ct.conscience_actuelle():
        print(f" {e['contenu']} ({e['importance']:.2f})")

    print("\n--- Le temps passe ---")
    ct.vieillir()
    ct.vieillir()
    ct.afficher()
