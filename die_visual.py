from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
import matplotlib.pyplot as plt

#Create a die
die_1 = Die()
die_2 = Die()

#Make some rolls and store the result
results = []

# for roll_num in range(1000):
# 	result = die_1.roll() * die_2.roll()
# 	results.append(result)
[results.append(die_1.roll() + die_2.roll()) for roll_num in range(1000)]

#print(results)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + 1
# for value in range(2, max_result):
# 	frequency = results.count(value)
# 	frequencies.append(frequency)
[frequencies.append(results.count(value)) for value in range(2, max_result)]

print(frequencies)
# print(dictfrequencies)

#Visualize the results
x_values = list(range(2, max_result))
# Bar() represents data will be formated as list
data = [Bar(x=x_values, y=frequencies)]

#dtick control spacing between tick marks on axis
x_axis_config = {"title":"Result","dtick":1}
y_axis_config = {"title":"Frequency of Result"}
my_layout = Layout(title='Results of rolling TWO D6 1000 times',
	xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, "layout":my_layout}, filename='d6_d6.html')

# #die rolling visualization
# plt.style.use('seaborn')

# fig, ax = plt.subplots()
# ax.plot(x_values, frequencies, linewidth=3)

# #Set chart title and label axes
# ax.set_title("Results of rolling TWO D6 1000 times", fontsize=24)
# ax.set_xlabel("Result", fontsize=14)
# ax.set_ylabel("Frequency of Result", fontsize=14)

# #Set size of tick labels.
# ax.tick_params(axis='both', labelsize=14)

# plt.show()

# #scatter visualization
# ax.scatter(x_values, frequencies, c=frequencies, cmap=plt.cm.Blues,s=10)
# #set chart title and label axis
# ax.set_title("Results of rolling TWO D6 1000 times", fontsize=24)
# ax.set_xlabel("Result", fontsize=14)
# ax.set_ylabel("Frequency of Result", fontsize=14)

# # set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()