from social.pnj_base import PNJBase

class MeilleurAmi(PNJBase):
    def __init__(self, nom):
        super().__init__(
            nom=nom,
            role="meilleur ami",
            personnalite="choisi par Isabella — reflete qui elle est devenue"
        )
        self.relation_isabella = 0.7
        self.secrets_partages = []

    def partager_secret(self, secret):
        self.secrets_partages.append(secret)
        self.relation_isabella = min(1.0, self.relation_isabella + 0.1)
        return f"Isabella confie a {self.nom} : {secret}"

    def soutenir(self, situation):
        self.relation_isabella = min(1.0, self.relation_isabella + 0.1)
        return f"{self.nom} soutient Isabella dans : {situation}"

    def trahir(self, raison):
        self.relation_isabella = max(0.0, self.relation_isabella - 0.4)
        return f"{self.nom} trahit Isabella — {raison} — quelque chose se brise"

    def afficher(self):
        super().afficher()
        print(f" Secrets partages : {len(self.secrets_partages)}")

if __name__ == "__main__":
    ami = MeilleurAmi("Sofia")
    print(ami.partager_secret("je ne sais pas encore qui je suis"))
    print(ami.soutenir("moment de doute profond"))
    ami.afficher()
