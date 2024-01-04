from matplotlib import pyplot
from pandas import read_csv
dataset = read_csv('ds_salaries(kaggle).csv')
dataset.hist()
pyplot.show()

from matplotlib import pyplot
from pandas import read_csv
dataset = read_csv('ds_salaries(kaggle).csv')
d = dataset.head(10)
d.plot(kind='bar', subplots=True, layout=(2, 2))
pyplot.show()