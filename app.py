import streamlit as st

import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''

#Website header
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write('Day and time:')
    day_inp = st.date_input('Ride day:')
    time_inp = st.time_input('Ride time:')
    pickup_datetime_inp = f'{day_inp} {time_inp}'
    #st.write(pickup_datetime_inp)

with col2:
    st.write('Pickup location:')
    pickup_longitude_inp = st.number_input('Pickup longitude:', step=0.0001)
    pickup_latitude_inp = st.number_input('Pickup latitude:')

with col3:
    st.write('Dropoff location:')
    dropoff_longitude_inp = st.number_input('Dropoff longitude:')
    dropoff_latitude_inp = st.number_input('Dropoff latitude:')

with col4:
    st.write('Number of passengers:')
    passenger_count_inp = st.number_input('Passenge count:', step=1)


#Calling the API
url = 'https://taxifare.lewagon.ai/predict'

#pickup_datetime='2012-10-06 10:20:00'
#pickup_longitude=40.7614327
#pickup_latitude=-73.9798156
#dropoff_longitude=40.6513111
#dropoff_latitude=-73.8803331
#passenger_count=2

params = {
    #'day': day_inp,
    #'time': time_inp,
    'pickup_datetime': pickup_datetime_inp,
    'passenger_count': passenger_count_inp,
    'pickup_longitude': float(pickup_longitude_inp),
    'pickup_latitude': float(pickup_latitude_inp),
    'dropoff_longitude': float(dropoff_longitude_inp),
    'dropoff_latitude': float(dropoff_latitude_inp)
    }

if st.button('Check fare'):
    response = requests.get(url, params=params)
    st.write(response.json()['prediction'])

#NY map
df = pd.DataFrame(np.expand_dims(np.array([40.7128, -74.0060]), axis = 1).T, columns=['lat', 'lon'])
st.map(df)
