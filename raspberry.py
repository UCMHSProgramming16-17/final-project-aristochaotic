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

#will store latitude and longitude of frc teams
ltd = []
lng = []

teams = tbat.get_all_teams()

for i in teams:
    #find the location of each team
    location = i['location']
    
    #find the address of each team and append them to the ltd and lng lists
    url = 'https://maps.googleapis.com/maps/api/geocode/json?=' 
    payload = {'key':'AIzaSyA4wsCs62yzwzy2HlUVg9tnRPMO2AA9qb4', 'address':location}
    r = requests.get(url, params=payload)
    locInfo = r.json()
    
    ltd.append(float(locInfo['results']['geometry']['location']['lat']))
    lng.append(float(locInfo['results']['geometry']['location']['lng']))
    
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

plot.title.text='FRC Team Locations'
    
circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)
