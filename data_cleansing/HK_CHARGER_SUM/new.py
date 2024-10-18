import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def get_ev_data():
    import pandas as pd
    #df2 = pd.read_html('https://www.ii.uib.no/~petter/mountains/HongKong.html', header = 0)[0]
    #df2.dropna(inplace=True)

    #df2[['lat','lon']] = df2['Location (lat/lon)'].str.split(",", expand=True)
    
    #df2 = pd.read_csv('lpg_filling_station.csv')
    df2=pd.read_excel('EV_Charger.xlsx')
    #Longitude
    #Latitude
    df2 = df2.rename(columns={'LOCATION_EN': 'Name',
                            'GeometryLongitude': 'lon',
                            'GeometryLatitude': 'lat' })
    
    df2['lon']=pd.to_numeric(df2['lon'], errors='coerce')
    df2['lat']=pd.to_numeric(df2['lat'], errors='coerce')
    df2.dropna(inplace=True)
    
    return df2


latitude = 22.28552
longitude = 114.15769

st.title('HK EV charging stations location')

df2 = get_ev_data()

st.map(df2)


st.table(df2)

import plotly.express as px

fig2 = px.scatter_mapbox(df2, lat="lat", lon="lon", hover_name="Name",  size_max=15, zoom=10)
fig2.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig2)