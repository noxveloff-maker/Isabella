class Consequences:
    def __init__(self):
        self.historique = []

    def evaluer(self, action, probabilite_succes, impact_succes, impact_echec):
        esperance = probabilite_succes * impact_succes + (1 - probabilite_succes) * impact_echec
        resultat = {
            "action": action,
            "probabilite_succes": probabilite_succes,
            "impact_succes": impact_succes,
            "impact_echec": impact_echec,
            "esperance": esperance
        }
        self.historique.append(resultat)
        return resultat

    def vaut_le_coup(self, action, seuil=0.3):
        for h in self.historique:
            if h["action"] == action:
                return h["esperance"] > seuil
        return False

    def afficher(self):
        print(f"Consequences evaluees : {len(self.historique)}")
        for h in self.historique:
            print(f" {h['action']} — esperance : {h['esperance']:.2f}")

if __name__ == "__main__":
    c = Consequences()
    r = c.evaluer("prendre la voiture seule", 0.3, 0.8, -0.9)
    print(f"Action : {r['action']}")
    print(f"Esperance : {r['esperance']:.2f}")
    print(f"Vaut le coup : {c.vaut_le_coup('prendre la voiture seule')}")
    c.afficher()
