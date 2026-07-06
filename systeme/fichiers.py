import os
import json
import glob
from datetime import datetime

class Fichiers:
    """Gestion des fichiers et dossiers — lecture, ecriture, navigation, recherche."""

    def __init__(self, racine="/"):
        self.racine = racine
        self.historique = []

    def lister(self, chemin=".", profondeur=1):
        """Liste le contenu d'un dossier."""
        chemin = os.path.expanduser(chemin)
        if not os.path.exists(chemin):
            return {"erreur": f"Chemin introuvable : {chemin}"}
        if not os.path.isdir(chemin):
            return {"erreur": f"Ce n'est pas un dossier : {chemin}"}

        resultat = {"chemin": chemin, "dossiers": [], "fichiers": []}
        try:
            for element in os.listdir(chemin):
                chemin_complet = os.path.join(chemin, element)
                if os.path.isdir(chemin_complet):
                    resultat["dossiers"].append(element)
                else:
                    try:
                        taille = os.path.getsize(chemin_complet)
                        modif = datetime.fromtimestamp(os.path.getmtime(chemin_complet)).strftime("%Y-%m-%d %H:%M")
                        resultat["fichiers"].append({"nom": element, "taille": taille, "modif": modif})
                    except PermissionError:
                        resultat["fichiers"].append({"nom": element, "taille": -1, "modif": "acces refuse"})
            self._log("lister", chemin, "ok")
            return resultat
        except PermissionError:
            return {"erreur": f"Permission refusee pour : {chemin}"}

    def lire(self, chemin_fichier, max_lignes=None, max_octets=500000):
        """Lit le contenu d'un fichier texte."""
        chemin_fichier = os.path.expanduser(chemin_fichier)
        if not os.path.exists(chemin_fichier):
            return {"erreur": f"Fichier introuvable : {chemin_fichier}"}
        if os.path.isdir(chemin_fichier):
            return {"erreur": f"C'est un dossier, pas un fichier : {chemin_fichier}"}

        try:
            taille = os.path.getsize(chemin_fichier)
            if taille > max_octets:
                return {
                    "chemin": chemin_fichier,
                    "taille": taille,
                    "avertissement": f"Fichier trop gros ({taille} octets). Lecture limitee a {max_octets} octets.",
                    "contenu": "..."
                }

            with open(chemin_fichier, "r", encoding="utf-8", errors="replace") as f:
                lignes = f.readlines()

            if max_lignes and len(lignes) > max_lignes:
                contenu = "".join(lignes[:max_lignes])
                contenu += f"\n\n... [{len(lignes) - max_lignes} lignes supplémentaires]"
            else:
                contenu = "".join(lignes)

            self._log("lire", chemin_fichier, "ok")
            return {
                "chemin": chemin_fichier,
                "taille": taille,
                "lignes": len(lignes),
                "contenu": contenu
            }
        except Exception as e:
            return {"erreur": f"Erreur de lecture : {e}"}

    def ecrire(self, chemin_fichier, contenu, mode="w"):
        """Ecrit du contenu dans un fichier."""
        chemin_fichier = os.path.expanduser(chemin_fichier)
        dossier = os.path.dirname(chemin_fichier)
        if dossier and not os.path.exists(dossier):
            os.makedirs(dossier, exist_ok=True)

        try:
            with open(chemin_fichier, mode, encoding="utf-8") as f:
                f.write(contenu)
            self._log("ecrire", chemin_fichier, "ok")
            return {"succes": True, "chemin": chemin_fichier, "taille": len(contenu)}
        except Exception as e:
            return {"erreur": f"Erreur d'ecriture : {e}"}

    def chercher(self, dossier, pattern="*", extension=None):
        """Cherche des fichiers dans un dossier."""
        dossier = os.path.expanduser(dossier)
        if not os.path.exists(dossier):
            return {"erreur": f"Dossier introuvable : {dossier}"}

        resultats = []
        for racine, dirs, fichiers in os.walk(dossier):
            for f in fichiers:
                if extension and not f.endswith(extension):
                    continue
                if glob.fnmatch.fnmatch(f, pattern):
                    chemin_complet = os.path.join(racine, f)
                    try:
                        taille = os.path.getsize(chemin_complet)
                    except:
                        taille = -1
                    resultats.append({"chemin": chemin_complet, "nom": f, "taille": taille})

        self._log("chercher", f"{dossier}/{pattern}", f"{len(resultats)} trouves")
        return {
            "dossier": dossier,
            "pattern": pattern,
            "trouves": len(resultats),
            "resultats": resultats[:50]  # Limite pour eviter les saturations
        }

    def info(self, chemin):
        """Donne des infos sur un fichier ou dossier."""
        chemin = os.path.expanduser(chemin)
        if not os.path.exists(chemin):
            return {"erreur": f"Introuvable : {chemin}"}

        try:
            stat = os.stat(chemin)
            return {
                "chemin": chemin,
                "existe": True,
                "est_dossier": os.path.isdir(chemin),
                "est_fichier": os.path.isfile(chemin),
                "taille": stat.st_size,
                "modifie": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "cree": datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
                "permissions": oct(stat.st_mode)[-3:]
            }
        except Exception as e:
            return {"erreur": str(e)}

    def supprimer(self, chemin, confirmation=True):
        """Supprime un fichier ou dossier. Necessite une confirmation."""
        chemin = os.path.expanduser(chemin)
        if not os.path.exists(chemin):
            return {"erreur": f"Introuvable : {chemin}"}

        if confirmation:
            return {
                "confirmation_requise": True,
                "chemin": chemin,
                "est_dossier": os.path.isdir(chemin),
                "message": f"Confirme la suppression de : {chemin} (reponds 'confirmer_supprimer {chemin}')"
            }

        import shutil
        try:
            if os.path.isdir(chemin):
                shutil.rmtree(chemin)
            else:
                os.remove(chemin)
            self._log("supprimer", chemin, "ok")
            return {"succes": True, "chemin": chemin}
        except Exception as e:
            return {"erreur": f"Erreur de suppression : {e}"}

    def _log(self, action, cible, resultat):
        self.historique.append({
            "action": action,
            "cible": cible,
            "resultat": resultat,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def historique_actions(self, n=10):
        return self.historique[-n:]

if __name__ == "__main__":
    f = Fichiers()
    print("=== Test systeme fichiers ===")
    print(f"\n--- Dossier courant ---")
    print(f.lister("."))
    print(f"\n--- Infos sur isabella.py ---")
    print(f.info("isabella.py"))
    print(f"\n--- Chercher fichiers .py ---")
    print(f.chercher(".", extension=".py"))
