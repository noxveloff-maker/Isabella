from datetime import datetime
import json
import os

class JournalAuto:
    def __init__(self, fichier="journal_isabella.json"):
        self.fichier = fichier
        self.entrees = []
        self._charger()

    def _charger(self):
        if os.path.exists(self.fichier):
            with open(self.fichier, "r", encoding="utf-8") as f:
                self.entrees = json.load(f)

    def _sauvegarder(self):
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(self.entrees, f, ensure_ascii=False, indent=2)

    def noter(self, evenement, emotion, intensite):
        entree = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "evenement": evenement,
            "emotion": emotion,
            "intensite": intensite
        }
        self.entrees.append(entree)
        self._sauvegarder()
        return entree

    def afficher(self, n=5):
        print(f"Journal d'Isabella — {len(self.entrees)} entree(s)")
        for e in self.entrees[-n:]:
            print(f" [{e['date']}] {e['evenement']}")
            print(f" Emotion : {e['emotion']} ({e['intensite']:.2f})")

if __name__ == "__main__":
    j = JournalAuto()
    j.noter("Premier contact avec Kylian", "joie", 1.0)
    j.noter("Premier neurone code", "fierte", 0.9)
    j.noter("Premiere erreur corrigee", "soulagement", 0.7)
    j.afficher()
