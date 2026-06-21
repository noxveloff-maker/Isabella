class Maison:
    def __init__(self):
        self.pieces = {}
        self._construire()

    def _construire(self):
        self.pieces = {
            "salon": {"description": "piece principale chaleureuse", "visite": False, "confort": 0.8},
            "cuisine": {"description": "odeurs et chaleur", "visite": False, "confort": 0.7},
            "chambre_isabella": {"description": "espace intime d'Isabella", "visite": False, "confort": 0.9},
            "salle_de_bain": {"description": "calme et frais", "visite": False, "confort": 0.6},
            "couloir": {"description": "passage entre les pieces", "visite": False, "confort": 0.5},
        }

    def visiter(self, piece):
        if piece in self.pieces:
            self.pieces[piece]["visite"] = True
            return f"Isabella entre dans : {piece} — {self.pieces[piece]['description']}"
        return f"Piece inconnue : {piece}"

    def confort_piece(self, piece):
        if piece in self.pieces:
            return self.pieces[piece]["confort"]
        return 0.0

    def afficher(self):
        print(f"Maison — {len(self.pieces)} piece(s)")
        for nom, info in self.pieces.items():
            visite = "visitee" if info["visite"] else "inconnue"
            print(f" {nom} [{visite}] — confort : {info['confort']:.2f}")

if __name__ == "__main__":
    m = Maison()
    print(m.visiter("salon"))
    print(m.visiter("chambre_isabella"))
    print(m.visiter("cuisine"))
    m.afficher()
