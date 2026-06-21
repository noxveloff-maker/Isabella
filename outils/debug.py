from datetime import datetime

class Debug:
    def __init__(self, actif=True):
        self.actif = actif
        self.logs = []

    def log(self, module, message, niveau="INFO"):
        if not self.actif:
            return
        entree = {
            "date": datetime.now().strftime("%H:%M:%S"),
            "module": module,
            "message": message,
            "niveau": niveau
        }
        self.logs.append(entree)
        print(f"[{entree['date']}] [{niveau}] {module} — {message}")

    def erreur(self, module, message):
        self.log(module, message, "ERREUR")

    def info(self, module, message):
        self.log(module, message, "INFO")

    def vider(self):
        self.logs = []

    def afficher(self):
        print(f"Logs : {len(self.logs)}")
        for l in self.logs[-5:]:
            print(f" [{l['niveau']}] {l['module']} : {l['message']}")

if __name__ == "__main__":
    d = Debug(actif=True)
    d.info("cerveau", "neurone initialise")
    d.info("memoire", "souvenir ajoute")
    d.erreur("apprentissage", "poids incorrect detecte")
    d.info("emotions", "joie activee a 0.8")
    d.afficher()
