#with open('vegetables.csv') as f:
#   vegetables = f.read()

#print(vegetables)

import json

with open('superheroes.json', 'r') as f:
    data = json.load(f)

print(data)


for hero in data:
    print(hero)

import csv

with open('superheroes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])
    for hero in data:
        writer.writerow([hero['name'],hero['age'],hero['secretidentity'],hero['powers'],hero['squadName'],hero['homeTown'],hero['formed'],hero['secretBase'],hero['active']])