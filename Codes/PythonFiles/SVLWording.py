def smallest_largest_words(sentence):
    w = ""
    allwords = []
    sentence += " "
    for i in sentence:
        if i != " ":
            w += i
        else:
            if w != "":
                allwords.append(w)
            w = ""
    s = l = allwords[0]
    for k in all_words:
        if len(s) > len(k):
            s = k
        if len(l) < len(k):
            l = k
    return s,l

sentence = str(input("Enter a sentence : "))
s,l = smallest_largest_words(sentence)
print(f"Smallest Word : {s}\nLargest Word : {l}")