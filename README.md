# PRODIGY_DS_01
from matplotlib import pyplot
from pandas import read_csv
dataset = read_csv('ds_salaries.csv')
dataset.hist()
pyplot.show()

from matplotlib import pyplot
from pandas import read_csv
dataset = read_csv('ds_salaries.csv')
d = dataset.head(10)
d.plot(kind='bar', subplots=True, layout=(2, 2))
pyplot.show()
