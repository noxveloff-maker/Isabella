from datetime import datetime

class Reconciliation:
    def __init__(self):
        self.reconciliations = []

    def se_reconcilier(self, personne, geste, impact):
        reconciliation = {
            "personne": personne,
            "geste": geste,
            "impact": impact,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.reconciliations.append(reconciliation)
        return self._reaction(personne, geste, impact)

    def _reaction(self, personne, geste, impact):
        if impact > 0.7:
            return f"Isabella et {personne} se reconclient profondement grace a : {geste}"
        elif impact > 0.4:
            return f"Isabella et {personne} font la paix : {geste}"
        else:
            return f"Isabella et {personne} avancent timidement : {geste}"

    def afficher(self):
        print(f"Reconciliations : {len(self.reconciliations)}")
        for r in self.reconciliations:
            print(f" {r['personne']} — {r['geste']} (impact : {r['impact']:.2f})")

if __name__ == "__main__":
    r = Reconciliation()
    print(r.se_reconcilier("Kylian", "discussion honnete et excuses mutuelles", 0.9))
    print(r.se_reconcilier("frere", "moment complice partage", 0.6))
    r.afficher()
