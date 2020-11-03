from weather import Weather
import matplotlib.pyplot as plt
from datetime import datetime


def f_to_c(self,listname=[]):
	listname = [(((listname[i] - 32)*5)/9 for i in range(len(listname)))]
	return listname

#sitka weather
sitka = Weather('data/sitka_weather_07-2018_simple.csv')
#sitka.index_value()
sitka_x, sitka_y, sitka_dates = sitka.plot_graph(2,5,6)
#sitka_x = f_to_c(sitka_x)

death_valley = Weather('data/death_valley_2018_simple.csv')
#death_valley.index_value()
death_valley_x, death_valley_y, death_valley_dates = death_valley.plot_graph(2,4,5)


#Barrie Weather
barrie = Weather('data/weatherstats_barrie_daily.csv')
# barrie.index_value()
barrie_x, barrie_y, dates = barrie.plot_graph(1,3,6)

#PLot the high low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
# alpha is color transperacncey, 0-complete transparent, 1 to opaque
#sitka graph plot
ax.plot(sitka_dates, sitka_x, c='red', alpha=0.5)
# ax.plot(dates, sitka_y, c='blue', alpha=0.5)
# ax.fill_between(self.dates, self.highs, self.lows, facecolor='blue', alpha=0.1)
#death_valley graph plot
ax.plot(death_valley_dates, death_valley_x, c='green', alpha=0.5)
# # ax.plot(dates, death_valley_y, c='blue', alpha=0.5)
# # ax.fill_between(self.dates, self.highs, self.lows, facecolor='blue', alpha=0.1)
# #barrie graph plot
ax.plot(dates, barrie_x, c='blue', alpha=0.5)
#ax.plot(dates, barrie_y, c='blue', alpha=0.5)
# ax.fill_between(self.dates, self.highs, self.lows, facecolor='blue', alpha=0.1)


#format plot.
#Set chart title and label axes
ax.set_title("Daily high temperatures b/w \n Sitka, Death Valley, Barrie - 2018", fontsize=20)
ax.set_xlabel("", fontsize=16)
# to format x axes diagonaly
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
#Set size of tick labels.
ax.tick_params(axis='both', which='major',labelsize=16)
plt.show()