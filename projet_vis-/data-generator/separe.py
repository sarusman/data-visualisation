import csv


def each_year():
	t=2010
	g=0
	fr=[]
	for i in range(11):
		data=[]
		with open("colonnes_extraites.csv", "r") as f:
			with open(str(t)+'.csv', 'w') as fichier_sortie:
				for line in f:
					date=line.split(",")[1]
					try:
						if int(date[0:4])==t:
							fichier_sortie.write(line)
					except:
						pass
			t+=1


	print(g)



each_year()