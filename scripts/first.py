
import csv
import numpy as np

csv_obj = csv.reader(open('../data/train.csv', 'rb'))

header = csv_obj.next() #takes the first row (columns)

#print the headers
print header

data = []
for row in csv_obj:
    data.append(row)

data = np.array(data)

number_passengers = np.size(data[:,1].astype(np.float))
number_survived = np.sum(data[:,1].astype(np.float))

proportion_survivors = number_survived / number_passengers
print "\nSurviving probability over all: %0.2f" % proportion_survivors

print "\n============================="
print "=======People on board======="
print "============================="

print "Total on board: %s" % np.size(data[:,0])

women_only_stats = data[:,4] == "female" #take only women
women_onboard = data[women_only_stats, 1].astype(np.float) #use woman as a mask to get the survived column
print "women: \t\t\t%s" % np.size(women_onboard) #size = count of the dimensions of this vector

men_only_stats = data[:,4] != "female"


men_onboard = data[men_only_stats,1].astype(np.float)
print "men: \t\t\t%s" % np.size(men_onboard)
print "=============================\n"


proportion_woman_survived = np.sum(women_onboard) / np.size(women_onboard) #sum over list -> number of survivors
print "chance to survive as man: %0.2f" % proportion_woman_survived

proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
print "chance to survive as woman: %0.2f" % proportion_men_survived

#test
