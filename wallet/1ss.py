import numpy as np
import random
import sys

a = random.randint(-20, 20)
b = random.randint(-20, 20)
secret = 13

if (len(sys.argv) > 1):
    secret = int(sys.argv[1])

seq = [a, b, secret]
f = np.poly1d(seq)
print("Secret equation:\n", f)

print("\nSecret: ", f(0))
print("Bob: ", f(1))
print("Carol: ", f(2))
print("Dave: ", f(3))
print("Alice: ", f(4))
print("New: ", f(5))

#######################################
x = [1, 2, 5]
y = [f(1), f(2), f(5)]
res = np.polyfit(x, y, 2)
print("\nSecret equation: ", res)
print("Secret: ", int(round(res[2], 0)))
