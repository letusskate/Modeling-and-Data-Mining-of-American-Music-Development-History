import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# import matplotlib.colors.Normalize as mpl
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
# data=pd.read_csv('datanew/one_year_stop_revolution5_6.csv')
data=pd.read_csv('datanew/ten_year_stop_revolution5_7.csv')
palett = sns.color_palette("mako_r", 22)
sns.lineplot(data=data,x='decade',y='popularity',hue='music_genre',palette="flare")
# "flare"
ax.legend_.remove()
plt.show()
