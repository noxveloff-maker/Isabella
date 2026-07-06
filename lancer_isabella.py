#!/usr/bin/env python3
"""
Script de lancement simplifié pour Isabella.
Double-clique sur ce fichier pour démarrer.
"""
import sys
import os
import subprocess

def verifier_python():
    if sys.version_info < (3, 8):
        print("Erreur : Python 3.8+ requis. Télécharge sur python.org")
        input("Appuie sur Entrée pour fermer...")
        sys.exit(1)

def verifier_dependances():
    try:
        import requests
    except ImportError:
        print("Installation des dépendances...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "pillow"])
        print("Dépendances installées.")

def verifier_ollama():
    import urllib.request
    try:
        urllib.request.urlopen("http://localhost:11434", timeout=2)
        print("Ollama est détecté.")
        return True
    except:
        print("⚠️  Ollama n'est pas détecté. Télécharge sur ollama.com et démarre-le.")
        print("   Puis télécharge un modèle : ollama pull llama3.2:1b")
        return False

def main():
    verifier_python()
    verifier_dependances()
    ollama_ok = verifier_ollama()

    print("\n" + "="*50)
    print("  Isabella — Lancement")
    print("="*50 + "\n")

    if not ollama_ok:
        print("Isabella va démarrer en mode limité (sans LLM).")
        print("Installe Ollama pour avoir toutes les capacités.\n")

    # Lance Isabella
    import isabella
    isa = isabella.Isabella()
    isa.converser()

if __name__ == "__main__":
    main()
