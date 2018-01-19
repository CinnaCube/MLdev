import numpy as numpy
from fileToDataset import fileToDatasetFunc

def standardize(data):

    data_standardized = numpy.zeros(numpy.shape(data))

    #geringsten und hoechsten Wert finden
    minValue = data.min(0)
    maxValue = data.max(0)

    #Entfernung zwischen min und max errechnen
    rangeofdata = maxValue - minValue

    #Anzahl daten bestimmen
    data_count = data.shape[0]

    print(data.shape)

    return 1
    #return data_standardized, rangeofdata, minValue

dataSet, classLabelVector, classColorVector = fileToDataset("../data/DataSet.txt")
standardize(dataSet)