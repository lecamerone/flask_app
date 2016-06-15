import pandas.io.data as web
import datetime

start = datetime.datetime(2016,5,13)
end = datetime.datetime(2016,6,14)

def pandas_google_fin(strt, en):
	f = web.DataReader("F", 'google', start, end)
	print(f)
	return f

if __name__ == "__main__":
	pandas_google_fin(start, end)