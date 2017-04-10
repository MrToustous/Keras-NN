import pandas as pd
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
		self.log_returns = pd.DataFrame(np.log(self.data['Adj Close']).diff(), index = data.index[1:])

	




