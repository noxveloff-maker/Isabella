# Isabella - Guide d'installation sur ton PC

## Prérequis

- **Python 3.8+** installé (télécharge sur [python.org](https://python.org))
- **Git** (optionnel, pour cloner)

---

## 1. Copier les fichiers sur ton PC

### Méthode A : Copier le dossier complet

Copie le dossier `Isabella/` (ou tout le dossier du projet) sur ton PC, par exemple dans :
```
C:\Users\TON_NOM\Documents\Isabella\
```

### Méthode B : Créer une archive ZIP

Dans un terminal (si tu as accès à ce PC) :
```bash
cd /chemin/vers/le/projet
zip -r isabella.zip . -x "*/__pycache__/*" "*.pyc"
```

Puis dézippe sur ton PC.

---

## 2. Installer les dépendances Python

Ouvre un terminal (cmd sur Windows, Terminal sur macOS/Linux) et va dans le dossier :

```bash
cd C:\Users\TON_NOM\Documents\Isabella

# Créer un environnement virtuel (recommandé)
python -m venv venv

# Activer l'environnement
# Windows :
venv\Scripts\activate
# macOS/Linux :
source venv/bin/activate

# Installer les dépendances
pip install requests pillow
```

### Dépendances optionnelles (fortement recommandées)

| Dépendance | Pourquoi | Installation |
|-----------|----------|-------------|
| **Tesseract OCR** | Lire le texte à l'écran | Voir ci-dessous |
| **pytesseract** | Wrapper Python Tesseract | `pip install pytesseract` |
| **pyautogui** | Contrôle souris/clavier plus robuste | `pip install pyautogui` |

#### Installer Tesseract OCR

- **Windows** : Télécharge sur [github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki), installe, puis ajoute au PATH.
- **macOS** : `brew install tesseract`
- **Linux** : `sudo apt install tesseract-ocr`

---

## 3. Installer Ollama (LLM local)

Isabella utilise un LLM local via Ollama.

1. Va sur [ollama.com](https://ollama.com) et télécharge Ollama pour ton OS.
2. Installe et démarre Ollama.
3. Télécharge un modèle (dans un terminal) :
   ```bash
   ollama pull llama3.2:1b
   # ou pour un modèle plus puissant :
   ollama pull llama3.2
   ```

---

## 4. Lancer Isabella

Dans le terminal, toujours dans le dossier Isabella avec l'environnement activé :

```bash
python isabella.py
```

Isabella démarre et te dit bonjour. Elle crée automatiquement les fichiers de sauvegarde.

---

## 5. Utiliser Isabella

Tape tes commandes en français. Exemples :

```
> liste le dossier .
> ouvre youtube et cherche ninjaxx
> capture l'écran
> clique sur le texte "Valider"
> ouvre le pavé numérique
> montre les suggestions
```

---

## 6. Fichiers importants

| Fichier | Description |
|---------|-------------|
| `isabella.py` | Fichier principal — lance celui-ci |
| `apprentissage_commandes.json` | Historique des commandes (auto-généré) |
| `apprentissage_visuel.json` | Positions d'éléments mémorisés |
| `memoire_long_terme.json` | Souvenirs d'Isabella |
| `journal_isabella.json` | Journal de toutes les interactions |
| `sauvegardes/` | Sauvegardes automatiques |
| `~/scripts_isabella/` | Scripts créés par l'utilisateur |
| `~/captures_isabella/` | Captures d'écran |

---

## 7. Structure du projet

```
Isabella/
├── isabella.py                    # Fichier principal
├── cerveau/                       # Neural networks, émotions
├── memoire/                       # Mémoires court/long terme
├── sensations/                    # Émotions (joie, peur, etc.)
├── langage/                       # LLM, prompt, parser
├── corps/                         # Avatar, visage, gestes
├── systeme/                       # Actions système
│   ├── fichiers.py
│   ├── terminal.py
│   ├── ecran.py
│   ├── controle.py
│   ├── navigateur.py
│   ├── orchestrateur.py
│   ├── scripts.py
│   ├── apprentissage_commandes.py
│   ├── chaineur.py
│   ├── vision_ecran.py           # OCR, vision
│   ├── selection.py              # Clic-glisser, copier
│   ├── apprentissage_visuel.py   # Mémorise positions
│   └── pave_numerique.py         # Clavier virtuel
├── apprentissage/
├── environnement/
├── social/
├── outils/
└── GUIDE_INSTALLATION.md         # Ce fichier
```

---

## 8. Problèmes courants

| Problème | Solution |
|----------|----------|
| `ModuleNotFoundError: No module named 'requests'` | `pip install requests` |
| `Tesseract not found` | Installer Tesseract et ajouter au PATH |
| Ollama ne répond pas | Vérifier qu'Ollama est démarré (`ollama serve`) |
| `Permission denied` sur Linux | `chmod +x` sur les scripts, ou utiliser `sudo` pour les captures |
| Le pavé numérique ne s'ouvre pas | tkinter est inclus dans Python standard, vérifier l'installation Python |

---

## 9. Personnaliser Isabella

Tu peux modifier son comportement en éditant :
- `langage/prompt_systeme.py` — son contexte et sa personnalité
- `isabella.py` — son nom, ses paramètres

---

Bonjour ! Je suis prête à t'aider sur ton PC.
