from sklearn.cluster import KMeans
import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from sklearn.cluster import KMeans
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('week15_Quiz_Dash_PBI\Starbucks.csv')
df=df[df['Store Number'] != '19773-160973']


X=df[['Longitude','Latitude']]

nc=4

kmeans = KMeans(n_clusters=nc, random_state=125)
kmeans.fit(X)

df['predict']=kmeans.predict(X)
#print(df['predict'])

fig = px.scatter_mapbox(df, lon="Longitude", lat="Latitude", 
    color="predict", hover_data=['Country'], zoom=1.5, center=dict(lat=27, lon=-15))
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app.layout = html.Div(children=[
    html.H1(children='Use K mean to group store by GPS'),
 
    dcc.Graph(
        id='storeInPhuket',
        figure=fig
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)