import csv
import json

csvFilePath = 'covid_19_data.csv'
jsonFilePath = 'json_file_name.json'

data = {}
with open(csvFilePath) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for rows in csvReader:
    id = rows['SNo']
    data[id] = rows


with open(jsonFilePath, 'w') as jsonFile:
  jsonFile.write(json.dumps(data, indent=4))

def export_all(self):
  open('output.json', 'w').close()

  with open()

