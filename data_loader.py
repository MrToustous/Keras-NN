import pandas as pd
import numpy as np
import pandas_datareader as pdr


def data_window(data, start = None, end = None):
	if not start:
		start_date = data.index[0]
	else:
		start_date = pd.to_datetime(start, dayfirst=True)
	    
	if not end:
		end_date = data.index[-1]
	else:
		end_date = pd.to_datetime(end,  dayfirst=True)

	return data.loc[pd.to_datetime(start_date, dayfirst = True):pd.to_datetime(end_date, dayfirst = True)]


class ticker():

	def __init__(self, ticker):
		self.ticker = ticker

	def get_data(self):
		self.data = pdr.get_data_yahoo(self.ticker)

	def get_logreturns(self):
		self.logreturns = pd.DataFrame(np.log(self.data['Adj Close']).diff(), index = self.data.index[1:])

	def create_dataset(self, look_back = 1):
		self.get_logreturns()

		dataX, dataY, index = [], [], []
		for i in range(len(self.data) - look_back - 1):
			vect = self.logreturns.iloc[i:i+look_back, 0].values
			dataX.append(vect)
			dataY.append(self.logreturns.iloc[i+look_back, 0])
			index.append(self.logreturns.index[i+look_back])
		
		dataX = np.array(dataX)
		# print(dataY)
		self.dataset =  pd.DataFrame({**{'X(t-{0})'.format(look_back-i): dataX[:, i] for i in range(look_back)}, 'Y': dataY}, index = index)



	




