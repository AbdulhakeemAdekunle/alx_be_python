size = int(input("Enter the size of the pattern: "))
step = 1
while step <= size:
    for i in range(1, (size + 1)):
        print("*", end="")
    step += 1
    print()
