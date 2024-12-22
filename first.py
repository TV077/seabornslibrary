import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


#Création d'un dataframe de démonstration.

data = pd.DataFrame({
    'age':[23,45,56,78,21,34,49,50,20,31,73,24,58,46,35,62]
})

# Tracé de l'histogramme avec estimation de la densité :
sns.histplot(data['age'], kde =True)
plt.title('Distribution des âges')


# Diagramme de dispersion :

data2 = pd.DataFrame({
    'height': [170,180,160,175,165,185,155,190,175,170],
    'weight': [65,80,55,70,60,90,50,85,75,65]
})

sns.scatterplot(x='height', y='weight', data=data2)
plt.title('Relation entre la taille et le poid')
plt.xlabel('Taille (cm)')
plt.ylabel('Poids (kg)')
plt.show()