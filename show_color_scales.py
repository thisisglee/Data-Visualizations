from plotly import colors
import json

#print(colors.PLOTLY_SCALES)

all_eq_data = colors.PLOTLY_SCALES

#To make the readable file
readable_file='data/readable_colors.json'
with open(readable_file,'w') as f:
	json.dump(all_eq_data, f, indent=4)