import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename='data/world_fires_1_day.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#get index
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)

	#get lons, lats of file
	lons, lats, brightness, hover_texts = [],[],[],[]
	title = "Global Fires"
	for row in reader:
		lons.append(row[1])
		lats.append(row[0])
		brightness.append(float(row[2])/200)
		hover_texts.append(f'Date - {row[5]}')


	#Map the fire,
	data = [Scattergeo(lon=lons, lat=lats)]

	#best way to customize PLotly charts
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'text': hover_texts,
	'marker':{
		'size':[5*bright for bright in brightness],
		'color':brightness,
		'colorscale':'Hot',
		'reversescale':True,
		'colorbar':{'title':'Magnitude'},
	}
}]

my_layout = Layout(title=title)

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')