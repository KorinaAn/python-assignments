import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
  
    # Convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=2)
        jsonf.write(jsonString)
          
csvFilePath = r'vegetables.csv'
jsonFilePath = r'output/vegetables.json'
csv_to_json(csvFilePath, jsonFilePath)
