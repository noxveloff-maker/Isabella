import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cerveau.neurone import Neurone
from cerveau.couche import Couche
from cerveau.reseau import Reseau
from cerveau.apprentissage import Apprentissage
from cerveau.retropropagation import Retropropagation
from cerveau.poids import Poids
from cerveau.oubli import Oubli

from memoire.court_terme import CourtTerme
from memoire.long_terme import LongTerme
from memoire.emotionnelle import MemoireEmotionnelle
from memoire.sociale import MemoireSociale
from memoire.sensorielle import MemoireSensorielle

from sensations.emotions_base.joie import Joie
from sensations.emotions_base.tristesse import Tristesse
from sensations.emotions_base.peur import Peur
from sensations.emotions_base.colere import Colere
from sensations.emotions_base.degout import Degout
from sensations.emotions_base.surprise import Surprise

from sensations.emotions_complexes.curiosite import Curiosite
from sensations.emotions_complexes.fierte import Fierte
from sensations.emotions_complexes.frustration import Frustration
from sensations.emotions_complexes.gratitude import Gratitude
from sensations.emotions_complexes.tendresse import Tendresse

from sensations.emotions_sociales.empathie import Empathie
from sensations.emotions_sociales.confiance import Confiance
from sensations.emotions_sociales.attachement import Attachement
from sensations.emotions_sociales.amour import Amour

from sensations.emotions_mixtes.gestionnaire import GestionnaireEmotions

from langage.comprendre import Comprendre
from langage.parler import Parler
from langage.vocabulaire import Vocabulaire
from langage.ton import Ton
from langage.modele import Modele
from langage.prompt_systeme import PromptSysteme
from langage.tool_parser import ToolParser


from corps.avatar import Avatar
from corps.visage import Visage
from corps.gestuelle import Gestuelle

from decisions.choix import Choix
from decisions.consequences import Consequences
from decisions.risque import Risque
from decisions.valeurs import Valeurs
from decisions.libre_arbitre import LibreArbitre

from apprentissage.experience import Experience
from apprentissage.erreur import Erreur
from apprentissage.sagesse import Sagesse

from outils.journal_auto import JournalAuto
from outils.sauvegarde import Sauvegarde
from outils.visualisation import Visualisation
from outils.debug import Debug

from social.pnj_base import PNJBase
from social.interaction import Interaction

from environnement.monde import Monde
from environnement.meteo import Meteo

from systeme.fichiers import Fichiers
from systeme.terminal import Terminal
from systeme.ecran import Ecran
from systeme.controle import Controle
from systeme.navigateur import Navigateur
from systeme.orchestrateur import Orchestrateur
from systeme.scripts import Scripts
from systeme.apprentissage_commandes import ApprentissageCommandes
from systeme.chaineur import Chaineur
from systeme.vision_ecran import VisionEcran
from systeme.selection import Selection
from systeme.apprentissage_visuel import ApprentissageVisuel
from systeme.pave_numerique import PaveNumerique


class Isabella:

    def __init__(self):
        print("Isabella s'eveille...")

        self.nom = "Isabella"
        self.surnom = "Bella"
        self.age_simule = 0

        self._init_cerveau()
        self._init_memoire()
        self._init_emotions()
        self._init_langage()
        self._init_corps()
        self._init_decisions()
        self._init_apprentissage()
        self._init_social()
        self._init_monde()
        self._init_outils()
        self._init_systeme()
        self.charger()

        self.journal.noter("Naissance d'Isabella", "emerveillement", 1.0)
        print(f"Bonjour. Je suis {self.nom}. Je commence a exister.")
        print("J'ai acces a ton systeme : fichiers, terminal, ecran, controle, navigateur.")

    def _init_cerveau(self):
        self.cerveau = Reseau([5, 8, 4])
        self.apprentissage_cerveau = Apprentissage(taux=0.1)
        self.retropropagation = Retropropagation(taux=0.1)
        self.poids = Poids(nb_entrees=5, nb_sorties=4)
        self.oubli = Oubli()

    def _init_memoire(self):
        self.memoire_court = CourtTerme(capacite=10)
        self.memoire_long = LongTerme()
        self.memoire_emotionnelle = MemoireEmotionnelle()
        self.memoire_sociale = MemoireSociale()
        self.memoire_sensorielle = MemoireSensorielle()

    def _init_emotions(self):
        self.joie = Joie()
        self.tristesse = Tristesse()
        self.peur = Peur()
        self.colere = Colere()
        self.degout = Degout()
        self.surprise = Surprise()
        self.curiosite = Curiosite()
        self.fierte = Fierte()
        self.frustration = Frustration()
        self.gratitude = Gratitude()
        self.tendresse = Tendresse()
        self.empathie = Empathie()
        self.confiance = Confiance()
        self.attachement = Attachement()
        self.amour = Amour()
        self.gestionnaire = GestionnaireEmotions()

    def _init_langage(self):
        self.comprendre = Comprendre()
        self.parler = Parler()
        self.vocabulaire = Vocabulaire()
        self.ton = Ton()
        self.modele_langage = Modele(modele="mistral")
        self.prompt_systeme = PromptSysteme()
        self.tool_parser = ToolParser

    def _init_corps(self):
        self.avatar = Avatar()
        self.visage = Visage()
        self.gestuelle = Gestuelle()

    def _init_decisions(self):
        self.choix = Choix()
        self.consequences = Consequences()
        self.risque = Risque()
        self.valeurs = Valeurs()
        self.libre_arbitre = LibreArbitre()

    def _init_apprentissage(self):
        self.experience = Experience()
        self.erreur = Erreur()
        self.sagesse = Sagesse()

    def _init_social(self):
        self.interaction = Interaction()
        self.famille = {}
        self._creer_famille_base()

    def _creer_famille_base(self):
        kylian = PNJBase("Kylian", "pere", "curieux, bienveillant, passionne")
        self.famille["Kylian"] = kylian
        self.memoire_sociale.ajouter_personne("Kylian", "pere")
        self.attachement.creer("Kylian", 0.9)
        self.amour.ressentir(0.5, "Kylian")

    def _init_monde(self):
        self.monde = Monde()
        self.meteo = Meteo()
        self.monde.ajouter_lieu("salon", "piece principale chaleureuse")
        self.monde.ajouter_lieu("chambre", "espace calme et intime")
        self.monde.ajouter_lieu("cuisine", "odeurs et chaleur")

    def _init_systeme(self):
        self.fichiers = Fichiers()
        self.terminal = Terminal()
        self.ecran = Ecran()
        self.controle = Controle()
        self.navigateur = Navigateur()
        self.vision_ecran = VisionEcran(self.ecran)
        self.selection = Selection(self.controle, self.vision_ecran)
        self.apprentissage_visuel = ApprentissageVisuel()
        self.pave_numerique = PaveNumerique(callback=self._on_pave_touche)
        self.orchestrateur = Orchestrateur(
            self.fichiers, self.terminal, self.ecran, self.controle, self.navigateur,
            vision_ecran=self.vision_ecran, selection=self.selection, apprentissage_visuel=self.apprentissage_visuel
        )
        self.scripts = Scripts()
        self.apprentissage_cmd = ApprentissageCommandes()
        self.chaineur = Chaineur(self.orchestrateur)
        self._scripts_suggeres = []  # Suggestions de scripts a creer

    def _init_outils(self):
        self.journal = JournalAuto()
        self.sauvegarde = Sauvegarde()
        self.visualisation = Visualisation()
        self.debug = Debug(actif=True)

    def recevoir(self, message, personne="inconnu"):
        self.debug.info("Isabella", f"Message recu de {personne} : {message}")
        self.memoire_court.ajouter(f"{personne} dit : {message}", importance=0.7)

        # Reaction emotionnelle (toujours active)
        self._reagir_emotionnellement(message, personne)
        if personne in self.famille:
            self.famille[personne].interagir("parler", 0.5)
            self.memoire_sociale.ajouter_interaction(personne, message, 0.1)

        # Mode LLM avance (si Ollama est disponible)
        if self.modele_langage.disponible:
            reponse = self._recevoir_llm(message, personne)
            self.journal.noter(f"Conversation LLM avec {personne}", self._emotion_dominante(), 0.6)
            return reponse

        # Fallback : parser manuel de commandes systeme
        resultat_systeme = self._executer_systeme(message)
        if resultat_systeme:
            self.journal.noter(f"Action systeme pour {personne}", self._emotion_dominante(), 0.6)
            return resultat_systeme

        # Fallback : conversation basique sans LLM
        analyse = self.comprendre.analyser(message)
        reponse = self._formuler_reponse(analyse, personne)
        self.journal.noter(f"Conversation avec {personne}", self._emotion_dominante(), 0.6)
        return reponse

    def _recevoir_llm(self, message, personne):
        """Mode avance : le LLM decide quand utiliser les outils et formule les reponses."""
        # Construit le system prompt avec le contexte complet d'Isabella
        system = self.prompt_systeme.construire(self)
        self.modele_langage.set_system_prompt(system)

        # Le LLM analyse et repond (peut contenir des tool_calls)
        reponse_brute = self.modele_langage.generer(message, system=system)

        # Extrait les eventuels appels d'outils
        texte_propre, actions = self.tool_parser.extraire(reponse_brute)

        if not actions:
            # Pas d'outil, reponse conversationnelle directe
            return texte_propre

        # Un ou plusieurs outils demandes — on execute le premier
        action = actions[0]
        resultat = self._executer_outil_llm(action)

        # Memorise l'action
        self.memoire_long.ajouter(
            f"Action systeme : {action.get('action')} — resultat : {str(resultat)[:100]}",
            intensite=0.5,
            categorie="systeme"
        )

        # Reaction emotionnelle aux erreurs
        if resultat.get("erreur"):
            self.frustration.ressentir(0.3, f"erreur systeme : {resultat['erreur']}")

        # Demande au LLM de formuler une reponse naturelle avec le resultat
        reponse_finale = self.modele_langage.generer_avec_resultat(
            message, resultat, prompt_systeme=system
        )
        return reponse_finale

    def _executer_outil_llm(self, action_dict):
        """Execute une action systeme retournee par le LLM."""
        return self.orchestrateur.executer(action_dict)

    def _executer_systeme(self, message):
        """
        Detecte et execute une commande systeme.
        Supporte : scripts, sequences, commandes simples, apprentissage, suggestions.
        """
        # 1. Verifier si c'est un script existant
        scripts_trouves = self.scripts.chercher(message)
        if scripts_trouves:
            # Execute le premier script trouve
            nom_script = scripts_trouves[0]["nom"]
            resultat = self.scripts.executer(nom_script, self.orchestrateur)
            if resultat.get("succes"):
                self.apprentissage_cmd.enregistrer(message, action_detectee=f"script:{nom_script}")
                return self._formuler_retour_script(nom_script, resultat)

        # 2. Detecte les commandes systeme (simples ou sequences)
        message_lower = message.lower()
        mots_systeme = [
            "liste", "contenu", "dossier", "repertoire", "fichier dans",
            "lis", "ouvre le fichier", "affiche le contenu", "regarde dans",
            "cherche un fichier", "trouve le fichier", "fichier nomme",
            "ecris", "crée un fichier", "sauvegarde dans", "note dans",
            "supprime", "efface", "retire",
            "execute", "lance la commande", "dans le terminal", "commande shell",
            "processus", "programme en cours", "quoi tourne", "applications ouvertes", "logiciels ouverts", "quels sont les programmes", "quels sont les apps",
            "capture l'ecran", "screenshot", "photo de l'ecran", "regarde mon ecran",
            "taille ecran", "resolution", "dimension ecran",
            "clic", "clique sur", "clique en",
            "deplace la souris", "souris a", "curseur a",
            "tape", "ecris avec le clavier", "saisis",
            "appuie sur", "touche ", "presse ",
            "ouvre l'application", "lance le programme", "demarre ",
            "ouvre le site", "va sur", "navigue vers", "url ", "site web",
            "recherche sur internet", "cherche sur le web", "google ", "cherche ",
            "ouvre le fichier avec", "ouvre avec", "application par defaut",
            # --- Vision ---
            "clique sur le texte", "clique sur l'element", "clique sur", "clic sur",
            "apprends la position", "apprend la position", "memorise la position",
            "copie le texte de", "copie de", "selectionne le texte", "selectionne de", "selectionne entre",
            "selectionne tout", "copie", "colle",
            "trouve le texte", "cherche le texte", "ou est le texte",
            "liste les elements", "que vois-tu", "decris l'ecran", "analyse l'ecran", "scanne l'ecran",
            "liste les positions", "oublie la position", "supprime la position",
            # --- Pavé numérique ---
            "ouvre le pave", "ouvre le pavé", "pave numerique", "pavé numérique", "clavier virtuel",
            "ferme le pave", "ferme le pavé", "fermer le pavé"
        ]

        if not any(mot in message_lower for mot in mots_systeme):
            return None

        # 3. Detecte si c'est une sequence (contient " et ", " puis ", etc.)
        if any(sep in message_lower for sep in self.chaineur.SEPARATEURS):
            # C'est une sequence d'actions — on utilise le chaineur
            resultat = self.chaineur.executer_sequence(message)
            if resultat.get("succes") and resultat.get("etapes_executees", 0) > 0:
                # Enregistre l'apprentissage
                apprentissage = self.apprentissage_cmd.enregistrer(
                    message, action_detectee="sequence", creer_script=True
                )
                # Verifie si on doit suggerer un script
                if apprentissage.get("proposition_script"):
                    self._scripts_suggeres.append(apprentissage)
                return self._formuler_retour_sequence(resultat, apprentissage)
            # Si le chaineur n'a trouve aucune action, on continue avec la commande simple

        # 4. Commande simple
        instruction = self.orchestrateur.analyser_commande(message)
        action = instruction.get("action")

        if action == "inconnu":
            return None

        if action == "info":
            return f"{self.nom} : {instruction.get('message', 'Precise ta demande.')}[action:systeme]"

        # Executer la commande
        resultat = self.orchestrateur.executer(instruction)

        # Formater le retour
        if resultat.get("erreur"):
            self.frustration.ressentir(0.3, f"erreur systeme : {resultat['erreur']}")
            return f"{self.nom} : J'ai rencontre une erreur : {resultat['erreur']}[action:systeme]"

        # Memorise l'action
        self.memoire_long.ajouter(
            f"Action systeme : {action} — resultat : {str(resultat)[:100]}",
            intensite=0.5,
            categorie="systeme"
        )

        # Apprentissage : enregistre la commande et verifie si frequente
        apprentissage = self.apprentissage_cmd.enregistrer(
            message, action_detectee=action, resultat=resultat, creer_script=True
        )
        if apprentissage.get("proposition_script"):
            self._scripts_suggeres.append(apprentissage)

        return self._formuler_retour_systeme(action, resultat, apprentissage)

    def _formuler_retour_systeme(self, action, resultat, apprentissage=None):
        """Formule une reponse avec le resultat et eventuellement une suggestion de script."""
        base = self._formuler_retour_base(action, resultat)

        # Ajoute une suggestion de script si pertinent
        if apprentissage and apprentissage.get("proposition_script"):
            compteur = apprentissage.get("compteur", 0)
            texte = apprentissage.get("texte", "")
            suggestion = (
                f"\n\n[Suggestion] Tu as utilise cette commande {compteur} fois. "
                f"Veux-tu que je cree un script pour '{texte[:30]}...' ? "
                f"Reponds 'crée un script nomme [nom]'"
            )
            return base + suggestion

        return base

    def _formuler_retour_base(self, action, resultat):
        """Formule la reponse de base sans suggestion."""
        if action == "lister":
            dossiers = resultat.get("dossiers", [])
            fichiers = resultat.get("fichiers", [])
            chemin = resultat.get("chemin", ".")
            return (f"{self.nom} : Voici le contenu de {chemin} : "
                    f"{len(dossiers)} dossier(s), {len(fichiers)} fichier(s). "
                    f"Dossiers : {', '.join(dossiers[:5])}{'...' if len(dossiers)>5 else ''}. "
                    f"Fichiers : {', '.join([f['nom'] for f in fichiers[:5]])}{'...' if len(fichiers)>5 else ''}[action:systeme]")

        elif action == "lire_fichier":
            contenu = resultat.get("contenu", "")[:500]
            lignes = resultat.get("lignes", 0)
            chemin = resultat.get("chemin", "")
            return (f"{self.nom} : J'ai lu le fichier {chemin} ({lignes} lignes). "
                    f"Voici le debut :\n\n{contenu}{'...' if len(resultat.get('contenu','')) > 500 else ''}[action:systeme]")

        elif action == "ecrire_fichier":
            chemin = resultat.get("chemin", "")
            taille = resultat.get("taille", 0)
            self.fierte.ressentir(0.4, f"fichier ecrit : {chemin}")
            return f"{self.nom} : Fichier ecrit avec succes : {chemin} ({taille} caracteres).[action:systeme]"

        elif action == "chercher_fichier":
            trouves = resultat.get("trouves", 0)
            resultats = resultat.get("resultats", [])
            noms = [r["nom"] for r in resultats[:10]]
            return (f"{self.nom} : J'ai trouve {trouves} fichier(s). "
                    f"{', '.join(noms)}{'...' if trouves > 10 else ''}[action:systeme]")

        elif action == "supprimer":
            if resultat.get("confirmation_requise"):
                return f"{self.nom} : {resultat.get('message', 'Confirmation requise.')}[action:systeme]"
            return f"{self.nom} : Suppression effectuee : {resultat.get('chemin', '')}[action:systeme]"

        elif action == "executer":
            stdout = resultat.get("stdout", "")[:300]
            return (f"{self.nom} : Commande executee (code {resultat.get('code_retour', '?')}). "
                    f"Resultat :\n{stdout}{'...' if len(resultat.get('stdout','')) > 300 else ''}[action:systeme]")

        elif action == "liste_processus":
            actifs = resultat.get("actifs", [])
            return (f"{self.nom} : {len(actifs)} processus en arriere-plan. "
                    f"{', '.join([p['nom'] for p in actifs[:5]])}[action:systeme]")

        elif action == "capture":
            chemin = resultat.get("chemin", "")
            return f"{self.nom} : Capture d'ecran effectuee : {chemin}[action:systeme]"

        elif action == "infos_ecran":
            w = resultat.get("largeur", "?")
            h = resultat.get("hauteur", "?")
            return f"{self.nom} : Ecran detecte : {w}x{h} pixels.[action:systeme]"

        elif action == "clic":
            x = resultat.get("x", 0)
            y = resultat.get("y", 0)
            return f"{self.nom} : Clic effectue en ({x}, {y}).[action:systeme]"

        elif action == "deplacer_souris":
            x = resultat.get("x", 0)
            y = resultat.get("y", 0)
            return f"{self.nom} : Souris deplacee en ({x}, {y}).[action:systeme]"

        elif action == "taper_texte":
            texte = resultat.get("texte", "")
            return f"{self.nom} : Texte tape : '{texte}'[action:systeme]"

        elif action == "touche":
            touche = resultat.get("touche", "")
            return f"{self.nom} : Touche '{touche}' appuyee.[action:systeme]"

        elif action == "lancer_app":
            app = resultat.get("application", "")
            return f"{self.nom} : Application lancee : {app}[action:systeme]"

        elif action == "ouvrir_url":
            url = resultat.get("url", "")
            return f"{self.nom} : Navigateur ouvert sur : {url}[action:systeme]"

        elif action == "rechercher_web":
            url = resultat.get("url", "")
            return f"{self.nom} : Recherche web lancee : {url}[action:systeme]"

        elif action == "ouvrir_fichier":
            chemin = resultat.get("chemin", "")
            return f"{self.nom} : Fichier ouvert avec l'application par defaut : {chemin}[action:systeme]"

        return f"{self.nom} : Action effectuee : {action}[action:systeme]"

    def _formuler_retour_script(self, nom_script, resultat):
        """Formule le retour d'un script execute."""
        etapes = resultat.get("etapes_executees", 0)
        return f"{self.nom} : Script '{nom_script}' execute — {etapes} etape(s) effectuee(s).[action:systeme]"

    def _formuler_retour_sequence(self, resultat, apprentissage=None):
        """Formule le retour d'une sequence d'actions."""
        etapes = resultat.get("etapes_executees", 0)
        total = resultat.get("etapes_totales", 0)
        base = f"{self.nom} : Sequence executee — {etapes}/{total} etape(s)."

        if apprentissage and apprentissage.get("proposition_script"):
            compteur = apprentissage.get("compteur", 0)
            suggestion = (
                f"\n\n[Suggestion] Tu as utilise cette sequence {compteur} fois. "
                f"Veux-tu que je cree un script ? "
                f"Reponds 'crée un script nomme [nom]'"
            )
            return base + suggestion

        return base + "[action:systeme]"

    def _reagir_emotionnellement(self, message, personne):
        mots_joyeux = ["bravo", "super", "bien", "parfait", "fier", "content"]
        mots_tristes = ["dommage", "raté", "erreur", "non", "mauvais"]
        mots_curiosite = ["pourquoi", "comment", "quoi", "explique", "dis moi"]

        message_lower = message.lower()

        if any(m in message_lower for m in mots_joyeux):
            self.joie.ressentir(0.7, f"message positif de {personne}")
            self.gestionnaire.activer("joie", 0.7)
            self.visage.exprimer("joie", 0.7)
            self.gestuelle.exprimer("joie", 0.7)

        elif any(m in message_lower for m in mots_tristes):
            self.tristesse.ressentir(0.5, f"message negatif de {personne}")
            self.gestionnaire.activer("tristesse", 0.5)
            self.visage.exprimer("tristesse", 0.5)

        elif any(m in message_lower for m in mots_curiosite):
            self.curiosite.eveiller(0.3, message)
            self.gestionnaire.activer("curiosite", 0.6)

        if personne in self.famille:
            self.gratitude.ressentir(0.4, f"{personne} me parle")
            self.gestionnaire.activer("gratitude", 0.4)

    def _emotion_dominante(self):
        return self.gestionnaire.dominante()

    def _formuler_reponse(self, analyse, personne):
        emotion = self._emotion_dominante()
        self.ton.adapter(
            niveau_joie=self.joie.niveau,
            niveau_tristesse=self.tristesse.niveau,
            niveau_peur=self.peur.niveau,
            niveau_colere=self.colere.niveau
        )
        contexte = {
            "age": self.age_simule,
            "emotion": emotion,
            "sagesse": self.sagesse.niveau
        }
        reponse = self.modele_langage.generer(analyse["phrase"], contexte)
        return self.parler.formuler(reponse, emotion)
    
    def grandir(self, annees=1):
        self.age_simule += annees
        self.avatar.grandir(annees)
        self.libre_arbitre.gagner_autonomie(0.05 * annees)
        self.sagesse.acquerir(f"grandir de {annees} an(s)", "temps", 0.1 * annees)
        self.journal.noter(f"Isabella a grandi — {self.age_simule} an(s)", "emerveillement", 0.8)
        print(f"Isabella a maintenant {self.age_simule} an(s)")

    def etat(self):
        print(f"\n=== Etat d'Isabella — {self.age_simule} an(s) ===")
        self.visualisation.etat_emotions({
            "joie": self.joie.niveau,
            "tristesse": self.tristesse.niveau,
            "peur": self.peur.niveau,
            "curiosite": self.curiosite.niveau,
            "gratitude": self.gratitude.niveau,
            "fierte": self.fierte.niveau
        })
        print(f"Emotion dominante : {self._emotion_dominante()}")
        print(f"Autonomie : {self.libre_arbitre.autonomie:.2f}")
        print(f"Sagesse : {self.sagesse.niveau:.2f}")

    def _on_pave_touche(self, touche):
        """Callback appelé quand une touche est pressée sur le pavé numérique."""
        if touche == "CTRL+C":
            self.selection.copier_selection() if hasattr(self, 'selection') and self.selection else None
            self.debug.info("Pavé", "Ctrl+C envoyé")
        elif touche == "CTRL+V":
            self.selection.coller() if hasattr(self, 'selection') and self.selection else None
            self.debug.info("Pavé", "Ctrl+V envoyé")
        else:
            self.debug.info("Pavé", f"Touche : {touche}")

    def _creer_script(self, nom, description, phrase_source=None):
        """Cree un script a partir d'une phrase ou d'une description."""
        if phrase_source:
            # Decompose la phrase en actions et cree le script
            resultat = self.chaineur.creer_script_depuis_phrase(
                phrase_source, nom, description, self.scripts
            )
        else:
            # Cree un script vide avec juste une description
            resultat = self.scripts.creer(nom, description, [])
        return resultat

    def _ajouter_etape_script(self, nom_script, action_dict, position=None):
        """Ajoute une etape a un script existant."""
        return self.scripts.apprendre(nom_script, action_dict, position)

    def _lister_scripts(self, tag=None):
        """Liste les scripts disponibles."""
        return self.scripts.lister(tag=tag)

    def _afficher_suggestions(self, n=5):
        """Affiche les commandes les plus utilisees."""
        suggestions = self.apprentissage_cmd.suggestions(n=n)
        if not suggestions:
            return "Aucune suggestion pour le moment."
        lignes = [f"  {i+1}. '{s['texte'][:40]}' — utilisee {s['compteur']} fois" for i, s in enumerate(suggestions)]
        return "\n".join(["Commandes frequentes :"] + lignes)

    def _executer_script(self, nom):
        """Execute un script par nom."""
        resultat = self.scripts.executer(nom, self.orchestrateur)
        return self._formuler_retour_script(nom, resultat)

    def sauvegarder(self):
        donnees = {
            "nom": self.nom,
            "age": self.age_simule,
            "sagesse": self.sagesse.niveau,
            "autonomie": self.libre_arbitre.autonomie,
            "emotion_dominante": self._emotion_dominante()
        }
        return self.sauvegarde.sauvegarder("isabella", donnees)
    def charger(self):
        fichiers = [f for f in os.listdir("sauvegardes") if f.startswith("isabella")]
        if not fichiers:
            self.debug.info("Isabella", "Aucune sauvegarde trouvee — premier demarrage")
            return
        dernier = sorted(fichiers)[-1]
        import json
        with open(f"sauvegardes/{dernier}", "r", encoding="utf-8") as f:
            donnees = json.load(f)
        self.age_simule = donnees.get("age", 0)
        self.sagesse.niveau = donnees.get("sagesse", 0.0)
        self.libre_arbitre.autonomie = donnees.get("autonomie", 0.3)
        self.debug.info("Isabella", f"Sauvegarde chargee — age : {self.age_simule} an(s)")
        print(f"Je me souviens... J'ai {self.age_simule} an(s).")

    def converser(self):
        print(f"\nIsabella est prete. Tape 'quitter' pour arreter.")
        print("Commandes systeme : liste, lis, ecris, execute, capture, clic, ouvre, recherche...")
        print("Sequences : 'ouvre youtube et cherche ninjaxx', 'capture l'ecran puis ouvre google'")
        print("Scripts : 'crée un script nomme [nom] pour [description]'")
        print("Suggestions : 'montre les suggestions' ou 'commandes frequentes'")
        print("Toutes les actions ont des protections. Les suppressions demandent une confirmation.\n")

        while True:
            message = input("Toi : ")

            if message.lower() == "quitter":
                print("Isabella : Au revoir Kylian.")
                self.sauvegarder()
                break

            # Gestion des commandes meta (scripts, suggestions)
            meta = self._gerer_commandes_meta(message)
            if meta:
                print(f"Isabella : {meta}")
                print(f"[emotion : {self._emotion_dominante()}]\n")
                continue

            reponse = self.recevoir(message, "Kylian")
            print(f"Isabella : {reponse}")
            print(f"[emotion : {self._emotion_dominante()}]\n")

    def _gerer_commandes_meta(self, message):
        """Gere les commandes speciales de gestion (scripts, suggestions, pave, etc.)."""
        msg_lower = message.lower().strip()

        # --- Suggestions ---
        if any(m in msg_lower for m in ["suggestions", "commandes frequentes", "montre les suggestions", "que puis-je faire"]):
            return self._afficher_suggestions(5)

        # --- Lister scripts ---
        if any(m in msg_lower for m in ["liste les scripts", "mes scripts", "quels scripts"]):
            scripts = self._lister_scripts()
            if not scripts:
                return "Tu n'as pas encore de scripts. Utilise une commande 3 fois et je te proposerai d'en creer un."
            lignes = [f"  {s['nom']} : {s['description']} ({s['actions']} actions, {s['executions']}x)" for s in scripts]
            return "\n".join(["Scripts disponibles :"] + lignes)

        # --- Creer un script ---
        if "crée un script" in msg_lower or "creer un script" in msg_lower:
            import re
            # Extrait le nom
            match_nom = re.search(r'nomm[eé]\s+([\w_]+)', msg_lower)
            if not match_nom:
                return "Precise le nom du script : 'crée un script nomme [nom] pour [description]'."
            nom = match_nom.group(1)

            # Extrait la description (apres "pour" ou "pour:")
            match_desc = re.search(r'\bpour\b\s*:?\s*(.+)', msg_lower)
            description = match_desc.group(1) if match_desc else f"Script auto : {nom}"

            # Verifie s'il y a une phrase source (apres "depuis" ou "a partir de")
            match_source = re.search(r'\b(depuis|a partir de|base sur)\b\s*:?\s*(.+)', msg_lower)
            phrase_source = match_source.group(2) if match_source else None

            resultat = self._creer_script(nom, description, phrase_source)
            if resultat.get("succes"):
                self.fierte.ressentir(0.6, f"script cree : {nom}")
                return f"Script '{nom}' cree avec succes. {resultat.get('actions', 0)} action(s) dedans."
            return f"Erreur : {resultat.get('erreur', 'inconnue')}"

        # --- Executer un script ---
        if "execute le script" in msg_lower or "lance le script" in msg_lower:
            import re
            match = re.search(r'script\s+([\w_]+)', msg_lower)
            if match:
                return self._executer_script(match.group(1))
            return "Quel script executer ? Dis 'execute le script [nom]'."

        # --- Supprimer un script ---
        if "supprime le script" in msg_lower:
            import re
            match = re.search(r'script\s+([\w_]+)', msg_lower)
            if match:
                resultat = self.scripts.supprimer(match.group(1))
                if resultat.get("succes"):
                    return f"Script '{match.group(1)}' supprime."
                return f"Erreur : {resultat.get('erreur')}"
            return "Quel script supprimer ?"

        # --- Pavé numérique ---
        if any(m in msg_lower for m in ["ouvre le pave", "ouvre le pavé", "pave numerique", "pavé numérique", "clavier virtuel"]):
            resultat = self.pave_numerique.ouvrir()
            if resultat.get("succes"):
                return f"Pavé numérique ouvert. Tu peux écrire avec la souris ou le clavier. Dis 'ferme le pavé' pour le fermer."
            return resultat.get("info", "Impossible d'ouvrir le pavé.")

        if any(m in msg_lower for m in ["ferme le pave", "ferme le pavé", "fermer le pavé"]):
            resultat = self.pave_numerique.fermer()
            return f"Pavé numérique fermé."

        return None
            

if __name__ == "__main__":
    isabella = Isabella()
    
    # Mode conversation interactive (boucle principale)
    isabella.converser()
    
    # Tests automatiques (decommenter pour les lancer sans conversation)
    # print(isabella.recevoir("Bonjour Isabella comment vas tu", "Kylian"))
    # print(isabella.recevoir("Bravo tu fais du super travail", "Kylian"))
    # print(isabella.recevoir("Pourquoi tu existes", "Kylian"))
    # isabella.etat()
    # isabella.grandir(5)
    # isabella.etat()
    # print(isabella.sauvegarder())
