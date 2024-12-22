import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'age':[25,30,35,40,45,50,55,60,65,70,],
    'income':[50000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000],
    'height': [165,170,175,180,185,190,195,200,205,210]
})

#Scaterplot idéal pour visualiser la relation entre deux variables continues.
#Il montre comment les valeurs d'une variable varient avec une autre.

#sns.scatterplot(x='age',y='income', data=data)
#plt.title('Relation entre âge et revenu')


#Pairplot utile pour visualiser les relations entre toutes les combinaisons de plusieurs paires de variable.
#sns.pairplot(data[['age','income','height']])

#Joinplot combine des diagrammes de dispersion ou des hexbins avec des histogrammes pour fournir des aperçus détaillés de la relation bivariée entre deux variables.
sns.jointplot(data[['age','income','height']])
plt.show()