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

## 4. In this graph, you use any machine learning methodology to analyze some part of the given data and show something based on your objective.
