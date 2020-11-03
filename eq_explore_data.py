import json

#explore the structure of the JSON
filename = 'data/eq_1_day_ml.json'
with open(filename) as f:
	all_eq_data = json.load(f)

# To make the readable file
# readable_file='data/readable_eq_data.json'
# with open(readable_file,'w') as f:
# 	json.dump(all_eq_data, f, indent=4)

#list that cvorresponds to evety earthquake
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats=[],[],[]
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon,lat = eq_dict['geometry']['coordinates'][0], eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

