def update_str(string,i,c):
    n = len(string)
    if n <= 0:
        raise ValueError("String is empty")
    if i < 0 or i >= n:
        raise IndexError("Index out of range")
    return string[:i] + c + string[i+1:]
def delete_str(string,i):
    n = len(string)
    if n <= 0:
        raise ValueError("String is empty")
    if i < 0 or i >= n:
        raise IndexError("Index out of range")
    return string[:i] + string[i+1:]
s = str(input("Enter a string : "))
i1 = int(input("Enter the index to update : "))
c1 = str(input("Enter the character to update in the string : "))
print("Original String :",s)
print("Updated Character in String :",update_str(s,i1,c1))
i2 = int(input("Enter the index to delete : "))
print("Deleted Character in String :",delete_str(s,i2))