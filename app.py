import streamlit as st
import bcrypt
import sqlite3
from loguru import logger

# Initialisation de la journalisation
logger.add('logs/app.log', rotation='1 MB')

def connect_db():
    return sqlite3.connect('database/data/securusers.db')

def create_user(username, password):
    # Hacher le mot de passe
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO securusers (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    logger.info(f'Utilisateur créé : {username}')

def verify_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM securusers WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    # Vérifier le mot de passe haché
    if result:
        return bcrypt.checkpw(password.encode('utf-8'), result[0])
    return False

st.title('Système de connexion sécurisé')

choice = st.selectbox('Choisissez une option', ['S\'inscrire', 'Se connecter'])

if choice == 'S\'inscrire':
    username = st.text_input('Nom d\'utilisateur')
    password = st.text_input('Mot de passe', type='password')
    if st.button('Créer un compte'):
        create_user(username, password)
        st.success('Compte créé avec succès !')

elif choice == 'Se connecter':
    username = st.text_input('Nom d\'utilisateur')
    password = st.text_input('Mot de passe', type='password')
    if st.button('Connexion'):
        if verify_user(username, password):
            st.success('Connexion réussie !')
            logger.info(f'Connexion réussie pour : {username}')
        else:
            st.error('Nom d\'utilisateur ou mot de passe incorrect')
            logger.warning(f'Échec de connexion pour : {username}')
