import pandas as pd
import streamlit as st
import plotly.express as px
st.title("Basic Streamlit App")

football_stats = pd.read_csv("byu_football_stats_2025.csv")
fig = px.scatter(
    football_stats,
    x="netPassingYards",
    y="byu_score",
    size="rushingYards",
    color="opponent_score",
    hover_data=["firstDowns", "thirdDownEff", "possessionTime"],
    title="BYU Score vs Net Passing Yards"
)


choice = st.radio('Do you like football?', ["yes","no"])
if choice == "yes":
    st.plotly_chart(fig)
else: 
    st.write("No graph for you")

