import streamlit as st
import csv
import pandas as pd
import altair as alt
import pydeck as py
import requests
from constants import STATES, CROPS
from utils import temperature_chart, crop_chart, totalProd_chart, totalTemp_chart

st.markdown("<h1 style='text-align: center; color: black;'>Climate Effects on Crop Production</h1>", unsafe_allow_html=True)

st.markdown("""---""")

filename = 'Crops-2017.csv'
COUNTIES = []
county = ""
crop = ""
state = ""

col1, col2, col3 = st.columns(3)

with col1:
    states = st.selectbox("Select a state", STATES).strip()
    state = states

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[1] == states:
            COUNTIES.append(row[0]);

with col2:
    counties = st.selectbox("Select a county", COUNTIES).strip()
    county = counties

with col3:
    crops = st.selectbox("Select a crop", CROPS).strip()
    crop = crops

st.markdown("""---""")

if crop == "Oats":
    st.markdown("<p style='text-align: center; color: black;'>Major oat producing states are Iowa, Minnesota and Wisconsin. Oats grow best in cool, moist climates, with the optimum temperature for growth being between 20°C and 21°C (68-70°F). The plants will thrive in well drained soils but are adapted to grow in many soil types, requiring a pH between 5.5 and 7.0.</p>", unsafe_allow_html=True)

if crop == "Soybeans":
    st.markdown("<p style='text-align: center; color: black;'>More than 80 percent of soybeans are cultivated in the upper Midwest. Soybeans are a temperate leguminous plant with an ideal daytime temperature of 85°F. When air temperatures exceed 85°F, soybeans can experience heat stress regardless of reproductive stage. When soybeans experience heat stress, yield reductions can begin to occur, especially when soil moisture is limiting.</p>", unsafe_allow_html=True)

if crop == "Wheat":
    st.markdown("<p style='text-align: center; color: black;'>Minnesota is a major wheat-producing state. High temperature stress is a major environmental factor that limits yield in wheat. Every 1°C increase above a mean temperature of 23°C decreases wheat yield by around 10 percent. More than 40 percent of total wheat area in the world is affected by high temperature stress.</p>", unsafe_allow_html=True)

if crop == "Corn":
    st.markdown("<p style='text-align: center; color: black;'>Corn is grown in most U.S. states, but production is concentrated in the Heartland region. Corn originated as a tropical grass and can tolerate exposures to adverse temperatures as high as 112°F for brief periods. Optimal daytime temperatures for corn typically range between 77°F and 91°F. Growth decreases when temperatures exceed 95°F.</p>", unsafe_allow_html=True)

st.markdown("""---""")

st.markdown("<h1 style='text-align: center; color: black;'>County</h1>", unsafe_allow_html=True)

colCounter = 0
first = 0
second = 0
third = 0
fourth = 0
fifth = 0
totalCrop1 = 0
totalCrop2 = 0
totalCrop3 = 0
totalCrop4 = 0
totalCrop5 = 0

with open('Crops-2017.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                first = col[colCounter]
            if (col[1] == state):
                if (col[colCounter] != ''):
                    hold = int(totalCrop1)
                    hold += int(col[colCounter])
                    totalCrop1 = str(hold)
        

with open('Crops-2012.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                second = col[colCounter]
            if (col[1] == state):
                if (col[colCounter] != ''):
                    hold = int(totalCrop2)
                    hold += int(col[colCounter])
                    totalCrop2 = str(hold)
                
            

with open('Crops-2007.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                third = col[colCounter]
            if (col[1] == state):
                if (col[colCounter] != ''):
                    hold = int(totalCrop3)
                    hold += int(col[colCounter])
                    totalCrop3 = str(hold)

with open('Crops-2002.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                fourth = col[colCounter]
            if (col[1] == state):
                if (col[colCounter] != ''):
                    hold = int(totalCrop4)
                    hold += int(col[colCounter])
                    totalCrop4 = str(hold)

with open('Crops-1997.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                fifth = col[colCounter]
            if (col[1] == state):
                if (col[colCounter] != ''):
                    hold = int(totalCrop5)
                    hold += int(col[colCounter])
                    totalCrop5 = str(hold)

crop_data = pd.DataFrame({
    'year': ['1997', '2002', '2007', '2012', '2017'], 'crop-production': [fifth, fourth, third, second, first], "Crop": crop})

totalCrop_data = pd.DataFrame({
    'year': ['1997', '2002', '2007', '2012', '2017'], 'crop-production': [totalCrop5, totalCrop4, totalCrop3, totalCrop2, totalCrop1], "Crop": crop})

chart1 = crop_chart.get_chart(crop_data)

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = 0
totalTemp1 = 0.0
totalTemp2 = 0.0
totalTemp3 = 0.0
totalTemp4 = 0.0
totalTemp5 = 0.0
stateCount1 = 0
stateCount2 = 0
stateCount3 = 0
stateCount4 = 0
stateCount5 = 0


with open('Temperature_2017.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if (row[0] == county and row[1] == state):
            temp1 = row[2]
        if (row[1] == state):
            # stateCount += 1.0
            stateCount1 += 1
            hold = float(totalTemp1)
            hold += float(row[2])
            totalTemp1 = str(hold)
    hold2 = float(totalTemp1) / stateCount1
    # hold2 = hold2
    totalTemp1 = str(hold2)
    

with open('Temperature_2012.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if (row[0] == county and row[1] == state):
            temp2 = row[2]
        if (row[1] == state):
            # stateCount += 1.0
            stateCount2 += 1
            hold = float(totalTemp2)
            hold += float(row[2])
            totalTemp2 = str(hold)
    hold2 = float(totalTemp2) / stateCount2
    # hold2 = hold2
    totalTemp2 = str(hold2)


with open('Temperature_2007.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if (row[0] == county and row[1] == state):
            temp3 = row[2]
        if (row[1] == state):
            # stateCount += 1.0
            stateCount3 += 1
            hold = float(totalTemp3)
            hold += float(row[2])
            totalTemp3 = str(hold)
    hold2 = float(totalTemp3) / stateCount3
    # hold2 = hold2
    totalTemp3 = str(hold2)

with open('Temperature_2002.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if (row[0] == county and row[1] == state):
            temp4 = row[2]
        if (row[1] == state):
            # stateCount += 1.0
            stateCount4 += 1
            hold = float(totalTemp4)
            hold += float(row[2])
            totalTemp4 = str(hold)
    hold2 = float(totalTemp4) / stateCount4
    # hold2 = hold2
    totalTemp4 = str(hold2)

with open('Temperature_1997.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if (row[0] == county and row[1] == state):
            temp5 = row[2]
        if (row[1] == state):
            # stateCount += 1.0
            stateCount5 += 1
            hold = float(totalTemp5)
            hold += float(row[2])
            totalTemp5 = str(hold)
    hold2 = float(totalTemp5) / float(stateCount5)
    # hold2 = hold2
    totalTemp5 = str(hold2)

temp_data = pd.DataFrame({
    'year': ['1997', '2002', '2007', '2012', '2017'], 'temperature': [temp5, temp4, temp3, temp2, temp1], "County": county})

avgTemp_data = pd.DataFrame({
    'year': ['1997', '2002', '2007', '2012', '2017'], 'temperature': [totalTemp5, totalTemp4, totalTemp3, totalTemp2, totalTemp1], "County": county})

chart2 = temperature_chart.get_chart(temp_data)

col1, col2 = st.columns(2)

col1, col2 = st.columns(2)

with col1:
    st.altair_chart(chart1, use_container_width=True)
with col2:
    st.altair_chart(chart2, use_container_width=True)

url = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + county + "+" + state +"&format=json&limit=1"
response = requests.get(url).json()

st.pydeck_chart(py.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=py.ViewState(
        latitude=int(float(response[0]["lat"])),
        longitude=int(float(response[0]["lon"])),
        zoom=11,
        pitch=50
)))

st.markdown("""---""")
st.markdown("<h1 style='text-align: center; color: black;'>State</h1>", unsafe_allow_html=True)

chart3 = totalProd_chart.get_chart(totalCrop_data)
st.altair_chart(chart3, use_container_width=True)

chart4 = totalTemp_chart.get_chart(avgTemp_data)
st.altair_chart(chart4, use_container_width=True)