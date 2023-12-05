import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
import

#Loading the dataset locally
df = pd.read_csv('./data/renewable_power_plants_CH.csv')

#Loading the geojson data locally
file_path = './data/georef-switzerland-kanton.geojson'
with open(file_path, 'r') as file:
    geojson = json.load(file)
geojson

st.title("Visualization of Renewable Energy Utilization in Switzerland")

# st.table(data=df.head())

# df = df[df['lat'].notna() & df['lon'].notna()]
# st.map(data=df)

st.header("Renewable Energy distribution across Switzerland")
df_canton = df.groupby('canton').agg({'electrical_capacity':'sum'})
fig = px.choropleth_mapbox(
    df_canton,
    geojson=geojson,
    color='electrical_capacity',

)
