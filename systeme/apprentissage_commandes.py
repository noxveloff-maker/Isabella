import json
import os
from datetime import datetime
from collections import Counter, defaultdict

class ApprentissageCommandes:
    """
    Apprend les commandes de l'utilisateur, compte les frequences,
    et suggere les plus utilisees. Peut creer des scripts automatiquement.
    """

    def __init__(self, fichier="apprentissage_commandes.json"):
        self.fichier = fichier
        self.commandes = {}  # texte -> {compteur, dernier_usage, contexte, script_associe}
        self.sequences = defaultdict(list)  # action -> [actions suivantes]
        self._charger()

    def _charger(self):
        if os.path.exists(self.fichier):
            with open(self.fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.commandes = data.get("commandes", {})
                self.sequences = defaultdict(list, data.get("sequences", {}))

    def _sauvegarder(self):
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump({
                "commandes": self.commandes,
                "sequences": dict(self.sequences),
                "dernier_export": datetime.now().strftime("%Y-%m-%d %H:%M")
            }, f, ensure_ascii=False, indent=2)

    def enregistrer(self, texte, action_detectee=None, resultat=None, creer_script=False):
        """
        Enregistre une commande utilisateur.
        Si elle est suffisamment frequente, propose de creer un script.
        """
        texte_normalise = self._normaliser(texte)

        if texte_normalise not in self.commandes:
            self.commandes[texte_normalise] = {
                "texte_original": texte,
                "compteur": 0,
                "dernier_usage": None,
                "premier_usage": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "action_detectee": action_detectee,
                "script_associe": None,
                "contextes": []
            }

        cmd = self.commandes[texte_normalise]
        cmd["compteur"] += 1
        cmd["dernier_usage"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        if action_detectee:
            cmd["action_detectee"] = action_detectee
        if resultat:
            cmd["contextes"].append({
                "date": datetime.now().strftime("%H:%M:%S"),
                "resultat": str(resultat)[:200]
            })
            # Garde seulement les 5 derniers contextes
            cmd["contextes"] = cmd["contextes"][-5:]

        self._sauvegarder()

        # Si assez frequent, propose la creation d'un script
        if creer_script and cmd["compteur"] >= 3 and not cmd["script_associe"]:
            return {
                "proposition_script": True,
                "texte": texte_normalise,
                "compteur": cmd["compteur"],
                "message": f"Tu as utilise cette commande {cmd['compteur']} fois. Veux-tu que je cree un script '{texte_normalise[:20]}' ?"
            }

        return {"compteur": cmd["compteur"]}

    def enregistrer_sequence(self, action1, action2):
        """Apprend que apres action1, on fait souvent action2."""
        self.sequences[action1].append(action2)
        self._sauvegarder()

    def suggestions(self, n=5, prefixe=None):
        """Suggere les N commandes les plus utilisees."""
        # Trie par compteur decroissant
        triees = sorted(self.commandes.items(), key=lambda x: x[1]["compteur"], reverse=True)

        if prefixe:
            prefixe = prefixe.lower()
            triees = [(t, c) for t, c in triees if prefixe in t.lower()]

        return [
            {
                "texte": c["texte_original"],
                "compteur": c["compteur"],
                "dernier_usage": c["dernier_usage"],
                "script": c["script_associe"]
            }
            for t, c in triees[:n]
        ]

    def suggestion_prochaine_action(self, action_precedente):
        """Suggere la prochaine action la plus probable apres une action."""
        suivantes = self.sequences.get(action_precedente, [])
        if not suivantes:
            return None
        compteur = Counter(suivantes)
        plus_frequent = compteur.most_common(1)[0]
        return {
            "action": plus_frequent[0],
            "probabilite": plus_frequent[1] / len(suivantes),
            "occurrences": plus_frequent[1]
        }

    def lier_script(self, texte_commande, nom_script):
        """Lie une commande frequente a un script."""
        texte_normalise = self._normaliser(texte_commande)
        if texte_normalise in self.commandes:
            self.commandes[texte_normalise]["script_associe"] = nom_script
            self._sauvegarder()
            return {"succes": True}
        return {"erreur": "Commande non trouvee"}

    def _normaliser(self, texte):
        """Normalise un texte pour le stockage."""
        # Enleve les articles, mots vides, etc.
        mots_inutiles = ["le", "la", "les", "de", "du", "des", "un", "une", "mon", "ma", "mes", "ton", "ta", "tes", "ce", "cette", "cet", "et", "ou", "dans", "sur", "pour", "avec", "par"]
        mots = texte.lower().split()
        mots_filtres = [m for m in mots if m not in mots_inutiles]
        return " ".join(mots_filtres)

    def stats(self):
        """Statistiques globales."""
        total = sum(c["compteur"] for c in self.commandes.values())
        unique = len(self.commandes)
        avec_script = sum(1 for c in self.commandes.values() if c["script_associe"])
        return {
            "total_executions": total,
            "commandes_uniques": unique,
            "commandes_avec_script": avec_script,
            "commandes_sans_script": unique - avec_script
        }

    def exporter_scripts_proposables(self, min_compteur=3):
        """Liste les commandes qui meriteraient un script."""
        return [
            {
                "texte": c["texte_original"],
                "compteur": c["compteur"],
                "action": c["action_detectee"]
            }
            for t, c in self.commandes.items()
            if c["compteur"] >= min_compteur and not c["script_associe"]
        ]

if __name__ == "__main__":
    a = ApprentissageCommandes()
    print("=== Test Apprentissage ===")

    # Simule des usages
    for _ in range(5):
        a.enregistrer("ouvre youtube et cherche ninjaxx", action_detectee="navigateur_url")
    a.enregistrer("ouvre youtube et cherche ninjaxx", action_detectee="navigateur_url", creer_script=True)

    a.enregistrer("liste les fichiers", action_detectee="fichiers_lister")
    a.enregistrer("liste les fichiers", action_detectee="fichiers_lister")

    a.enregistrer("capture l'ecran", action_detectee="ecran_capture")

    print("\nSuggestions :")
    for s in a.suggestions():
        print(f"  '{s['texte']}' — utilisee {s['compteur']} fois")

    print("\nStats :", a.stats())
    print("\nScripts proposables :", a.exporter_scripts_proposables())
