
n = int(15)
for i in range (n):
    if i == 0 or i==n-1:
        print((i+(n-i))*" * ")
    else:
        if n%2 == 1:
            print( (int(n/2-1)) * ' * ', (" " * (i +(i-1))), (int(n/2)-int(1)) * ' * ' )
