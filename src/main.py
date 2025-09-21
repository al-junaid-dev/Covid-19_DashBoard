import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

url = "https://disease.sh/v3/covid-19/countries
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data) #Raw data extracted from the source
    # Keeping important fields
    df = df[['country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'active', 'tests', 'population']]

    # Filling empty data with 0
    df = df.fillna(0)

    # Calculating per million stats
    df['Cases_per_Million'] = (df['cases'] / df['population']) * 1_000_000
    df['Deaths_per_Million'] = (df['deaths'] / df['population']) * 1_000_000

    # Calculating recovery and fatality rates
    df['Recovery_Rate'] = ((df['recovered'] / df['cases']) * 100).round(2)
    df['Fatality_Rate'] = ((df['deaths'] / df['cases']) * 100).round(2)

    # Sorting by most affected countries
    df = df.sort_values(by="cases", ascending=False).reset_index(drop=True)

    # Storing the data 
    df.to_excel('covid_19_dashboard/data/covid_data.xlsx',index=False)

    top10 = df.head(10)
    
    with PdfPages("covid_19_dashboard/data/covid_dashboard.pdf") as pdf:
    # Plot 1: New cases & deaths
        plt.figure(figsize=(10,5))
        plt.plot(top10['country'], top10['cases'], label='Cases', color='blue')
        plt.plot(top10['country'], top10['deaths'], label='Deaths', color='red')
        plt.title("COVID-19 Cases & Deaths")
        plt.xlabel("Country"); plt.ylabel("Count")
        plt.legend(); plt.grid(True)
        pdf.savefig()  # save the current figure
        plt.close()

    # Plot 2: Recovery vs Fatality
        plt.figure(figsize=(10,5))
        plt.plot(top10['country'], top10['Recovery_Rate'], label='Recovery Rate %', color='green')
        plt.plot(top10['country'], top10['Fatality_Rate'], label='Fatality Rate %', color='orange')
        plt.title("Recovery vs Fatality Rates")
        plt.xlabel("country"); plt.ylabel("Percentage")
        plt.legend(); plt.grid(True)
        pdf.savefig()
        plt.close()
        print("Dashboard PDF created successfully!")

    #Plotting Graph using matplotlib
    plt.figure(figsize=(12,6))
    plt.bar(top10['country'], top10['cases'], color='blue', alpha=0.7, label='Total Cases')
    plt.bar(top10['country'], top10['deaths'], color='red', alpha=0.7, label='Deaths')
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.title("Top 10 Countries - COVID-19 Cases & Deaths")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

else :
    print('Unable to fetch the dat due to status code :',response.status_code)