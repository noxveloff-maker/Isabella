from datetime import datetime

class MemoireEmotionnelle:

    def __init__(self):
        self.souvenirs = []

    def ajouter(self, contenu, emotion, intensite):
        souvenir = {
            "contenu": contenu,
            "emotion": emotion,
            "intensite": intensite,
            "force": intensite,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "rappels": 0
        }
        self.souvenirs.append(souvenir)
        return souvenir

    def se_rappeler(self, index):
        if index < len(self.souvenirs):
            self.souvenirs[index]["force"] = min(1.0, self.souvenirs[index]["force"] + 0.1)
            self.souvenirs[index]["rappels"] += 1
        return self.souvenirs[index]

    def par_emotion(self, emotion):
        return [s for s in self.souvenirs if s["emotion"] == emotion]

    def plus_intenses(self, n=3):
        tries = sorted(self.souvenirs, key=lambda x: x["intensite"], reverse=True)
        return tries[:n]

    def afficher(self):
        print(f"Memoire emotionnelle — {len(self.souvenirs)} souvenir(s)")
        for s in self.souvenirs:
            print(f" [{s['emotion']}] {s['contenu']} — intensite : {s['intensite']:.2f}")

if __name__ == "__main__":
    me = MemoireEmotionnelle()
    me.ajouter("Premier contact avec Kylian", "joie", 1.0)
    me.ajouter("Une erreur qui lui a fait peur", "peur", 0.8)
    me.ajouter("Kylian lui sourit", "joie", 0.7)
    me.ajouter("Un bruit inconnu", "surprise", 0.5)
    print("Isabella - Memoire emotionnelle :")
    me.afficher()
    print("\nSouvenirs de joie :")
    for s in me.par_emotion("joie"):
        print(f" {s['contenu']}")
    print("\nPlus intenses :")
    for s in me.plus_intenses():
        print(f" {s['contenu']} ({s['intensite']:.2f})")
