import matplotlib.pyplot as plt

x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,s=10)

#set chart title and label axis
ax.set_title("Cube of Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cube of Values",fontsize=14)

# set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()