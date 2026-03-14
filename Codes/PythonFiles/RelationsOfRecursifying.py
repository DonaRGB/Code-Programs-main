def mf1(n):
    if n <= 1:
        return
    for i in range(0,int(n)+1):
        print("Codingal")
        # since this loop runs in n iterations, this loop has a time complexity of O(n)
    mf1(n/2) # this runs recursively with complexity T(n/2)
    mf1(n/3) # this runs recursively with complexity T(n/3)
    # the sum of these complexities are T(n) = T(n/2) + T(n/3) + O(n)
    # since the time complexity is linear, the equation simplifies into T(n) = T(n/2) + T(n/3) + n
    # the recursive calls shrink quickly so then the equation becomes T(n) = O(n)
    # so, the time complexity of this function is O(n)
def mf2(n):
    if n <= 1:
        return
    print("Codingal") # this function takes O(1) time complexity
    mf2(n - 1) # this recursive call is time complexity of O(n - 1)
    # then the total time complexity of this function is T(n) = T(n - 1) + O(1)
    # expanding : T(n) = T(n - 1) + 1 => T(n) = O(n)
    # so this function also has time complexity of O(n) as well