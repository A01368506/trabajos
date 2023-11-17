import streamlit as st
import pandas as pd
import numpy as np
import plotly as px
import plotly.figure_factory as ff
from bokeh.plotting import figure
import matplotlib.pyplot as plt


st.title("Police Incident Reports from 2018 to 2020 in San Francisco")
df = pd.read_csv("Police.csv")
st.markdown("The data shown below  belongs to incident reports in the city of San francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police districts, neighborhood in which it happened, type of incidentin category and subcategory, exact location and resoluntion.")
mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()

subset_data2 = mapa
police_district_input = st.sidebar.multiselect(
'Police District',
mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input) > 0:
    subset_data2 = mapa[mapa['Police District'].isin(police_district_input)]

subset_data1 = subset_data2
neighborhood_input = st.sidebar.multiselect(
'Neighborhood',
subset_data2.groupby('Neighborhood').count().reset_index()['Neighborhood'].tolist())
if len(neighborhood_input) > 0:
    subset_data1 = subset_data2[subset_data2['Neighborhood'].isin(neighborhood_input)]

subset_data = subset_data1
incident_input = st.sidebar.multiselect(
    'Incident Category',
    subset_data1.groupby('Incident Category').count().reset_index()['Incident Category'].tolist())

if len(incident_input) > 0:
    subset_data = subset_data1[subset_data1['Incident Category'].isin(incident_input)]

subset_data
