import numpy as np
def main():
    print("Matrix Operations Program\n-----------------------------")
    r1,c1 = map(int,input("Enter rows and cols of Matrix A : ").split())
    print("Enter the elemetns of Matrix A :")
    A = np.array([list(map(int,input().split())) for _ in range(r1)])
    r2,c2 = map(int,input("Enter rows and cols of Matrix B : ").split())
    print("Enter the elemetns of Matrix B :")
    B = np.array([list(map(int,input().split())) for _ in range(r2)])
    while True:
        print("Choose Operation :\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Determinant\n6. Inverse\n7. Exit")
        choice = int(input("Enter choice : "))
        if choice == 1:
            if A.shape == B.shape:
                print("Result :",A+B)
            else:
                print("Addition not possible (dimension mismatch)")
        elif choice == 2:
            if A.shape == B.shape:
                print("Result :",A-B)
            else:
                print("Subtraction not possible (dimension mismatch)")
        elif choice == 3:
            if A.shape[1] == B.shape[0]:
                print("Result :",A@B)
            elif A.shape[0] == B.shape[1]:
                print("Result :",B@A)
            else:
                print("Multiplication not possible (dimension mismatch)")
        elif choice == 4:
            print("Transpose of A :",A.T)
            print("Transpose of B :",B.T)
        elif choice == 5:
            if A.shape[0] == A.shape[1]:
                print("Determinant of A :",np.linalg.det(A))
            else:
                print("Determinant not possible for A (not a square matrix)")
            if B.shape[0] == B.shape[1]:
                print("Determinant of B :",np.linalg.det(B))
            else:
                print("Determinant not possible for B (not a square matrix)")    
        elif choice == 6:
            if A.shape[0] == A.shape[1]:
                print("Inverse of A :",np.linalg.inv(A))
            else:
                print("Inverse not possible for A (not a square matrix)")
            if B.shape[0] == B.shape[1]:
                print("Inverse of B :",np.linalg.inv(B))
            else:
                print("Inverse not possible for B (not a square matrix)")
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()