def ONSquared(n):
    iteration = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*", end = " ")
            iteration += 1
        print("")
    print(f"\nWhen n is {n}, iterations = {iteration}")
ONSquared(5)
ONSquared(4)
ONSquared(3)
print("\nWith every \"n\", the time taken equals n^2.\nO(n^2)")