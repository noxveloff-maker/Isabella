import tkinter as tk
from tkinter import ttk
import threading
import queue

class PaveNumerique:
    """
    Pavé numérique virtuel cliquable avec tkinter.
    Permet de saisir des chiffres, de copier/coller, et d'envoyer à Isabella.
    """

    def __init__(self, callback=None):
        self.callback = callback  # Fonction appelée quand on appuie sur une touche
        self.fenetre = None
        self.file_touches = queue.Queue()
        self._thread_ui = None
        self._en_cours = False

    def _creer_interface(self):
        """Crée la fenêtre tkinter avec le pavé numérique."""
        self.fenetre = tk.Tk()
        self.fenetre.title("Pavé Numérique — Isabella")
        self.fenetre.geometry("300x400")
        self.fenetre.resizable(False, False)
        self.fenetre.configure(bg="#1a1a2e")

        # Zone d'affichage
        self.affichage = tk.Entry(
            self.fenetre, font=("Segoe UI", 24), justify="right",
            bg="#16213e", fg="#e94560", insertbackground="#e94560",
            relief=tk.FLAT, bd=10
        )
        self.affichage.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
        self.affichage.bind("<KeyPress>", self._on_key_press)

        # Configuration grille
        for i in range(5):
            self.fenetre.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.fenetre.grid_columnconfigure(j, weight=1)

        # Boutons
        boutons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2),
        ]

        for texte, row, col in boutons:
            btn = tk.Button(
                self.fenetre, text=texte, font=("Segoe UI", 18, "bold"),
                bg="#0f3460", fg="#e94560", activebackground="#e94560",
                activeforeground="#0f3460", relief=tk.FLAT, bd=0,
                command=lambda t=texte: self._appuyer(t),
                cursor="hand2"
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            # Effet hover
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#1a5276"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#0f3460"))

        # Boutons actions
        actions = [
            ("C", 5, 0, "#c0392b", self._clear),
            ("←", 5, 1, "#7f8c8d", self._backspace),
            ("OK", 5, 2, "#27ae60", self._valider),
        ]

        for texte, row, col, couleur, cmd in actions:
            btn = tk.Button(
                self.fenetre, text=texte, font=("Segoe UI", 16, "bold"),
                bg=couleur, fg="white", activebackground="white",
                activeforeground=couleur, relief=tk.FLAT, bd=0,
                command=cmd, cursor="hand2"
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Boutons spéciaux (Ctrl+C, Ctrl+V, Espace)
        speciaux = [
            ("Ctrl+C", 6, 0, self._ctrl_c),
            ("Espace", 6, 1, self._espace),
            ("Ctrl+V", 6, 2, self._ctrl_v),
        ]

        for texte, row, col, cmd in speciaux:
            btn = tk.Button(
                self.fenetre, text=texte, font=("Segoe UI", 12),
                bg="#2c3e50", fg="#bdc3c7", activebackground="#34495e",
                relief=tk.FLAT, bd=0, command=cmd, cursor="hand2"
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        self.fenetre.protocol("WM_DELETE_WINDOW", self._fermer)
        self.fenetre.mainloop()

    def _on_key_press(self, event):
        """Capture les touches du clavier physique aussi."""
        if event.char in "0123456789.":
            self._appuyer(event.char)
        elif event.keysym == "Return":
            self._valider()
        elif event.keysym == "BackSpace":
            self._backspace()
        elif event.keysym == "Escape":
            self._clear()
        return "break"

    def _appuyer(self, touche):
        """Ajoute une touche à l'affichage."""
        self.affichage.insert(tk.END, touche)
        self.file_touches.put(touche)

    def _clear(self):
        """Efface tout."""
        self.affichage.delete(0, tk.END)
        self.file_touches.put("CLEAR")

    def _backspace(self):
        """Efface le dernier caractère."""
        texte = self.affichage.get()
        self.affichage.delete(0, tk.END)
        self.affichage.insert(0, texte[:-1])
        self.file_touches.put("BACKSPACE")

    def _valider(self):
        """Valide et envoie le texte."""
        texte = self.affichage.get()
        self.file_touches.put(f"VALIDATE:{texte}")
        if self.callback:
            self.callback(texte)
        self.affichage.delete(0, tk.END)

    def _ctrl_c(self):
        """Simule Ctrl+C."""
        self.file_touches.put("CTRL+C")
        if self.callback:
            self.callback("CTRL+C")

    def _ctrl_v(self):
        """Simule Ctrl+V."""
        self.file_touches.put("CTRL+V")
        if self.callback:
            self.callback("CTRL+V")

    def _espace(self):
        """Ajoute un espace."""
        self.affichage.insert(tk.END, " ")
        self.file_touches.put(" ")

    def _fermer(self):
        """Ferme la fenêtre."""
        self._en_cours = False
        self.file_touches.put("CLOSE")
        if self.fenetre:
            self.fenetre.destroy()
            self.fenetre = None

    def ouvrir(self):
        """Ouvre le pavé numérique dans un thread séparé."""
        if self._en_cours:
            return {"info": "Pavé déjà ouvert"}
        self._en_cours = True
        self._thread_ui = threading.Thread(target=self._creer_interface, daemon=True)
        self._thread_ui.start()
        return {"succes": True, "message": "Pavé numérique ouvert"}

    def fermer(self):
        """Ferme le pavé numérique."""
        self._fermer()
        return {"succes": True, "message": "Pavé numérique fermé"}

    def lire_touche(self, timeout=0.1):
        """Lit une touche depuis la file (non bloquant)."""
        try:
            return self.file_touches.get(timeout=timeout)
        except queue.Empty:
            return None

    def attendre_validation(self, timeout=30):
        """Attend que l'utilisateur valide une saisie."""
        import time
        debut = time.time()
        while time.time() - debut < timeout:
            touche = self.lire_touche(timeout=0.5)
            if touche and touche.startswith("VALIDATE:"):
                return touche.split(":", 1)[1]
            if touche == "CLOSE":
                return None
        return None

    def est_ouvert(self):
        """Vérifie si le pavé est ouvert."""
        return self._en_cours and self.fenetre is not None

if __name__ == "__main__":
    def on_touche(texte):
        print(f"[Pavé] Touche appuyée : {texte}")

    p = PaveNumerique(callback=on_touche)
    p.ouvrir()

    # Attend la validation
    resultat = p.attendre_validation(timeout=60)
    if resultat:
        print(f"Validation : {resultat}")
    else:
        print("Fermé ou timeout")
