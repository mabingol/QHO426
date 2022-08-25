import numpy as np
import random
import sys

a = random.randint(-20, 20)
b = random.randint(-20, 20)
secret = 12

if (len(sys.argv) > 1):
    secret = int(sys.argv[1])

seq = [a, b, secret]
f = np.poly1d(seq)
print("Secret equation:\n", f)

print("\nSecret: ", f(0))
print("Bob: ", f(1), end=' ')
print("Carol: ", f(2), end=' ')
print("Dave: ", f(3), end=' ')
print("Alice: ", f(4))

print("\nwe revoke Alice here")

g_x = np.poly1d([random.randint(-20, 20), random.randint(-20, 20), 0])
print("\nBob's new secret equation:\n", g_x)
h_x = np.poly1d([random.randint(-20, 20), random.randint(-20, 20), 0])
print("Carol's new secret equation:\n", h_x)
k_x = np.poly1d([random.randint(-20, 20), random.randint(-20, 20), 0])
print("Dave's new secret equation:\n", k_x)

carol_to_bob = h_x(1)
dave_to_bob = k_x(1)
print("\nBob new value: ", f(1) + g_x(1) + carol_to_bob + dave_to_bob)

bob_to_carol = g_x(2)
dave_to_carol = k_x(2)
print("Carol new value: ", f(2) + h_x(2) + bob_to_carol + dave_to_carol)

bob_to_dave = g_x(3)
carol_to_dave = h_x(3)
print("Dave new value: ", f(3) + k_x(3) + bob_to_dave + carol_to_dave)

####################################
print("\nNow lets verify")

f_new = f + g_x + h_x + k_x
print("New secret:\n", f_new)
print("\nSecret: ", f_new(0))
print("Bob: ", f_new(1), end=' ')
print("Carol: ", f_new(2), end=' ')
print("Dave: ", f_new(3), end=' ')
print("check_Alice_old: ", f_new(4), end=' ')

x = [1, 2, 3]
y = [f_new(1), f_new(2), f_new(3)]
res = np.polyfit(x, y, 2)

print("\nSecret equation: ", res)
print("Secret: ", int(res[2]))
