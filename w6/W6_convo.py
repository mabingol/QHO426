with open("harry.txt") as h:
    with open("john.txt") as j:
        h_lines = h.readlines()
        j_lines = j.readlines()
        
for i in range(len(j_lines)):
    print(f"\033[92mJohn_says: {j_lines[i]}\033[0m", end = "")
    print(f"\033[95mHarry_says: {h_lines[i]}\033[43m", end = "")