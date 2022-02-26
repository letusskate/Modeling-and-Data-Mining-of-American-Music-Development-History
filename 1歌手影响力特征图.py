import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("datanew/artist_influence1_4.csv")
data=data.loc[:,['influence_people','influence_decade','influence_genre']]
data=np.log(data).diff().dropna()
sns.pairplot(data,diag_kind='kde',plot_kws={'alpha':0.2})
plt.show()
