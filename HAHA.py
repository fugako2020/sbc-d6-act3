


n = int(input("Enter the number of rows: "))


i = n


while i > 0:
    print("*" * i)
    i -= 1


print("*" + " " * (n - 2) + "*")


i = 2


while i <= n:
    print("*" * i)
    i += 1

