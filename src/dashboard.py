import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Fetching live data
url = "https://disease.sh/v3/covid-19/countries
data = requests.get(url).json()
df = pd.DataFrame(data)

# Streamlit dashboard
st.title("🦠 COVID-19 Real-Time Dashboard")
st.write("Live COVID-19 stats per country")

# Dropdown to select country
country = st.selectbox("Select Country", df['country'].unique())
country_data = df[df['country'] == country].iloc[0]

st.metric("Total Cases", f"{country_data['cases']:,}")
st.metric("Total Deaths", f"{country_data['deaths']:,}")
st.metric("Total Recovered", f"{country_data['recovered']:,}")

# Plot bar chart for top 10 countries
top10 = df.sort_values(by="cases", ascending=False).head(10)
st.bar_chart(top10.set_index("country")[["cases", "deaths"]])
st.write("Created by © Mohd Junaid | 2025 |  All Rights Reserved")