from datetime import datetime

class Monde:
    def __init__(self):
        self.lieux = {}
        self.heure = 8
        self.jour = 1
        self.meteo = "ensoleille"

    def ajouter_lieu(self, nom, description):
        self.lieux[nom] = {"description": description, "visite": False, "objets": []}
        return f"Lieu ajoute : {nom}"

    def visiter(self, lieu):
        if lieu in self.lieux:
            self.lieux[lieu]["visite"] = True
            return f"Isabella visite : {lieu} — {self.lieux[lieu]['description']}"
        return f"Lieu inconnu : {lieu}"

    def passer_temps(self, heures=1):
        self.heure += heures
        if self.heure >= 24:
            self.heure -= 24
            self.jour += 1
        return f"Jour {self.jour} — {self.heure}h00"

    def afficher(self):
        print(f"Monde d'Isabella — Jour {self.jour} {self.heure}h00")
        print(f"Meteo : {self.meteo}")
        print(f"Lieux connus : {len(self.lieux)}")
        for nom, info in self.lieux.items():
            visite = "visite" if info["visite"] else "inconnu"
            print(f" {nom} [{visite}] — {info['description']}")

if __name__ == "__main__":
    m = Monde()
    print(m.ajouter_lieu("salon", "piece principale chaleureuse"))
    print(m.ajouter_lieu("chambre", "espace calme et intime"))
    print(m.ajouter_lieu("cuisine", "odeurs et chaleur"))
    print(m.visiter("salon"))
    print(m.passer_temps(3))
    print(m.visiter("cuisine"))
    m.afficher()
