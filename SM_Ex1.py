import json
import csv

json_fichier = 'data.json'
csv_fichier = 'Nombres_complexes.csv'

with open(json_fichier, 'r') as f1:
    data = json.load(f1)

with open(csv_fichier, 'w', newline='') as f2:
    ecrit = csv.writer(f2)
    ecrit.writerow(['reel', 'imaginaire'])
    for nombre_complexe in data["Nombres complexes"]:
        #print(nombre_complexe[0], nombre_complexe[1])
        ecrit.writerow([nombre_complexe[0], nombre_complexe[1]])
#print(data)
