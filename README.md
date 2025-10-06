# 🦠 COVID-19 Real-Time Dashboard  

A real-time interactive dashboard built with **Python, Pandas, Plotly, and Streamlit** to track the spread and impact of COVID-19 globally and by country.  
The data is fetched live using the [disease.sh API](https://disease.sh).  

---

## 🚀 Features  

- 🌍 **Global Overview** – Total cases, deaths, recoveries, active cases, and tests  
- 📊 **Country-Wise Metrics** – Real-time statistics with daily new cases and deaths  
- 🔝 **Top 10 Countries Visualization** – Bar chart comparing the most affected countries  
- 🗺️ **Interactive World Map** – Choropleth map to visualize cases, deaths, and per-million stats  
- 🎛️ **Filters** – Filter data by continent and country  
- ⚡ **Real-Time Updates** – Data is pulled live from the API each time you run the app  

---

## 📂 Project Structure  

```
covid19_dashboard/
│
├─ src/
│   ├─ covid_data.py         # Data fetching and cleaning
│   └─ dashboard.py          # Streamlit dashboard app
│
├─ requirements.txt          # Python dependencies
└─ README.md                 # Project documentation
```

---

## 🛠️ Installation & Setup  

1. Clone the repository  
```bash
git clone https://github.com/yourusername/covid19_dashboard.git
cd covid19_dashboard
```

2. Create a virtual environment (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3. Install dependencies  
```bash
pip install -r requirements.txt
```

4. Run the dashboard  
```bash
streamlit run src/dashboard.py
```

---

## 📊 Data Source  

All COVID-19 statistics are fetched from the [disease.sh API](https://disease.sh/), which provides reliable, community-maintained data.  

---

## 📸 Screenshots  

*(Add screenshots here after running the dashboard)*  

---

## 📌 Future Enhancements  

- Add historical trend analysis with time-series charts  
- Country-wise forecasting using Scipy curve fitting  
- Export reports to CSV, Excel, or PDF  

---

## 👨‍💻 Author  

**Mohd Junaid**  
📌 Engineering Student | Python & Data Science Enthusiast  
