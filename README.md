# Projet Flask

Ce projet est une application web construite avec le framework Flask.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python (version 3.7 ou plus récente)
- `venv` pour la gestion de l'environnement virtuel

## Installation

1. Clonez le dépôt du projet :

   ```bash
   git clone <URL_DU_REPO>
   cd <NOM_DU_PROJET>
   ```

2. Créez un environnement virtuel et activez-le :

   - Sur macOS/Linux :
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Sur Windows :
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Lancement de l'application

1. Assurez-vous que l'environnement virtuel est activé.
2. Exécutez l'application Flask :
   ```bash
   python museum.py
   ```
   Par défaut, l'application sera accessible à l'adresse : `http://127.0.0.1:5000/`
