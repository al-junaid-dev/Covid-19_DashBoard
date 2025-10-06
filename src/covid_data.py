import requests
import pandas as pd
import numpy as np

def fetch_covid_data():
    """
    Fetch live COVID-19 country-level data using disease.sh API
    Returns a cleaned pandas DataFrame with necessary columns.
    """
    url = "https://disease.sh/v3/covid-19/countries"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    data = r.json()
    
    df = pd.DataFrame(data)
    
    # Extract iso3 codes
    df['iso3'] = df.get('countryInfo', [{}]).apply(lambda ci: ci.get('iso3') if isinstance(ci, dict) else None)
    
    # Keep important columns
    cols = ['country', 'iso3', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'active', 'tests', 'population']
    for c in cols:
        if c not in df:
            df[c] = 0

    # Compute per-million metrics
    df['cases_per_million'] = (df['cases'] / df['population']) * 1_000_000
    df['deaths_per_million'] = (df['deaths'] / df['population']) * 1_000_000
    df['recovery_rate'] = ((df['recovered'] / df['cases']) * 100).round(2)
    df['fatality_rate'] = ((df['deaths'] / df['cases']) * 100).round(2)
    
    df = df.fillna(0)
    return df[cols + ['cases_per_million','deaths_per_million','recovery_rate','fatality_rate']]
