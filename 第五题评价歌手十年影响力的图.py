import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("datanew/ten_year_stop_major_artist_influence5_13.csv")
data=data.loc[:,['influence','genre','major_artist']]
sns.stripplot(x="genre",y="influence",data=data,jitter=True)
plt.xticks( rotation=60, fontsize='small')
plt.show()
