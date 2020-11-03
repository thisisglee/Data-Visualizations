import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename ='data/sitka_weather_07-2018_simple.csv'
#filename ='data/death_valley_2018_simple.csv'
#filename ='data/weatherstats_barrie_daily.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row=next(reader)
	#print(header_row)

	# #the enumerate function returns index and values of each item
	for index, column_header in enumerate(header_row):
		print(index, column_header)

	# #Get high,low temperatures and date from this file
	highs, lows, dates = [],[],[]
	#first_date = datetime.strptime('2018-07-01','%Y-%m-%d')
	# %A- wekday name like Monday, %B month name like November, %m- month number, %M - minutes 00 to 59, %S - seconds 00 to 61
	for row in reader:
		date = datetime.strptime(row[2],'%Y-%m-%d')
		try:
			high, low = int(row[5]),int(row[6])
		except Exception as e:
			# continune or remove can also work
			print(f'Missing data for {date}')
		else:
			highs.append(high)
			lows.append(low)
			dates.append(date)

	# print(highs)
	# print(lows)
	# print(dates)

#PLot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
#alpha is color transperacncey, 0-complete transparent, 1 to opaque
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
#fills color between one x and 2 y values, facecolor determines the color of the shaded region
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#format plot.
#Set chart title and label axes
ax.set_title("Daily high and low temperatures \n Sitka", fontsize=20)
ax.set_xlabel("", fontsize=16)
# to format x axes diagonaly
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
#Set size of tick labels.
ax.tick_params(axis='both', which='major',labelsize=16)
plt.show()