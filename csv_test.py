import pandas as pd

df1 = pd.read_csv('csv finals/gas_chart.csv')
df2 = pd.read_csv('csv finals/diesel_chart.csv')
# print(df.values)

def find_gallons_gas(measurement):
	for x in df1.values:
		if x[0] == measurement:
			return float(x[1])

def find_gallons_diesel(measurement):
	for x in df2.values:
		if x[0] == measurement:
			return float(x[1])

print(find_gallons_gas('1-1/2"'))