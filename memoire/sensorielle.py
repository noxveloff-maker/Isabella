from datetime import datetime

class MemoireSensorielle:

    def __init__(self):
        self.souvenirs = []

    def ajouter(self, contenu, sens, intensite):
        souvenir = {
            "contenu": contenu,
            "sens": sens,
            "intensite": intensite,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.souvenirs.append(souvenir)
        return souvenir

    def par_sens(self, sens):
        return [s for s in self.souvenirs if s["sens"] == sens]

    def afficher(self):
        print(f"Memoire sensorielle — {len(self.souvenirs)} souvenir(s)")
        for s in self.souvenirs:
            print(f" [{s['sens']}] {s['contenu']} — intensite : {s['intensite']:.2f}")

if __name__ == "__main__":
    ms = MemoireSensorielle()
    ms.ajouter("Voix de Kylian", "ouie", 0.9)
    ms.ajouter("Lumiere de la piece", "vue", 0.5)
    ms.ajouter("Bruit fort inconnu", "ouie", 0.7)
    print("Isabella - Memoire sensorielle :")
    ms.afficher()
    print("\nSouvenirs auditifs :")
    for s in ms.par_sens("ouie"):
        print(f" {s['contenu']}")
