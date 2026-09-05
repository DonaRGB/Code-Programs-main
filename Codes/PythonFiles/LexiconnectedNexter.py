def nextLexiconigraphicallyContinuationOfTheWord(s):
    s = s.lower()
    if s == "":
        return "a"
    i = len(s)-1
    while s[i] == "z" and i >= 0:
        i -= 1
    if i == -1:
        return s + "a"
    return s.replace(s[i],chr(ord(s[i])+1),1)

i = str(input("Enter a word :"))
print(f"Lexiconically next word : {nextLexiconigraphicallyContinuationOfTheWord(i)}")