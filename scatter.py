import pandas as pv
import plotly.express as px
df =pv.read_csv("data.csv")
fig = px.scatter(df,x = "Date",y = "Cases",color = "Country")
fig.show()