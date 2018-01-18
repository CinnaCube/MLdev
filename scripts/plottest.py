import matplotlib.pyplot as pyplot

dataset = [1,3,4]
dataset2 = [4,5,6]

fig = pyplot.figure()
ax = fig.add_subplot(1,1,1)
i = 0
#for x in dataset:
ax.scatter(dataset, dataset2)
    #i += 1
ax.set_xlabel('Anzahl Mitarbeiter')
ax.set_ylabel('Umsatz')
pyplot.show()