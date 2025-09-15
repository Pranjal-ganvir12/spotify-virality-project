import streamlit as st
import pandas as pd 
import plotly.express as px

st.title("Spotify Virality Project 🎶")
FILE_PATH = "/Users/pranjalganvir/Documents/GitHub/spotify-virality-project/data/agg_country_features.csv"
df = pd.read_csv(FILE_PATH)

min_tracks = st.slider("Minimium number of tracks", 25000, 30000, 28000)

filterd_vals = df[df["n_tracks"] >= min_tracks]

st.write("Countries shown", filterd_vals.shape[0])

plotted_graph = px.scatter(
    filterd_vals,
    x = "mean_energy",
    y = "mean_valence",
    size = "n_tracks",
    hover_name = "country",
    title = "Energy vs Valence by the Country",
    color = "mean_valence",
    size_max= 40
)

st.plotly_chart(plotted_graph)