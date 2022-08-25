import csv
import json

csvFilePath = 'covid_19_data.csv'
jsonFilePath = 'json_covid_19.json'

data = {}

with open(csvFilePath) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for rows in csvReader:
    id = rows['SNo']
    data[id] = rows

with open(jsonFilePath, 'w') as jsonFile:
  jsonFile.write(json.dumps(data, indent=4))

print(id)

def animate(frame):
  ax.set_xlim(0, len(confirmed_cases)-1)
  ax.set_ylim(0, int(max(confirmed_cases))*2)

  list_x.append(frame)
  list_y.append(confirmed_cases[frame])

  ax.plot(list_x, list_y)

my_animation = animation.FuncAnimation(fig, animate, frames=len(confirmed_cases), interval = 100, repeat=Fales)