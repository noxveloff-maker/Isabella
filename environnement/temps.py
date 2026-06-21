class Temps:
    def __init__(self):
        self.heure = 8
        self.jour = 1
        self.mois = 1
        self.annee = 0
        self.saison = "printemps"

    def avancer(self, heures=1):
        self.heure += heures
        if self.heure >= 24:
            self.heure -= 24
            self.jour += 1
            if self.jour > 30:
                self.jour = 1
                self.mois += 1
                self._mettre_a_jour_saison()
                if self.mois > 12:
                    self.mois = 1
                    self.annee += 1
        return f"Jour {self.jour} mois {self.mois} — {self.heure}h00"

    def _mettre_a_jour_saison(self):
        if self.mois in [3, 4, 5]:
            self.saison = "printemps"
        elif self.mois in [6, 7, 8]:
            self.saison = "ete"
        elif self.mois in [9, 10, 11]:
            self.saison = "automne"
        else:
            self.saison = "hiver"

    def est_nuit(self):
        return self.heure < 7 or self.heure > 22

    def afficher(self):
        moment = "nuit" if self.est_nuit() else "jour"
        print(f"Jour {self.jour} | Mois {self.mois} | Annee {self.annee}")
        print(f"Heure : {self.heure}h00 | {moment} | Saison : {self.saison}")

if __name__ == "__main__":
    t = Temps()
    print(t.avancer(3))
    print(t.avancer(16))
    t.afficher()
