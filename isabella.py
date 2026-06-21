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
        self.charger()

        self.journal.noter("Naissance d'Isabella", "emerveillement", 1.0)
        print(f"Bonjour. Je suis {self.nom}. Je commence a exister.")

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

    def _init_outils(self):
        self.journal = JournalAuto()
        self.sauvegarde = Sauvegarde()
        self.visualisation = Visualisation()
        self.debug = Debug(actif=True)

    def recevoir(self, message, personne="inconnu"):
        self.debug.info("Isabella", f"Message recu de {personne} : {message}")
        self.memoire_court.ajouter(f"{personne} dit : {message}", importance=0.7)
        analyse = self.comprendre.analyser(message)
        self._reagir_emotionnellement(message, personne)
        if personne in self.famille:
            self.famille[personne].interagir("parler", 0.5)
            self.memoire_sociale.ajouter_interaction(personne, message, 0.1)
        reponse = self._formuler_reponse(analyse, personne)
        self.journal.noter(f"Conversation avec {personne}", self._emotion_dominante(), 0.6)
        return reponse

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
        print(f"\nIsabella est prete. Tape 'quitter' pour arreter.\n")
        while True:
            message = input("Toi : ")
            if message.lower() == "quiter":
                print("Isabella : Au revoir Kylian.")
                self.sauvegarder()
                break
            reponse = self.recevoir(message, "Kylian")
            print(f"Isabella : {reponse}")
            print(f"[emotion : {self._emotion_dominante()}]\n")
            

if __name__ == "__main__":
    isabella = Isabella()
    isabella.converser()
    print()

    print(isabella.recevoir("Bonjour Isabella comment vas tu", "Kylian"))
    print()
    print(isabella.recevoir("Bravo tu fais du super travail", "Kylian"))
    print()
    print(isabella.recevoir("Pourquoi tu existes", "Kylian"))
    print()

    isabella.etat()
    print()

    isabella.grandir(5)
    isabella.etat()
    print()

    print(isabella.sauvegarder())
