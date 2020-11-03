#to plot and style individual points
import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# s is to size the point
#ax.scatter(x_values, y_values,c='red',s=10)
#values closer to 0 produce darker color and closer to 1 produces lighter color
ax.scatter(x_values, y_values,c=(0,0.8,0),s=10)
#Colormap- is a gradient from one color to another
#ax.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues,s=10)

#set chart title and label axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Sqaure of Values",fontsize=14)

# set size of tick labels.
#ax.tick_params(axis='both', which='major', labelsize=14)

#set the range of the axes
ax.axis([0, 1100, 0,1100000])

#plt.show()

#to save graphs as image ( but make sure to replace 
plt.savefig('squares_plot.png', bbox_inches='tight')