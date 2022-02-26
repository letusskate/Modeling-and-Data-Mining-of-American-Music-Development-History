
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('datanew/流派间相似性比较数据带影响.csv')
data=data.set_index('genre')
sns.heatmap(data,cmap='Reds')
plt.show()