a=int(input())
for i in range(1,a+1):
    for sp in range(0,a-i):
        print(" ",end="")
    for j in range (0,2*i-1):
        print("*",end="")
    print()
for i in range(a-1,0,-1):
    for sp in range(0,a-i):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()

another method

h=int(input())
for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))

