class Exterieur:
    def __init__(self):
        self.decouverte = False
        self.lieux_connus = []
        self.peur_initiale = 0.6

    def decouvrir(self):
        if not self.decouverte:
            self.decouverte = True
            self.peur_initiale = max(0.0, self.peur_initiale - 0.2)
            return "Isabella decouvre l'exterieur pour la premiere fois — immense et inconnu"
        return "Isabella sort dehors — elle commence a connaitre ce monde"

    def explorer(self, lieu):
        if lieu not in self.lieux_connus:
            self.lieux_connus.append(lieu)
            return f"Isabella explore : {lieu} — nouveau lieu decouvert"
        return f"Isabella revisite : {lieu}"

    def afficher(self):
        print(f"Exterieur — decouverte : {self.decouverte}")
        print(f" Lieux connus : {self.lieux_connus}")
        print(f" Peur de l'inconnu : {self.peur_initiale:.2f}")

if __name__ == "__main__":
    e = Exterieur()
    print(e.decouvrir())
    print(e.explorer("jardin"))
    print(e.explorer("rue"))
    e.afficher()
