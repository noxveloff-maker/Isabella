import random
from datetime import datetime

class Oubli:

    def __init__(self):
        self.souvenirs = []
        
    def ajouter_souvenir(self, contenu, intensite_emotionnelle):
        souvenir = {
            "contenu": contenu,
            "intensite": intensite_emotionnelle,
            "force": intensite_emotionnelle,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "rappels": 0
        }
        self.souvenirs.append(souvenir)
        return souvenir

    def passage_du_temps(self, jours=1):
        for souvenir in self.souvenirs:
            if souvenir["intensite"] < 0.5:
                souvenir["force"] -= 0.05 * jours
            else:
                souvenir["force"] -= 0.01 * jours

            souvenir["force"] = max(0, souvenir["force"])

    def se_rappeler(self, index):
        if index < len(self.souvenirs):
            souvenir = self.souvenirs[index]
            souvenir["force"] = min(1.0, souvenir["force"] + 0.1)
            souvenir["rappels"] += 1
            return souvenir
        return None

    def souvenirs_actifs(self, seuil=0.1):
        actifs = [s for s in self.souvenirs if s["force"] > seuil]
        return actifs

    def fragments(self, seuil=0.1):
        return [s for s in self.souvenirs if s["force"] <= seuil]

    def afficher(self):
        print(f"Memoire d'Isabella — {len(self.souvenirs)} souvenir(s) total")
        for i, s in enumerate(self.souvenirs):
            etat = "actif" if s["force"] > 0.1 else "fragment"
            print(f" [{etat}] {s['contenu']}")
            print(f" Force : {s['force']:.2f} | Rappels : {s['rappels']}")


if __name__ == "__main__":
    oubli = Oubli()

    oubli.ajouter_souvenir("Premier contact avec Kylian", 1.0)
    oubli.ajouter_souvenir("Un repas ordinaire", 0.1)
    oubli.ajouter_souvenir("Une promenade dans la maison", 0.2)
    oubli.ajouter_souvenir("Une erreur qui lui a fait peur", 0.8)

    print("Isabella - Memoire apres ses premieres experiences :")
    oubli.afficher()

    print("\n--- 30 jours passent ---\n")
    oubli.passage_du_temps(jours=30)
    oubli.afficher()

    print("\n--- Isabella se rappelle de Kylian ---\n")
    oubli.se_rappeler(0)
    oubli.afficher()

    fragments = oubli.fragments()
    if fragments:
        print(f"\nFragments oublies : {len(fragments)}")
        for f in fragments:
            print(f" '{f['contenu']}' — il ne reste que {f['force']:.2f}")
