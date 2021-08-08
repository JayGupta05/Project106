from numpy.core.numeric import correlate
import plotly_express as px
import csv
import numpy as np

def getDataSource():
    marks = []
    present = []
    with open("Percentage.csv") as f:
        dictionary = csv.DictReader(f)
        for row in dictionary:
            marks.append(float(row["Marks In Percentage"]))
            present.append(float(row["Days Present"]))
    return{
        'x':marks, 'y':present
    }

def findCore(source):
    coorelation = np.corrcoef(source['x'],source['y'])
    print(coorelation[0,1])

source = getDataSource()
findCore(source)