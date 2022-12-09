from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('week15_Quiz_Dash_PBI\Starbucks.csv')

df=df[df['Brand'] == 'Starbucks']
df=df[df['Country'] == 'TH']
df=df[df["State/Province"]=='83']

print(df.head())

## https://plotly.com/python-api-reference/generated/plotly.express.density_mapbox

fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', radius=10,
                        center=dict(lat=7.8, lon=98.32), zoom=8,
                        mapbox_style="open-street-map", hover_name= "City", hover_data=["Store Number", "Store Name"])

## https://plotly.com/python/mapbox-layers/

fig2 = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', hover_name= "City", hover_data=["Store Number", "Store Name"])
fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app.layout = html.Div(children=[
    html.H1(children='Store in Phuket'),

    dcc.Graph(
        id='storeInPhuket',
        figure=fig
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)