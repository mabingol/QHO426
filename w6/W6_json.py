import json
from demos.W5_shop import shop as products

def write_json():
    with open("products.json", "w") as bob:
        dicto = products()
        json.dump(dicto, bob)

def read_json():
    with open("products.json") as jason:
        dicto = json.load(jason)
        total = 0
        for val in dicto.values():
            total += val
            print(val)
        print(f"{total/len(dicto)}")

read_json()
        