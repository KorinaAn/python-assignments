import json
import csv

with open('superheroes.json') as json_file:
	jsondata = json.load('superheroes.json')

data_file = open('superheroes.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0
for data in jsondata:
	if count == 0:
		header = data.keys("name", "age", "secretIdentity", "powers", "squadName", "homeTown", "formed", "secretBase", "active")
		csv_writer.writerow()
		count += 1
		csv_writer.writerow(data.values())


#import json
#import csv

#with open('superheroes.json') as json_file:
#	hero = json.load(json_file)

#heroes = hero['superheroes']
#csv_file = open('superheroes.csv', 'w')

#csv_writer = csv.writer(csv_file)
#count = 0

#for hero in superheroes:
#	if count == 0:
#		header_csv = e.keys()
#csv_writer.writerow(header_csv)
#count += 1
#csv_writer.writerow(e.values())

#csv_file.close()

