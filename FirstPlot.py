from matplotlib.pyplot import figure, show
import numpy as npy
from numpy.random import rand
import json


#https://stackoverflow.com/questions/7908636/possible-to-make-labels-appear-when-hovering-over-a-point-in-matplotlib


if 1: # picking on a scatter plot (matplotlib.collections.RegularPolyCollection)

    debt = []
    salary = []
    names = []

    with open('schools.json', 'r') as infile:
        data = json.loads(infile.read())

    # pprint( data )

    schools = data['Results']
    for school in schools:
        if type(school['latest.aid.median_debt.completers.overall']) == type(None) or type(school['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings']) == type(None):
            continue

        debt.append(school['latest.aid.median_debt.completers.overall']);
        salary.append(school['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings'])
        names.append(school['school.name'])

    x, y, c, s = rand(4, 100)
    def onpick3(event):
        ind = event.ind
        print( 'onpick3 scatter:', ind, npy.take(debt, ind), npy.take(salary, ind), npy.take(names, ind))

    fig = figure()

    ax1 = fig.add_subplot(111)
    col = ax1.scatter(debt, salary, picker=True)
    #fig.savefig('pscoll.eps')
    fig.canvas.mpl_connect('pick_event', onpick3)

show()

# x = [1,2,3,4]
# y = [3,4,8,6]
# matplotlib.pyplot.scatter(x,y)
# matplotlib.pyplot.show()
