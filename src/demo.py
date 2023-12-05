import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

# st.balloons()

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df


mpg_df_raw = load_data(path="./data/mpg.csv")
mpg_df = deepcopy(mpg_df_raw)


st.title("Introduction to streamlit")
st.header("MPG Data Exploration")

# url = 
# st.write("Data Source:", url)


# st.table(data=mpg_df)




if st.checkbox("Show Datafame"):
    st.subheader("This is my dataset:")
    st.dataframe(data=mpg_df.head())

left_column, right_column = st.columns(2)

years = ["All"] + sorted(pd.unique(mpg_df['year']))
year = left_column.selectbox("choose a year", years)

show_means = right_column.radio(
    label='show class means', options=['yes', 'no']
)

if year == "All":
    reduced_df = mpg_df
else:
    reduced_df = mpg_df[mpg_df["year"] == year]

means = reduced_df.groupby('class').mean(numeric_only=True)
m_fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(reduced_df['displ'], reduced_df['hwy'], alpha=0.5)
if show_means == "yes":
    ax.scatter

st.pyplot(m_fig)