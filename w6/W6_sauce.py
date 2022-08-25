def populate(path):
    with open(path, "w") as f:
        while True:
            sauce  = input("Enter a sauce (or stop): ")
            if sauce.lower() == "stop":
                break
            f.write(sauce + "\n")


def read_sauce(path):
    with open(path) as f:
        print(f.read())

read_sauce("s1.txt")
read_sauce("s2.txt")