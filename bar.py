import pandas as pv
import plotly.express as px
df = pv.read_csv("data.csv")
fig = px.bar(df,x = 'Country',y = 'InternetUsers')
fig.show()







