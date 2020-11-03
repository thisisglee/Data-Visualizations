import csv
import matplotlib.pyplot as plt
from datetime import datetime

class Weather():
	"""A class to get file name and plot data"""
	def __init__(self, filename):
		self.filename = filename
		self.highs, self.lows, self.dates = [],[],[]

		#open file
		self._open_file()


	def _open_file(self):
		"""open file"""
		try:
			with open(self.filename) as f:
				reader = csv.reader(f)
				header_row=next(reader)
				self.reader = reader
				self.header_row = header_row
		except Exception as e:
			raise e
		else:
			self.reader = reader
			self.header_row = header_row


	def index_value(self):
		"""return index value by enum loop"""
		for index, column_header in enumerate(self.header_row):
			print(index, column_header)

	def plot_graph(self, date_column, high_temp_column, low_temp_column):
		with open(self.filename) as f:
			reader = csv.reader(f)
			header_row=next(reader)
			self.reader = reader
			self.header_row = header_row
			for row in self.reader:
				date = datetime.strptime(row[int(date_column)],'%Y-%m-%d')
				try:
					high, low = float(row[int(high_temp_column)]),float(row[int(low_temp_column)])
				except Exception as e:
					# continune or remove can also work
					print(f'Missing data for {date}')
					
				else:
					self.highs.append(high)
					self.lows.append(low)
					self.dates.append(date)
		return(self.highs, self.lows, self.dates)

		

