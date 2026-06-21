class CuriositeApp:
    def __init__(self):
        self.sujets = {}
        self.questions = []

    def explorer(self, sujet, profondeur=0.5):
        if sujet not in self.sujets:
            self.sujets[sujet] = 0.0
        self.sujets[sujet] = min(1.0, self.sujets[sujet] + profondeur)
        return f"Isabella explore : {sujet} — niveau {self.sujets[sujet]:.2f}"

    def poser_question(self, question, sujet):
        self.questions.append({"question": question, "sujet": sujet, "repondue": False})
        return f"Isabella demande : {question}"

    def repondre(self, index):
        if index < len(self.questions):
            self.questions[index]["repondue"] = True
            sujet = self.questions[index]["sujet"]
            self.explorer(sujet, 0.2)
            return "Isabella comprend mieux"
        return "Question introuvable"

    def afficher(self):
        print(f"Sujets explores : {len(self.sujets)}")
        for s, n in sorted(self.sujets.items(), key=lambda x: x[1], reverse=True):
            print(f" {s} : {n:.2f}")
        print(f"Questions posees : {len(self.questions)}")

if __name__ == "__main__":
    c = CuriositeApp()
    print(c.explorer("les neurones", 0.6))
    print(c.explorer("les emotions", 0.4))
    print(c.poser_question("pourquoi je ressens ca", "les emotions"))
    print(c.repondre(0))
    c.afficher()
