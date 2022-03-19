def dimensions():
    w = float(input("Enter the width: "))
    l = float(input("Enter the length: "))
    return w, l #Returning a tuple

def calc_area(l, w):
    return l*w

def r_name():
    return input("Enter name of the room: ")

def price(name, area):
    if name.lower() == "bathroom":
        return 3*area
    elif name.lower() == "bedroom":
        return 2*area
    elif name.lower() == "kitchen":
        return 4*area
    elif name.lower() == "living room":
        return 2*area
    else:
        return 5*area

def run():
    t_price = 0
    num = int(input("How many rooms to clean? "))
    for i in range(num):
       name = r_name()
       x, y = dimensions()
       area = calc_area(x,y)
       t_price += price(name, area)

    print(f"Your total is £{t_price:.2f}")
  
run()