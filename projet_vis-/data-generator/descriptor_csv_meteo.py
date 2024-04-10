import csv, leather
from matplotlib.pyplot import pyplot as plt
from datetime import datetime
from leather.data_types import Date

liste=[]
with open("meteo.csv", 'r') as file:
        reader = csv.reader(file)
        for r in reader:
            if r[8]!="td" and r[8]!="mq":
                temp=float(r[8])-273,15
                temp=str(temp)
                liste.append([ r[1],r[8]])
                print("Température "+temp+"DEG le "+r[1])

