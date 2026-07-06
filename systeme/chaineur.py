import time
import re

class Chaineur:
    """
    Decompose une phrase complexe en une sequence d'actions executables.
    Gere les delais entre les etapes et les dependances.
    """

    # Mots de liaison qui separent des etapes
    SEPARATEURS = [" et ", " puis ", " ensuite ", " apres ", " apres ca ", " puis apres ", ","]

    def __init__(self, orchestrateur, delais=None):
        self.orchestrateur = orchestrateur
        self.delais = delais or {
            "navigateur_url": 2.0,      # Attendre que le site charge
            "recherche": 1.0,            # Attendre que la recherche s'affiche
            "clic": 0.5,               # Delai entre clic et action suivante
            "taper": 0.3,              # Delai apres frappe
            "lancer": 2.0,             # Attendre que l'app demarre
            "capture": 0.5,            # Delai apres capture
            "default": 0.5             # Delai par defaut
        }

    def decomposer(self, phrase):
        """
        Decompose une phrase en une liste d'instructions.
        Ex: "ouvre youtube et cherche ninjaxx" ->
            [
                {action: "url", module: "navigateur", parametres: {url: "youtube.com"}},
                {action: "recherche", module: "navigateur", parametres: {requete: "ninjaxx"}}
            ]
        """
        # Detecte d'abord si c'est un script connu
        # Ensuite decompose par mots de liaison
        etapes = self._split_phrase(phrase)
        actions = []
        for etape in etapes:
            instruction = self.orchestrateur.analyser_commande(etape)
            if instruction.get("action") not in ["inconnu", "info"]:
                actions.append(instruction)
        return actions

    def _split_phrase(self, phrase):
        """Separe une phrase en etapes par les mots de liaison."""
        phrase = phrase.lower().strip()
        # Remplace les separateurs par un marqueur unique
        for sep in self.SEPARATEURS:
            phrase = phrase.replace(sep, "||SEP||")
        etapes = [e.strip() for e in phrase.split("||SEP||") if e.strip()]
        return etapes

    def executer_sequence(self, phrase, mode_rapide=False):
        """
        Execute une sequence d'actions avec les delais appropriés.
        Retourne les resultats de chaque etape.
        """
        actions = self.decomposer(phrase)
        if not actions:
            return {"erreur": "Aucune action detectee dans la phrase", "phrase": phrase}

        resultats = []
        for i, action in enumerate(actions):
            resultat = self.orchestrateur.executer(action)
            resultats.append({
                "etape": i + 1,
                "action": action,
                "resultat": resultat
            })

            # Si erreur et pas de confirmation requise, on arrete
            if resultat.get("erreur") and not resultat.get("confirmation_requise"):
                break

            # Delai entre les actions (sauf la derniere)
            if not mode_rapide and i < len(actions) - 1:
                delai = self._calculer_delai(action)
                if delai > 0:
                    time.sleep(delai)

        return {
            "succes": True,
            "phrase": phrase,
            "etapes_totales": len(actions),
            "etapes_executees": len(resultats),
            "resultats": resultats
        }

    def _calculer_delai(self, action):
        """Calcule le delai necessaire apres une action."""
        module = action.get("module", "")
        action_nom = action.get("action", "")
        cle = f"{module}_{action_nom}"
        return self.delais.get(cle, self.delais.get("default", 0.5))

    def creer_script_depuis_phrase(self, phrase, nom_script, description, scripts_manager):
        """
        Cree un script a partir d'une phrase complexe.
        """
        actions = self.decomposer(phrase)
        if not actions:
            return {"erreur": "Impossible de creer un script — aucune action detectee"}

        return scripts_manager.creer(nom_script, description, actions)

    def ajouter_delai(self, action_nom, secondes):
        """Personnalise le delai pour une action specifique."""
        self.delais[action_nom] = secondes

    def lister_delais(self):
        """Liste les delais configures."""
        return self.delais.copy()

if __name__ == "__main__":
    from systeme.orchestrateur import Orchestrateur
    from systeme.fichiers import Fichiers
    from systeme.terminal import Terminal
    from systeme.ecran import Ecran
    from systeme.controle import Controle
    from systeme.navigateur import Navigateur

    o = Orchestrateur(Fichiers(), Terminal(), Ecran(), Controle(), Navigateur())
    c = Chaineur(o)

    print("=== Test Chaineur ===")
    tests = [
        "ouvre youtube et cherche ninjaxx",
        "liste le dossier . puis lis le fichier isabella.py",
        "capture l'ecran puis ouvre google.com"
    ]
    for phrase in tests:
        print(f"\n>>> {phrase}")
        actions = c.decomposer(phrase)
        print(f"Actions : {len(actions)}")
        for a in actions:
            print(f"  - {a['module']}.{a['action']}")
