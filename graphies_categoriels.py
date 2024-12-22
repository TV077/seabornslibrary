import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
   'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
   'income': [70000, 80000, 60000, 85000, 90000, 75000, 65000, 95000, 55000, 90000]
})


#Boxplot Montre la répartition d’une variable quantitative en catégories en utilisant les quartiles de la distribution et les valeurs extrêmes. Très utile pour détecter les valeurs aberrantes.

#sns.boxplot(x='gender', y='income', data=data)
#plt.title('Distribution du revenu par genre')

#Violinplot combine les aspects d’un boxplot et d’un KDE pour fournir des informations riches sur la distribution des données en catégories.
#sns.violinplot(x='gender', y='income',data=data)
#plt.title('violon plot du revenu par genre')


#Swarmplot Affiche tous les points de données sans chevauchement, ce qui peut donner une meilleure représentation de la distribution des valeurs, particulièrement en combinaison avec un boxplot ou violinplot.
sns.swarmplot(x='gender', y='income', data=data, color='k', alpha=0.5)
plt.show()