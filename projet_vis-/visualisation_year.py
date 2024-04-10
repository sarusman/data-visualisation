import pandas
import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt

final=[[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],]
date=[0,0,0,0,0,0,0,0,0,0,0,0]
temp=0
plt.figure(figsize=(15, 7))

satoshi="2013"  # METTEZ L'ANNÉE QUE VOUS VOULEZ VISUALISER (2015, 2020) sont obsolètes

with open(f"data/data-meteo-annees/{satoshi}.csv") as f:
	reads=csv.reader(f)
	count=0
	for i in reads:
		if count>=1:
			mois=int(i[1].split("-")[1])-1
			final[mois][0]=mois
			if i[2]!="":
				final[mois][1]+=int(float(i[2]))
			count=1
			date[mois]+=1
		count+=1



print(final)
print(date)
mois=["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
for i in range(len(final)):
	try:
		final[i]=(mois[i], (final[i][1]/date[i]-273.1))
	except:
		pass
x, y = zip(*final)


for x_val, y_val in zip(x, y):
	print(y_val)
	plt.vlines(x=x_val, ymin=0, ymax=y_val, color='red', linestyle='dotted', alpha=0.5)
	plt.text(x_val, y_val, f'T°: {round(y_val)}', color='red', ha='right')

plt.xlabel("Mois (Janvier à Décembre)", color="green")
plt.ylabel("Température en (°)",  color="green")
plt.title("Évolution de la Température en fonction du mois de l'année "+satoshi, color="green")
plt.plot(x, y, marker='o', color="green")
plt.show()




