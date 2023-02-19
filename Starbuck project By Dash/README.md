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

## 3. With this map graph , users can see the density of Starbucks stores in Phuket, Thailand.

## 4. In this graph, you use any machine learning methodology to analyze some part of the given data and show something based on your objective.
