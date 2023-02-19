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
        html.H1(children='Basic question'),

        html.Div(children='''
            compare the number of Starbucks stores among Thailand(TH), Vietnam(VN), Singapore(SG), and Malaysia(MY).
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig1,
            config = {'doubleClick': 'reset'}
        )
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.H1(children='Intermediate question'),

        html.Div(children='''
            click left graph to know the number of Starbucks stores in each province
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