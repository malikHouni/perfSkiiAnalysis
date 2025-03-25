import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Définir un thème de couleurs pour Streamlit
st.set_page_config(page_title="Analyse des Performances des Skieurs", layout="wide")

# Générer des données fictives pour 10 skieurs
np.random.seed(42)
skieurs = [f"Skieur_{i+1}" for i in range(10)]
distances = np.random.uniform(1000, 5000, size=10)  # Distance en mètres
temps = np.random.uniform(300, 900, size=10)  # Temps en secondes
vitesses = distances / temps  # Calcul de la vitesse moyenne en m/s

# Créer un DataFrame
df = pd.DataFrame({
    'Skieur': skieurs,
    'Distance (m)': distances,
    'Temps (s)': temps,
    'Vitesse Moyenne (m/s)': vitesses
})

# Affichage du titre de l'application avec une image si nécessaire
st.title("Analyse des Performances des Skieurs")
st.markdown("""
    Cette application analyse les performances des skieurs en fonction de la distance parcourue,
    du temps écoulé et de la vitesse moyenne. Explorez les performances des skieurs et visualisez 
    des graphiques interactifs pour une meilleure compréhension.
""")

# Affichage du tableau des données
st.subheader("Données des Skieurs")
st.dataframe(df.style.highlight_max(axis=0, color='lightgreen'))

# Statistiques descriptives avec style
st.subheader("Statistiques des Performances")
st.write(df.describe().style.highlight_max(axis=0, color='lightblue'))

# Graphiques
st.subheader("Graphiques des Performances")
st.markdown("Voici quelques graphiques représentant les performances des skieurs.")

# Graphique de la vitesse moyenne avec style amélioré
plt.figure(figsize=(10, 6))
sns.barplot(x='Skieur', y='Vitesse Moyenne (m/s)', data=df, palette='coolwarm')
plt.title('Vitesse Moyenne des Skieurs', fontsize=16)
plt.xlabel('Skieur', fontsize=12)
plt.ylabel('Vitesse Moyenne (m/s)', fontsize=12)
plt.xticks(rotation=45)
st.pyplot(plt)

# Graphique de la distance vs temps avec une palette de couleurs attrayante
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temps (s)', y='Distance (m)', data=df, hue='Vitesse Moyenne (m/s)', palette='coolwarm', s=100)
plt.title('Distance vs Temps', fontsize=16)
plt.xlabel('Temps (s)', fontsize=12)
plt.ylabel('Distance (m)', fontsize=12)
st.pyplot(plt)

# Comparaison de la vitesse avec les autres skieurs
st.subheader("Classement des Skieurs par Vitesse Moyenne")
df_sorted = df.sort_values(by='Vitesse Moyenne (m/s)', ascending=False)
st.write(df_sorted[['Skieur', 'Vitesse Moyenne (m/s)']])

# Option de filtrage
skieur_choisi = st.selectbox('Choisir un skieur pour analyse détaillée', skieurs)
skieur_data = df[df['Skieur'] == skieur_choisi].iloc[0]

# Détails sur le skieur choisi
st.subheader(f"Analyse détaillée pour {skieur_choisi}")
st.markdown(f"""
    **Distance parcourue**: {skieur_data['Distance (m)']} m  
    **Temps total**: {skieur_data['Temps (s)']} s  
    **Vitesse moyenne**: {skieur_data['Vitesse Moyenne (m/s)']} m/s
""")

# Boutons pour télécharger les données ou voir les résultats sous forme de PDF (optionnel)
st.download_button(
    label="Télécharger les données des skieurs",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="performances_skieurs.csv",
    mime="text/csv"
)

# Ajout d'un fond pour la page avec un peu de style CSS
st.markdown("""
    <style>
        .reportview-container {
            background-color: #f4f4f9;
        }
        .sidebar .sidebar-content {
            background-color: #e0e0e0;
        }
        .css-1d391kg {
            background-color: #2e3a59;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)
