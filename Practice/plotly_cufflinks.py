import cufflinks as cf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chart_studio.plotly as py

from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot

init_notebook_mode(connected=True)
cf.go_online()


df1 = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
print(df1.head(3))

df2 = pd.DataFrame({
    'Category':['A','B','C'],
    'Values':[1,2,3]
})
print(df1.head())

# this matplotlib plot
# df1.plot()

# this is iplot, plotly
df1.iplot()
plt.show()


