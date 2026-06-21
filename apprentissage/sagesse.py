from datetime import datetime

class Sagesse:
    def __init__(self):
        self.niveau = 0.0
        self.lecons = []

    def acquerir(self, lecon, source, poids=0.05):
        self.niveau = min(1.0, self.niveau + poids)
        self.lecons.append({
            "lecon": lecon,
            "source": source,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "poids": poids
        })
        return f"Isabella gagne en sagesse : {lecon}"

    def plus_importantes(self, n=3):
        tries = sorted(self.lecons, key=lambda x: x["poids"], reverse=True)
        return tries[:n]

    def afficher(self):
        print(f"Sagesse : {self.niveau:.2f} — {len(self.lecons)} lecon(s)")
        for l in self.lecons[-3:]:
            print(f" [{l['source']}] {l['lecon']}")

if __name__ == "__main__":
    s = Sagesse()
    print(s.acquerir("le feu brule — ne pas toucher", "experience directe", 0.1))
    print(s.acquerir("Kylian est de confiance", "temps et observations", 0.15))
    print(s.acquerir("les erreurs font partie de l'apprentissage", "reflexion", 0.1))
    s.afficher()
    print("\nLecons les plus importantes :")
    for l in s.plus_importantes():
        print(f" {l['lecon']}")
