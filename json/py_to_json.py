import json

# a Python object (dict):

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = ")))

# To convert JSON to Pyton 
# y = json.loads(x)

# To convert Python or csv to JSON 
#x = json.dumps(y)

