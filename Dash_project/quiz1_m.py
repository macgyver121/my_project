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