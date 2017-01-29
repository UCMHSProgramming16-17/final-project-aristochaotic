import TheBlueAlliance as tba
import tbat
import requests
import json
from bokeh.plotting import figure, output_file, save
from bokeh.charts import Line, output_file, save
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

#will store latitude and longitude of frc teams
ltd = []
lng = []

#declare source to hold ltd and lng values and later plot points on the map
source = 0

teams = tbat.get_team_list(0)

for i in teams:
    #find the location of each team
    location = i['location']
    try:
        #find the address of each team and append them to the ltd and lng lists
        url = 'https://maps.googleapis.com/maps/api/geocode/json?=' 
        payload = {'key':'AIzaSyA4wsCs62yzwzy2HlUVg9tnRPMO2AA9qb4', 'address':location}
        r = requests.get(url, params=payload)
        locInfo = r.json()
        
        ltd.append(float(locInfo['results'][0]['geometry']['location']['lat']))
        lng.append(float(locInfo['results'][0]['geometry']['location']['lng']))
    except IndexError:
        continue
    
    #find the address of each team and append them to the ltd and lng lists
    url = 'https://maps.googleapis.com/maps/api/geocode/json?=' 
    payload = {'key':'AIzaSyA4wsCs62yzwzy2HlUVg9tnRPMO2AA9qb4', 'address':location}
    r = requests.get(url, params=payload)
    locInfo = r.json()
    

    try:
        # Python will try to do the code inside this block
        ltd.append(float(locInfo['results'][0]['geometry']['location']['lat']))
        lng.append(float(locInfo['results'][0]['geometry']['location']['lng']))
    except:
        # If the block above fails, this block will run
        # You can be specific and limit it based on specific exceptions, but I don't think you need to worry about that
        # If you wanted to do that for the IndexError you were getting, it would look like the line below:
        # except IndexError:
        print("Couldn't get a location for team %s" % i['team_number'])
    
    source = ColumnDataSource(
        data=dict(
            lat=ltd,
            lon=lng
        )
    )

mapstyle = json.loads(json.dumps('[{"elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"landscape.natural","elementType":"geometry.fill","stylers":[{"color":"#f5f5f2"},{"visibility":"on"}]},{"featureType":"administrative","stylers":[{"visibility":"off"}]},{"featureType":"transit","stylers":[{"visibility":"off"}]},{"featureType":"poi.attraction","stylers":[{"visibility":"off"}]},{"featureType":"landscape.man_made","elementType":"geometry.fill","stylers":[{"color":"#ffffff"},{"visibility":"on"}]},{"featureType":"poi.business","stylers":[{"visibility":"off"}]},{"featureType":"poi.medical","stylers":[{"visibility":"off"}]},{"featureType":"poi.place_of_worship","stylers":[{"visibility":"off"}]},{"featureType":"poi.school","stylers":[{"visibility":"off"}]},{"featureType":"poi.sports_complex","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#ffffff"},{"visibility":"simplified"}]},{"featureType":"road.arterial","stylers":[{"visibility":"simplified"},{"color":"#ffffff"}]},{"featureType":"road.highway","elementType":"labels.icon","stylers":[{"color":"#ffffff"},{"visibility":"off"}]},{"featureType":"road.highway","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"road.arterial","stylers":[{"color":"#ffffff"}]},{"featureType":"road.local","stylers":[{"color":"#ffffff"}]},{"featureType":"poi.park","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"poi","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#71c8d4"}]},{"featureType":"landscape","stylers":[{"color":"#e5e8e7"}]},{"featureType":"poi.park","stylers":[{"color":"#8ba129"}]},{"featureType":"road","stylers":[{"color":"#ffffff"}]},{"featureType":"poi.sports_complex","elementType":"geometry","stylers":[{"color":"#c7c7c7"},{"visibility":"off"}]},{"featureType":"water","stylers":[{"color":"#a0d3d3"}]},{"featureType":"poi.park","stylers":[{"color":"#91b65d"}]},{"featureType":"poi.park","stylers":[{"gamma":1.51}]},{"featureType":"road.local","stylers":[{"visibility":"off"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"visibility":"on"}]},{"featureType":"poi.government","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"landscape","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"visibility":"simplified"}]},{"featureType":"road.local","stylers":[{"visibility":"simplified"}]},{"featureType":"road"},{"featureType":"road"},{},{"featureType":"road.highway"}]'))

#configure options
map_options = GMapOptions(map_type="hybrid", styles=mapstyle)

#plot the map
plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
)

plot.title.text='FRC Team Locations'
    
circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)
