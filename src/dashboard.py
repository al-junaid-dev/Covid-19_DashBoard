import streamlit as st
import pandas as pd
import plotly.express as px
from covid_data import fetch_covid_data

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
st.title("🦠 COVID-19 Real-Time Dashboard")
st.markdown("Built with Python, Pandas, Plotly & Streamlit — © 2025 Mohd Junaid")

# Fetch data
df = fetch_covid_data()

# Sidebar filters
continent_list = ["All"] + sorted(df.get("continent", pd.Series()).dropna().unique().tolist())
selected_continent = st.sidebar.selectbox("Select Continent", continent_list, index=0)

if selected_continent != "All":
    df = df[df.get("continent") == selected_continent]

selected_country = st.sidebar.selectbox("Select Country", df['country'].tolist())

# Top-level metrics
st.markdown("## Global Overview")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Cases", f"{int(df['cases'].sum()):,}")
c2.metric("Total Deaths", f"{int(df['deaths'].sum()):,}")
c3.metric("Total Recovered", f"{int(df['recovered'].sum()):,}")
c4.metric("Active Cases", f"{int(df['active'].sum()):,}")
c5.metric("Total Tests", f"{int(df['tests'].sum()):,}")

st.markdown("---")

# Country summary
country_row = df[df['country']==selected_country].iloc[0]
st.markdown(f"### {selected_country} Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Cases", f"{country_row['cases']:,}", f"+{country_row['todayCases']:,}")
col2.metric("Deaths", f"{country_row['deaths']:,}", f"+{country_row['todayDeaths']:,}")
col3.metric("Recovered", f"{country_row['recovered']:,}")
col4.metric("Cases/Million", f"{country_row['cases_per_million']:.1f}")
st.markdown(f"**Recovery Rate:** {country_row['recovery_rate']:.2f}%  |  **Fatality Rate:** {country_row['fatality_rate']:.2f}%")

st.markdown("---")

# Top 10 countries chart
top10 = df.sort_values("cases", ascending=False).head(10)
fig_top = px.bar(top10.melt(id_vars=["country"], value_vars=["cases","deaths"], var_name="Metric", value_name="Count"),
                 x="country", y="Count", color="Metric", barmode="group", title="Top 10 Countries - COVID-19")
fig_top.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_top, use_container_width=True)

# World map
st.subheader("World Map")
map_metric = st.selectbox("Map Metric", ["cases", "deaths", "cases_per_million", "deaths_per_million"], index=0)
fig_map = px.choropleth(df, locations="iso3", color=map_metric, hover_name="country",
                        hover_data=["cases","deaths","cases_per_million"], title=f"COVID-19 - {map_metric.replace('_',' ').title()}",
                        projection="natural earth", height=500)
st.plotly_chart(fig_map, use_container_width=True)
