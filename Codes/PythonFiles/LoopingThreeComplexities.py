def my_func(n):
    i1 = 0
    for i in range(0,n+1):
        i1 += 1
        print("First Loop",i+1)
    print("\n")
    i2 = 0
    j = 1
    while j <= n + 1:
        i2 += 1
        print("Second Loop",j)
        j = j*2
    print("\n")
    i3 = 0
    for k in range(0,100):
        i3 += 1
        print("Third Loop",k+1)
    print(f"\n- Iterations of First Loop : {i1}\n- Iterations of Second Loop : {i2}\n- Iterations of Third Loop : {i3}")
from random import randint as ri
my_func(ri(ri(0,100),ri(101,200)))
print("\n---------------------------------------------------------\n")
my_func(ri(ri(ri(0,100),ri(101,200)),ri(ri(201,300),ri(301,400))))
print("\n---------------------------------------------------------\n")
my_func(ri(ri(ri(ri(0,100),ri(101,200)),ri(ri(201,300),ri(301,400))),ri(ri(ri(401,500),ri(501,600)),ri(ri(601,700),ri(701,800)))))
print("\n---------------------------------------------------------\n")
print("Thus, the following information can be deduced :\n   1. The first loop runs with time complexity O(n)\n   2. The second loop runs with time complexity O(log(n))\n   3. The third loop runs with time complexity O(1)")