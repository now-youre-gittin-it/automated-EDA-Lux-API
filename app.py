import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import pandas as pd
import lux

def app():
    st.title('Analysis of Superstore Dataset')
    st.write('Check out these cool visualizations!')
    #df = pd.read_csv("https://raw.githubusercontent.com/lux-org/lux-datasets/master/data/hpi.csv")
    #export_file = 'visualizations.html'
    #export_file = 'visualizations.html'
    #html_content = df.save_as_html(output=True)
    html_file=open('D:/Abhinaya/GitHub/automated-EDA-Lux-API/my_viz.html', 'r', encoding='utf-8')
    html_content=html_file.read()
    #print(html_content)
    components.html(html_content, width=1000, height=800)


app()
