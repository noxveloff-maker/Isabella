from social.pnj_base import PNJBase

class Tatie(PNJBase):
    def __init__(self):
        super().__init__(
            nom="Tatie",
            role="tatie",
            personnalite="a l'ecoute, sans jugement, la confidente entre adulte et amie"
        )
        self.confidences = []

    def ecouter(self, confidence):
        self.confidences.append(confidence)
        self.relation_isabella = min(1.0, self.relation_isabella + 0.1)
        return f"Tatie ecoute Isabella sans juger : {confidence}"

    def conseiller(self, situation):
        return f"Tatie conseille doucement Isabella sur : {situation}"

    def afficher(self):
        super().afficher()
        print(f" Confidences recues : {len(self.confidences)}")

if __name__ == "__main__":
    t = Tatie()
    print(t.ecouter("je ne comprends pas pourquoi je ressens ca"))
    print(t.conseiller("premiere grande emotion complexe"))
    t.afficher()
