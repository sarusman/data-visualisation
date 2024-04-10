import pandas
import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt

final=[[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],]
date=[0,0,0,0,0,0,0,0,0,0,0,0]
temp=0
plt.figure(figsize=(15, 7))


#DATA : https://www.parisaeroport.fr/groupe/finances/relations-investisseurs/trafic

anne="15" # REMPLACER L'ANNÉE ICI (2000 - 2024)

x=[]
y=[]
with open(f"data/data-tourisme/DATA-TOURISME.csv") as f:
	reads=csv.reader(f)
	count=0
	for i in reads:
		if count>1:
			if (i[0][4:6]==anne):
				x.append(i[0])
				y.append(int(i[3].replace(",", "")))
		count+=1



plt.xlabel("Mois (Janvier à Décembre)", color="green")
plt.ylabel("Nombre de Personnes",  color="green")
plt.title("Tourisme dans les aéroports de France à l'année 20"+anne, color="green")
plt.plot(x, y, marker='o', color="green")


plt.show()




