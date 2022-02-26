import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fir=pd.read_csv('datanew/artist_influence_music4_3.csv')
els=pd.read_csv('datanew/artist_influence_genre_decade5_4.csv')
data=pd.merge(fir,els,on='artist_id',how='inner')

sns.boxplot(x='music_genre', y='influence',data=data)
plt.xticks( rotation=60, fontsize='small')
plt.show()