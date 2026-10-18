def remove_duplicate_characters(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

s = str(input("Enter a string to remove duplicate characters : "))
print("String after removing duplicates :", remove_duplicate_characters(s))