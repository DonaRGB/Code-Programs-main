def generate_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password
for _ in range(100):
    print(generate_password(10),end = "\n\n")