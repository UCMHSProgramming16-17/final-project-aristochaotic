import TheBlueAlliance as tba
import numpy as np
import pandas as pd
import tbat
import requests
from bokeh.plotting import figure, output_file, save
from bokeh.charts import Line, output_file, save
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

ltd = []
lng = []

teams = tbat.get_all_teams()

for i in teams:
    data = tbat.get_team_info(i)
    
    gurl = 'https://maps.googleapis.com/maps/api/geocode/json?=' #for location
    payload = {'key':'AIzaSyA4wsCs62yzwzy2HlUVg9tnRPMO2AA9qb4', 'address':data['location']}
    gr = requests.get(gurl, params=payload)
    locInfo = gr.json()
    
    ltd.append(float(locInfo['results'][0]['geometry']['location']['lat']))
    lng.append(float(locInfo['results'][0]['geometry']['location']['lng']))
    
    source = ColumnDataSource(
        data=dict(
            lat=ltd,
            lon=lng
        )
    )
 
map_options = GMapOptions(lat=ltd, lng=lng, map_type="hybrid", zoom=11)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
)

plot.title.text='FRC Teams'
    
circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)
