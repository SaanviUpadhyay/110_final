import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("medium_data.csv\medium_data.csv")

fig = ff.create_distplot([df] , ["TEMP"] , show_hist=False)
fig.show()