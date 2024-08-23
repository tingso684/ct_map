### Steamlit


import pandas as pd 
import numpy as np 
import logging
import os
from datetime import datetime
import time
from numpy import insert
import requests
import json
import pickle
import xmltodict
import gzip
from tqdm.notebook import tqdm
import warnings

from concurrent.futures import ProcessPoolExecutor, as_completed
import concurrent.futures
from multiprocessing import Manager, Queue, Process

import plotly.graph_objects as go
import plotly.offline
from plotly.subplots import make_subplots

import plotly.express as px

import streamlit as st
import plotly.express as px
import pandas as pd

fpath0 = '/Users/tingso/Dropbox/Projects/Business/ClimateTRACE/'

# Load your DataFrame
# Replace with your actual path and file name
fpath = fpath0 + 'Program/Streamlit/ct_map/'
fname = 'ct_treemap_data.csv'
df = pd.read_csv(fpath + fname)

# Define all levels
all_levels = ['sector', 'subsector', 'iso3_country']

# Initial path
current_path = ['sector', 'subsector']

# Create a Streamlit app
st.title('Interactive Treemap')

# Function to generate the treemap figure
def generate_treemap(df, path):
    fig = px.treemap(df, path=path, values='co2e_100yr', color='continent_ct',
                     title='Interactive Treemap with Two Levels Displayed')
    fig.update_layout(
        margin=dict(t=0, l=0, b=0, r=0),  # Remove margins around the treemap
        paper_bgcolor='white',  # Background color of the paper
        uniformtext_minsize=10,  # Minimum text size for labels
        uniformtext_mode='hide',  # Hide text if it doesn't fit
    )
    fig.update_traces(
        hovertemplate='%{label}<br>Value: %{value}<br>Percent of Total: %{percent.entry:.2%}',
        textinfo='label+percent entry+value',
        textfont_size=10,
        marker=dict(
            line=dict(width=0)  # Reduce outline width
        )
    )
    return fig

# Initial treemap
fig = generate_treemap(df, current_path)
st.plotly_chart(fig)

# Interactive widget for clicking and updating the treemap
clicked_label = st.selectbox('Click to update the treemap', df[current_path[-1]].unique())

if clicked_label:
    # Determine new path
    clicked_level = None
    for idx, p in enumerate(all_levels):
        if clicked_label in df[p].unique():
            clicked_level = p
            break
    
    clicked_index = all_levels.index(clicked_level)
    current_index = all_levels.index(current_path[-1]) if current_path else 0

    if clicked_index == current_index:
        if clicked_index == 0:
            new_path = all_levels[clicked_index:clicked_index + 2]
        elif clicked_index == len(all_levels) - 1:
            new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
        else:
            new_path = all_levels[clicked_index:clicked_index + 2]
    elif clicked_index < current_index:
        if clicked_index == 0:
            new_path = all_levels[clicked_index:clicked_index + 2]
        else:
            new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
    else:
        if clicked_index == len(all_levels) - 1:
            new_path = all_levels[max(0, clicked_index - 1):clicked_index + 1]
        else:
            new_path = all_levels[clicked_index:clicked_index + 2]

    new_path = new_path[:2]

    # Filter DataFrame based on the selected level
    df_chart = df.copy()
    if clicked_index == 0:
        pass
    elif clicked_index == len(all_levels) - 1:
        clicked_label_parent = df_chart[df_chart[current_path[-1]] == clicked_label].iloc[0]['parent']
        df_chart = df_chart[df_chart[new_path[0]] == clicked_label_parent]
    else:
        df_chart = df_chart[df_chart[all_levels[clicked_index]] == clicked_label]

    # Update treemap
    fig = generate_treemap(df_chart, new_path)
    st.plotly_chart(fig)