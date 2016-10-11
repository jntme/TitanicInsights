
import csv
import numpy as np

csv_obj = csv.reader(open('../data/train.csv', 'rb'))
header = csv_obj.next()

print header
