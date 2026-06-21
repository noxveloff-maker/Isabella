class Ton:
    def __init__(self):
        self.ton_actuel = "neutre"
        self.historique = []

    def adapter(self, niveau_joie=0, niveau_tristesse=0, niveau_peur=0, niveau_colere=0):
        emotions = {
            "joyeux": niveau_joie,
            "triste": niveau_tristesse,
            "craintif": niveau_peur,
            "en colere": niveau_colere
        }
        dominant = max(emotions, key=emotions.get)
        if emotions[dominant] > 0.3:
            self.ton_actuel = dominant
        else:
            self.ton_actuel = "neutre"
        self.historique.append(self.ton_actuel)
        return self.ton_actuel

    def appliquer(self, message):
        prefixes = {
            "joyeux": "😊",
            "triste": "😔",
            "craintif": "😨",
            "en colere": "😠",
            "neutre": "🙂"
        }
        return f"{prefixes.get(self.ton_actuel, '')} {message}"

    def afficher(self):
        print(f"Ton actuel : {self.ton_actuel}")

if __name__ == "__main__":
    t = Ton()
    print(t.adapter(niveau_joie=0.8))
    print(t.appliquer("Bonjour Kylian"))
    print(t.adapter(niveau_tristesse=0.7))
    print(t.appliquer("Je me sens seule"))
    t.afficher()
