def Online(n):
    iteration = 0
    for _ in range(1,n+1):
        iteration += 1
    print(f"When n is {n}, iterations = {iteration}.")
Online(10)
Online(20)
Online(42)
print("\nWith every \"n\", the time taken and iterations will increase.")