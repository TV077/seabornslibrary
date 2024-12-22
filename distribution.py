import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'income': np.random.normal(50000,15000,1000)

})

#Affichage du graphique de densité :
sns.kdeplot(data['income'], shade=True)
plt.title('Distribution de revenu')
plt.show()