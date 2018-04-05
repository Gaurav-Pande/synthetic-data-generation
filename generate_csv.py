from random import randrange
from datetime import datetime, timedelta
import pandas as pd
import csv
import time
import numpy as np
from math import sqrt
#bi = np.random.binomial(n=100, p=0.5, size=10000)
#n = np.random.normal(100*0.5, sqrt(100*0.5*0.5), size=4350)
n = np.random.poisson(60,145)
#startdate = datetime(2017,1,1,13,00)

def random_date(start,l):
   #dates = list(pd.date_range(start, start + timedelta(days=30)))
   #date_list = [base - timedelta(days=x) for x in range(0, numdays)]
   current = start
   while l >= 0:
     current = current + timedelta(minutes=10)
     yield current
     l-=1


#----------------------------------------------------------------------
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def a(num):
    for x in num:
        yield x

if __name__=='__main__':
  #csv = open("data.csv", "w") 
  numdays=1
  base = datetime.today()
  date_list = [base - timedelta(days=x) for x in range(0, numdays)]
  timestamp = []
  nump=a(n)
  index=0;
  for date in date_list:
    for x in reversed(list(random_date(date,144))):
      timestamp.append(x.strftime("%d/%m/%Y %H:%M").split(" "))
      #print x.strftime("%d/%m/%y %H:%M")
  for time in timestamp:
	  print time
  for i,j in zip(timestamp,nump):
      i.insert(0,index)
      i.insert(0,index)
      i.append(j)
      index=index+1

  path="data.csv"
  csv_writer(timestamp,path)


