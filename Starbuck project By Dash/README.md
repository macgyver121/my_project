# Analysis and Visualization the Starbuck dataset using Dash

## 1. With this graph, users can compare the number of Starbucks stores among Thailand, Vietnam, Singapore, and Malaysia.
```
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('week15_Quiz_Dash_PBI\Starbucks.csv')

df = df[df['Brand'] == 'Starbucks']
df = df[df['Country'].isin(['TH','VN','SG','MY'])]

df_count = df.groupby('Country')['Store Number'].count()

fig = px.histogram(df, x='Country', color='Country')

app.layout = html.Div(
    children=[
        html.H1(children='Basic Question'),

        dcc.Graph(
            id='graph1',
            figure=fig
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
```

![image](https://user-images.githubusercontent.com/85028821/219960816-0797163f-8e5d-4660-bc2a-f12bcd88bab7.png)

## 2. With these two graphs, users can click on each country in one graph and know the number of Starbucks stores in each province of the clicked country in another graph.

```
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('week15_Quiz_Dash_PBI\Starbucks.csv')

df = df[df['Brand'] == 'Starbucks']
df = df[df['Country'].isin(['TH','VN','SG','MY'])]

dfsummary=df.groupby(['Country'])['Store Number'].count()
#print(dfsummary)
dfsummary=dfsummary.reset_index()
#print(dfsummary)

dfsummarybycity=df.groupby(['State/Province'])['Store Number'].count()
dfsummarybycity=dfsummarybycity.reset_index()

fig1 = px.bar(dfsummary, x = 'Country', y = 'Store Number', color = 'Country')
fig2 = px.bar(dfsummarybycity, x = 'State/Province', y = 'Store Number')

app.layout = html.Div([ 

    html.Div(children=[
        html.H1(children='Chart1'),

        html.Div(children='''
            Compare the number of Starbucks stores among Thailand(TH), Vietnam(VN), Singapore(SG), and Malaysia(MY).
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig1,
            config = {'doubleClick': 'reset'}
        )
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.H1(children='Chart2'),

        html.Div(children='''
            The number of Starbucks stores in each province
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2,
            config = {'doubleClick': 'reset'}
        )
    ], style={'padding': 10, 'flex': 1})
 ], style={'display': 'flex', 'flexDirection': 'row'})

@app.callback(
    Output(component_id='graph2', component_property='figure'),
    Input(component_id='graph1', component_property='clickData'))

def update_graph(data):
    dffilter=df
    if bool(data):
        dffilter=df[df['Country']==data['points'][0]['x']]

    dfsummarybycity=dffilter.groupby(['State/Province'])['Store Number'].count()
    dfsummarybycity=dfsummarybycity.reset_index()

    figcity = px.bar(dfsummarybycity, x = 'State/Province', y = 'Store Number', barmode='group')

    return figcity

if __name__ == '__main__':
    app.run_server(debug=True)
```

![image](https://user-images.githubusercontent.com/85028821/219960961-02ab69ef-7954-4186-86b1-5c4320575e68.png)


## 3. With this map graph , users can see the density of Starbucks stores in Phuket, Thailand.

```
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
```

![image](https://user-images.githubusercontent.com/85028821/219961080-7c71adb6-5c59-48bc-ad28-dd5dd272a721.png)


## 4. In this graph, you use any machine learning methodology to analyze some part of the given data and show something based on your objective.
Use K-means for clustering store by country in 4 group

```
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
```

![image](https://user-images.githubusercontent.com/85028821/219961291-dde57916-cf26-406d-b954-82b3a4e146e8.png)
