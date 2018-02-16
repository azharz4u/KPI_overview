import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, plot
from collections import defaultdict
import pandas as pd
import sys

app = dash.Dash(__name__)
server = app.server
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
app.config.suppress_callback_exceptions=True
df = pd.read_csv('http://npmran/projects/MainKPIs/PC.csv')
available_Sites= df['Sites'].unique()
app.layout = html.Div([
html.Div([
html.Div([
html.H1('Total_PS_Traffic'),
dcc.Dropdown(
id='mydropdown',
options=[{'label': i, 'value': i} for i in available_Sites],
value='UAJR3313',
multi=True),
dcc.Graph(id='graph0'),
],style={'display': 'inline-block', 'width': '49%','height': '100%'}),
html.Div([
html.H1('packetloss'),
dcc.Graph(id='graph1')
],style={'display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('Voice_Drops'),
dcc.Graph(
id='graph2')
],style={'display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS_Drops'),
dcc.Graph(
id='graph3')
],style={'display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('RRC_Fails'),
dcc.Graph(
id='graph4')
],style={'display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('Voice_Traffic'),
dcc.Graph(
id='graph5')
],style={'display': 'inline-block', 'width': '49%'}),
html.Div([
html.H1('PS_RAB_Fails'),
dcc.Graph(
id='graph6')
],style={'display': 'inline-block', 'width': '49%'}),
])])
@app.callback(
Output('graph0','figure'), [Input('mydropdown', 'value')])
def update_graph0(selected_dropdown_value):
    # loop through each selectd sites and add a trace to the graph corresponding to that sites
    traces = []
    for sites in selected_dropdown_value:
        odf = df[df['Sites'] == sites]
        trace = {'x': odf['Date'], 'y': odf['Total_PS_Traffic'],'name':sites}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph1','figure'), [Input('mydropdown', 'value')])
def update_graph1(selected_dropdown_value):
    # loop through each selectd sites and add a trace to the graph corresponding to that sites
    traces = []
    for sites in selected_dropdown_value:
        odf = df[df['Sites'] == sites]
        trace = {'x': odf['Date'], 'y': odf['packetloss'],'name':sites}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph2','figure'), [Input('mydropdown', 'value')])
def update_graph2(selected_dropdown_value):
    # loop through each selectd sites and add a trace to the graph corresponding to that sites
    traces = []
    for sites in selected_dropdown_value:
        odf = df[df['Sites'] == sites]
        trace = {'x': odf['Date'], 'y': odf['Voice_Drops'],'name':sites}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph3','figure'), [Input('mydropdown', 'value')])
def update_graph3(selected_dropdown_value):
    # loop through each selectd sites and add a trace to the graph corresponding to that sites
    traces = []
    for sites in selected_dropdown_value:
        odf = df[df['Sites'] == sites]
        trace = {'x': odf['Date'], 'y': odf['PS_Drops'],'name':sites}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph4','figure'), [Input('mydropdown', 'value')])
def update_graph4(selected_dropdown_value):
    # loop through each selectd sites and add a trace to the graph corresponding to that sites
    traces = []
    for sites in selected_dropdown_value:
        odf = df[df['Sites'] == sites]
        trace = {'x': odf['Date'], 'y': odf['RRC_Fails'],'name':sites}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph5','figure'), [Input('mydropdown', 'value')])
def update_graph5(selected_dropdown_value):
    # loop through each selectd sites and add a trace to the graph corresponding to that sites
    traces = []
    for sites in selected_dropdown_value:
        odf = df[df['Sites'] == sites]
        trace = {'x': odf['Date'], 'y': odf['Voice_Traffic'],'name':sites}
        traces.append(trace)
    return {'data': traces}
@app.callback(
Output('graph6','figure'), [Input('mydropdown', 'value')])
def update_graph6(selected_dropdown_value):
    # loop through each selectd sites and add a trace to the graph corresponding to that sites
    traces = []
    for sites in selected_dropdown_value:
        odf = df[df['Sites'] == sites]
        trace = {'x': odf['Date'], 'y': odf['PS_RAB_Fails'],'name':sites}
        traces.append(trace)
    return {'data': traces}	

if __name__ == '__main__':
    app.run_server(debug=True)