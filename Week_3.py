
# coding: utf-8

# # Importing Libraries

# In[1]:


import pandas as pd
import numpy as np 


# # Reading Data

# In[44]:


dt=pd.read_csv("C:/Users/FERNANDO/Desktop/raw_data_coursera.csv")


# # Filtering rows which no have Borough information 

# In[45]:


dt=dt[dt["Borough"]!='Not assigned'].reset_index(drop=True)


# # Completing information

# In[46]:


dt['Neighbourhood'].loc[dt["Neighbourhood"]=='Not assigned']=dt['Borough']


# # Printing shape

# In[47]:


dt.shape


# # Part 2

# In[69]:


coordinates=pd.read_csv("C:/Users/FERNANDO/Desktop/Geospatial_Coordinates.csv")


# In[82]:


coordinates.columns=['Postcode', 'Latitude', 'Longitude']


# In[84]:


df = pd.merge(dt,coordinates, how='left', on='Postcode')


# In[89]:


import folium
from geopy.geocoders import Nominatim 


# In[90]:


address = 'Toronto, Canada'

geolocator = Nominatim()
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of the City of Toronto are {}, {}.'.format(latitude, longitude))


# In[92]:


map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(df['Latitude'], df['Longitude'], df['Borough'], df['Neighbourhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=3,
        popup=label,
        color='green',
        fill=True,
        fill_color='#3199cc',
        fill_opacity=0.3,
        parse_html=False).add_to(map_toronto)  
    
map_toronto

