# Système de Connexion Sécurisé

Ce projet est une application Streamlit qui permet aux utilisateurs de s'inscrire et de se connecter à un système sécurisé. Les mots de passe sont hachés à l'aide de la bibliothèque `bcrypt`, et les événements sont journalisés à l'aide de `loguru`.

## Fonctionnalités

- **Enregistrement des utilisateurs** : Les utilisateurs peuvent créer un compte avec un nom d'utilisateur et un mot de passe.
- **Connexion sécurisée** : Les utilisateurs peuvent se connecter avec leurs informations d'identification.
- **Hachage des mots de passe** : Les mots de passe sont stockés sous forme hachée pour garantir la sécurité.
- **Journalisation** : Les événements importants (comme les tentatives de connexion) sont enregistrés pour la traçabilité.

## Prérequis

- Python 3.x
- Bibliothèques Python requises :
  - `streamlit`
  - `cryptography`
  - `loguru`
  - `bcrypt`

## Installation

1. Clonez ce dépôt :

   ```bash
   git clone <URL_DU_REPO>
   cd <NOM_DU_REPO>

2. Créez un environnement virtuel et activez-le :

``
    python -m venv .venv
    source .venv/bin/activate  # Sur Windows utilisez .venv\Scripts\activate
``

3. Installez les dépendances :

``
   pip install -r requirements.txt
``

4. Exécutez le script d'initialisation de la base de données pour créer la base de données et la table :

``
   python init_db.py

``

5. Démarrez l'application Streamlit :

``
    streamlit run app.py
``

## Utilisation

- Accédez à l'application via le navigateur à l'adresse suivante : ``http://localhost:8501``
- Choisissez entre S'inscrire ou Se connecter.
- Suivez les instructions à l'écran pour créer un compte ou vous connecter.

## Structure du Projet

```.
├── app.py               # Application principale Streamlit
├── init_db.py           # Script pour initialiser la base de données
├── requirements.txt      # Fichier des dépendances
├── logs/                # Dossier pour les fichiers de log
│   └── app.log          # Journalisation des événements
└── data/                # Dossier pour la base de données
    └── securusers.db    # Base de données SQLite
```

## Aide et Support

Pour toute question ou problème, n'hésitez pas à ouvrir une issue sur ce dépôt ou à me contacter directement