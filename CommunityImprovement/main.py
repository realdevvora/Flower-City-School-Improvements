import numpy as np
import json
import pandas as pd
import plotly.express as px

display_data=pd.read_excel('final.xlsx')

fig = px.scatter_mapbox(display_data, hover_name='school', lat='latitude', lon='longitude', color='avg_rating',
                        mapbox_style="stamen-terrain",  color_continuous_scale=['#8B0000', '#FFFF00', "#006400"], size = 'avg_rating')

fig.show()