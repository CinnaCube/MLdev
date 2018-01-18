#!/usr/bin/env python
import numpy as numpy
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D #Erweiterung für die Matplotlib - siehe: http://matplotlib.org/mpl_toolkits/

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def fileToDataset(datafile):

    filestream = open(datafile)

    numberoflines = file_len(datafile)
    #print(file_len(datafile))

    numpyMat = numpy.zeros((numberoflines-1,3))

    classlabelvector = []
    classcolorvector = []

    #print(numpyMat)

    data = open(datafile)
    index = 0

    for line in data:
        if index != 0:
            line = line.strip()
            listFromLine = line.split("\t")

            numpyMat[index-1,:] = listFromLine[1:4]

            classLabel = listFromLine[4]

            if classLabel == 'Buero':
                color = 'yellow'
            elif classLabel == 'Wohnung':
                color = 'red'
            else:
                color = 'blue'

            classlabelvector.append(classLabel)
            classcolorvector.append(color)

        index += 1

    #return "1"
    return numpyMat,classlabelvector,classcolorvector

dataSet, classLabelVector, classColorVector = fileToDataset("../data/DataSet.txt")
#data = Dataread('../data/DataSet.txt')


