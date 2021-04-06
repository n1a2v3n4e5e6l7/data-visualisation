import pandas as pv
import plotly.express as px
df = pv.read_csv("data.csv")
fig = px.scatter(df,x = 'Population',y = 'Per capita',size = "Percentage",color = 'Country',size_max = 60,title = "Per capita income")
fig.show()