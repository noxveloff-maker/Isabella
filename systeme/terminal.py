import subprocess
import os
import shlex
from datetime import datetime

class Terminal:
    """Execute des commandes shell et gère les processus."""

    def __init__(self):
        self.historique = []
        self.processus_actifs = {}

    def executer(self, commande, timeout=30, working_dir=None):
        """Execute une commande de maniere securisee."""
        commande = commande.strip()
        if not commande:
            return {"erreur": "Commande vide"}

        # Interdiction des commandes dangereuses
        mots_interdits = ["rm -rf /", "mkfs", "dd if=/dev/zero", "> /dev/sda", "format", ":(){ :|:& }:", "shutdown"]
        for mot in mots_interdits:
            if mot in commande.lower():
                return {
                    "erreur": f"Commande bloquee pour securite : {mot}",
                    "commande": commande
                }

        try:
            result = subprocess.run(
                commande,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=working_dir or os.getcwd()
            )
            self._log(commande, result.returncode)
            return {
                "commande": commande,
                "code_retour": result.returncode,
                "stdout": result.stdout[-5000:] if result.stdout else "",
                "stderr": result.stderr[-2000:] if result.stderr else "",
                "succes": result.returncode == 0
            }
        except subprocess.TimeoutExpired:
            return {"erreur": "Commande trop longue (timeout)", "commande": commande}
        except Exception as e:
            return {"erreur": f"Erreur execution : {e}", "commande": commande}

    def executer_long(self, commande, nom="processus"):
        """Lance un processus en arriere-plan."""
        try:
            process = subprocess.Popen(
                commande,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.processus_actifs[nom] = {
                "process": process,
                "commande": commande,
                "pid": process.pid,
                "lance": datetime.now().strftime("%H:%M:%S")
            }
            self._log(commande, 0, bg=True)
            return {
                "succes": True,
                "nom": nom,
                "pid": process.pid,
                "commande": commande
            }
        except Exception as e:
            return {"erreur": f"Impossible de lancer : {e}"}

    def lire_processus(self, nom):
        """Lit la sortie d'un processus en arriere-plan."""
        if nom not in self.processus_actifs:
            return {"erreur": f"Processus '{nom}' inconnu"}
        proc = self.processus_actifs[nom]["process"]
        stdout = ""
        stderr = ""
        try:
            stdout, stderr = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            return {
                "nom": nom,
                "pid": proc.pid,
                "statut": "en cours",
                "poll": proc.poll()
            }
        return {
            "nom": nom,
            "pid": proc.pid,
            "statut": "termine" if proc.poll() is not None else "en cours",
            "stdout": stdout[-2000:] if stdout else "",
            "stderr": stderr[-500:] if stderr else ""
        }

    def tuer_processus(self, nom):
        """Arrete un processus en arriere-plan."""
        if nom not in self.processus_actifs:
            return {"erreur": f"Processus '{nom}' inconnu"}
        proc = self.processus_actifs[nom]["process"]
        try:
            proc.terminate()
            proc.wait(timeout=5)
            del self.processus_actifs[nom]
            return {"succes": True, "nom": nom, "message": "Processus arrete"}
        except:
            proc.kill()
            return {"succes": True, "nom": nom, "message": "Processus force-arrete"}

    def liste_processus(self):
        """Liste les processus en arriere-plan."""
        return {
            "actifs": [
                {
                    "nom": nom,
                    "pid": info["pid"],
                    "commande": info["commande"],
                    "lance": info["lance"]
                }
                for nom, info in self.processus_actifs.items()
            ]
        }

    def _log(self, commande, code, bg=False):
        self.historique.append({
            "commande": commande,
            "code": code,
            "arriere_plan": bg,
            "date": datetime.now().strftime("%H:%M:%S")
        })

if __name__ == "__main__":
    t = Terminal()
    print("=== Test terminal ===")
    print(t.executer("echo 'Hello Isabella' && ls -la"))
    print("\n--- Processus ---")
    print(t.executer("ps aux | head -5"))
    print("\n--- Historique ---")
    for h in t.historique:
        print(h)
