import numpy as np
import plotly.express as px
import csv

def getDataSource(data_path):
  days_present = []
  marks = []
  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      days_present.append(float(row["Days Present"]))
      marks.append(float(row["Marks In Percentage"]))

  return{"x":days_present,"y":marks}

def findCorrelation(data_source):
  correlation=np.corrcoef(data_source["x"],data_source["y"])
  print("Correlation is:\n",correlation[0,1])

def setup():
  data_path="Student Marks vs Days Present.csv"
  data_source = getDataSource(data_path)
  findCorrelation(data_source)

setup()