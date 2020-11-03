import json
import geojson

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#explore the structure of the JSON
filename = 'data/eq_data_30_day_ml.json'
with open(filename) as f:
	all_eq_data = json.load(f)

mags, lons, lats, hover_texts =[],[],[],[]
title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']
for eq_dict in all_eq_dicts:
	mags.append(eq_dict['properties']['mag'])
	lons.append(eq_dict['geometry']['coordinates'][0])
	lats.append(eq_dict['geometry']['coordinates'][1])
	hover_texts.append(eq_dict['properties']['title'])

#Map the earthquakes,
#data = [Scattergeo(lon=lons, lat=lats)]

#best way to customize PLotly charts
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'text': hover_texts,
	'marker':{
		'size':[5*mag for mag in mags],
		'color':mags,
		'colorscale':'Hot',
		'reversescale':True,
		'colorbar':{'title':'Magnitude'},
	}
}]

my_layout = Layout(title=title)

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')