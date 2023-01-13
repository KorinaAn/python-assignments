#Write a python script called veggies.py that defines a list of dicts named vegetables

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#Write a python program that Loops through each vegetable
#In the loop, write the name of each vegetable and the color into a CSV called vegetables.csv

for veg in vegetables:
    print (veg)

import csv

with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow (["name", "color"])
    for veg in vegetables:
        writer.writerow([veg["name"],veg["color"]])
  


#with open('vegetables.csv', 'r') as f:
#    reader = csv.DictReader(f)
#   rows = list(reader)

#print(rows)