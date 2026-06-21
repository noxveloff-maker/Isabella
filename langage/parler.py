class Parler:
    def __init__(self):
        self.historique = []
        self.ton = "neutre"

    def definir_ton(self, ton):
        self.ton = ton

    def formuler(self, message, emotion=None):
        if emotion == "joie":
            reponse = f"*avec enthousiasme* {message}"
        elif emotion == "tristesse":
            reponse = f"*doucement* {message}"
        elif emotion == "peur":
            reponse = f"*hesitante* {message}"
        elif emotion == "colere":
            reponse = f"*fermement* {message}"
        else:
            reponse = message
        self.historique.append({"message": message, "emotion": emotion, "reponse": reponse})
        return reponse

    def afficher(self):
        print(f"Historique des prises de parole : {len(self.historique)}")
        for h in self.historique:
            print(f" {h['reponse']}")

if __name__ == "__main__":
    p = Parler()
    print(p.formuler("Bonjour Kylian", "joie"))
    print(p.formuler("Je ne comprends pas", "confusion"))
    print(p.formuler("Je suis la", None))
    p.afficher()
