import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups NY')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)   # laod the data
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])   # convert the first colum in date time
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done!")

# if show raw data is checked
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
# HISTOGRAME
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0] # creat histograme whit data
st.bar_chart(hist_values)

# MAP
hour_to_filter = st.slider('hour', 0, 23, 17)   # slide to chose hour
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]   # filtre by hours

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
