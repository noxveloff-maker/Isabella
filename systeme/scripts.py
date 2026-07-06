import json
import os
from datetime import datetime

class Scripts:
    """
    Stocke et gere des scripts/macro d'actions systeme.
    Chaque script est une sequence d'actions executables.
    """

    def __init__(self, dossier="scripts_isabella"):
        self.dossier = os.path.expanduser(f"~/{dossier}")
        os.makedirs(self.dossier, exist_ok=True)
        self.scripts = {}
        self._charger()

    def _fichier(self, nom):
        return os.path.join(self.dossier, f"{nom}.json")

    def _charger(self):
        """Charge tous les scripts existants."""
        for f in os.listdir(self.dossier):
            if f.endswith(".json"):
                chemin = os.path.join(self.dossier, f)
                try:
                    with open(chemin, "r", encoding="utf-8") as fichier:
                        nom = f[:-5]  # Retire .json
                        self.scripts[nom] = json.load(fichier)
                except:
                    pass

    def _sauvegarder(self, nom):
        """Sauvegarde un script."""
        if nom in self.scripts:
            with open(self._fichier(nom), "w", encoding="utf-8") as f:
                json.dump(self.scripts[nom], f, ensure_ascii=False, indent=2)

    def creer(self, nom, description, actions, tags=None):
        """
        Cree un nouveau script.
        actions = liste de dict [{action, module, parametres}, ...]
        """
        self.scripts[nom] = {
            "nom": nom,
            "description": description,
            "actions": actions,
            "tags": tags or [],
            "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "date_dernier_usage": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "nb_executions": 0,
            "nb_apprentissages": 0  # Combien de fois on lui a appris a l'ameliorer
        }
        self._sauvegarder(nom)
        return {"succes": True, "nom": nom, "actions": len(actions)}

    def executer(self, nom, orchestrateur):
        """Execute un script en utilisant l'orchestrateur."""
        if nom not in self.scripts:
            return {"erreur": f"Script '{nom}' inconnu"}

        script = self.scripts[nom]
        resultats = []
        for i, action in enumerate(script["actions"]):
            resultat = orchestrateur.executer(action)
            resultats.append({"etape": i, "action": action, "resultat": resultat})
            if resultat.get("erreur") and not resultat.get("confirmation_requise"):
                break

        script["nb_executions"] += 1
        script["date_dernier_usage"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._sauvegarder(nom)

        return {
            "succes": True,
            "nom": nom,
            "etapes_executees": len(resultats),
            "resultats": resultats
        }

    def apprendre(self, nom, nouvelle_action, position=None):
        """Ajoute une etape a un script existant (apprentissage)."""
        if nom not in self.scripts:
            return {"erreur": f"Script '{nom}' inconnu"}

        script = self.scripts[nom]
        if position is None:
            script["actions"].append(nouvelle_action)
        else:
            script["actions"].insert(position, nouvelle_action)

        script["nb_apprentissages"] += 1
        self._sauvegarder(nom)
        return {"succes": True, "nom": nom, "actions": len(script["actions"])}

    def modifier(self, nom, nouvelle_description=None, nouvelles_actions=None, nouveaux_tags=None):
        """Modifie completement un script."""
        if nom not in self.scripts:
            return {"erreur": f"Script '{nom}' inconnu"}

        script = self.scripts[nom]
        if nouvelle_description:
            script["description"] = nouvelle_description
        if nouvelles_actions:
            script["actions"] = nouvelles_actions
        if nouveaux_tags is not None:
            script["tags"] = nouveaux_tags

        self._sauvegarder(nom)
        return {"succes": True, "nom": nom}

    def supprimer(self, nom):
        """Supprime un script."""
        if nom not in self.scripts:
            return {"erreur": f"Script '{nom}' inconnu"}

        del self.scripts[nom]
        chemin = self._fichier(nom)
        if os.path.exists(chemin):
            os.remove(chemin)
        return {"succes": True, "nom": nom}

    def lister(self, tag=None):
        """Liste les scripts, filtres par tag optionnel."""
        resultats = []
        for nom, script in self.scripts.items():
            if tag and tag not in script.get("tags", []):
                continue
            resultats.append({
                "nom": nom,
                "description": script["description"],
                "tags": script.get("tags", []),
                "actions": len(script["actions"]),
                "executions": script["nb_executions"],
                "dernier_usage": script["date_dernier_usage"],
                "apprentissages": script["nb_apprentissages"]
            })
        return sorted(resultats, key=lambda x: x["executions"], reverse=True)

    def chercher(self, mot_cle):
        """Cherche un script par mot-cle dans le nom, description ou tags."""
        mot_cle = mot_cle.lower()
        resultats = []
        for nom, script in self.scripts.items():
            if (mot_cle in nom.lower() or
                mot_cle in script.get("description", "").lower() or
                any(mot_cle in t.lower() for t in script.get("tags", []))):
                resultats.append({
                    "nom": nom,
                    "description": script["description"],
                    "tags": script.get("tags", [])
                })
        return resultats

    def dupliquer(self, nom_original, nouveau_nom):
        """Duplique un script."""
        if nom_original not in self.scripts:
            return {"erreur": f"Script '{nom_original}' inconnu"}
        if nouveau_nom in self.scripts:
            return {"erreur": f"Script '{nouveau_nom}' existe deja"}

        script = self.scripts[nom_original].copy()
        script["nom"] = nouveau_nom
        script["date_creation"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        script["date_dernier_usage"] = script["date_creation"]
        script["nb_executions"] = 0
        script["nb_apprentissages"] = 0
        self.scripts[nouveau_nom] = script
        self._sauvegarder(nouveau_nom)
        return {"succes": True, "nom": nouveau_nom}

if __name__ == "__main__":
    s = Scripts()
    print("=== Test Scripts ===")
    
    # Creation d'un script "ouvrir_youtube_ninjaxx"
    s.creer("ouvrir_youtube_ninjaxx", 
             "Ouvre YouTube et cherche une video de Ninjaxx",
             [
                 {"action": "url", "module": "navigateur", "parametres": {"url": "https://youtube.com"}},
                 {"action": "recherche", "module": "navigateur", "parametres": {"requete": "Ninjaxx", "moteur": "youtube"}}
             ],
             tags=["youtube", "video", "ninjaxx"])
    
    print("Scripts crees :", s.lister())
    print("\nChercher 'youtube' :", s.chercher("youtube"))
    
    # Apprendre une nouvelle etape
    s.apprendre("ouvrir_youtube_ninjaxx", 
                {"action": "touche", "module": "controle", "parametres": {"touche": "Enter"}})
    
    print("\nApres apprentissage :")
    for script in s.lister():
        print(f"  {script['nom']} : {script['actions']} actions, {script['apprentissages']} apprentissages")
