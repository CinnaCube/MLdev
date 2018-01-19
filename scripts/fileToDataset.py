#!/usr/bin/env python
import numpy as numpy
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D #Erweiterung für die Matplotlib - siehe: http://matplotlib.org/mpl_toolkits/

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def array_len(data):
    i = 0
    for item in data:
        i += 1
        pass
    return i

def fileToDataset(datafile):

    #Datei öffnen
    filestream = open(datafile)

    #Anzahl an Zeilen
    numberoflines = file_len(datafile)

    #Leeres multidimensionales Array initialisieren [numberoflines][3]
    numpyMat = numpy.zeros((numberoflines-1,3))

    classlabelvector = []
    classcolorvector = []

    #dateistrem zurücksetzen
    data = open(datafile)

    index = 0

    #Datei einlesen
    for line in data:
        if index != 0:

            #Zeile säubern
            line = line.strip()

            #Zeile durch Tabulator getrennte Werte aufteilen und in Array schreiben
            listFromLine = line.split("\t")

            #Zeile von Werten (2 bis ausschließlich 5 Werte) in mehrdimensionale Array schreiben
            numpyMat[index-1,:] = listFromLine[1:4]

            #5 Wert (Label)
            classLabel = listFromLine[4]

            #Farben je nach Art zuteilen
            if classLabel == 'Buero':
                color = 'yellow'
            elif classLabel == 'Wohnung':
                color = 'red'
            else:
                color = 'blue'

            #Label und Farbe in Array
            classlabelvector.append(classLabel)
            classcolorvector.append(color)

        index += 1

    return numpyMat,classlabelvector,classcolorvector

def standardize(data):

    data_standardized = numpy.zeros(numpy.shape(data))

    #geringsten und hoechsten Wert finden
    minValue = data.min(0)
    maxValue = data.max(0)

    #Entfernung zwischen min und max errechnen
    rangeofdata = maxValue - minValue

    #Anzahl daten bestimmen
    data_count = array_len(data)

    #Errechnen von standardisierten Werten. Formel: NormWert = (Wert - MinWert)/(MaxWert - MinWert)
    data_standardized = data - numpy.tile(minValue, (data_count, 1))
    data_standardized = data_standardized / numpy.tile(maxValue - minValue, (data_count, 1))

    return data_standardized, rangeofdata, minValue

#def

dataSet, classLabelVector, classColorVector = fileToDataset("../data/DataSet.txt")
data_standardized, rangeofdata, minValue = standardize(dataSet)