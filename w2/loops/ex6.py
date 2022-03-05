n = int(input('Please Enter a Number '))
while n > 0:
    # check even and odd
    if n % 2 == 0:
        print(n, 'is an even number')
    else:
        print(n, 'is an odd number')
    # decrease number by 1 in each iteration
    n = n - 1