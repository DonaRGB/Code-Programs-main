class Data:
    def __init__(self,value,index,count = 0):
        self.value = value
        self.index = index
        self.count = count
def sortByFreqAndIdx(arr):
    if arr is None or len(arr) < 2:
        return
    hm = {}
    for i in range(len(arr)):
        hm.setdefault(arr[i], Data(arr[i],i)).count += 1
    values = [*hm.values()]
    values.sort(key = lambda x: (-x.count, x.index))
    k = 0
    for d in values:
        for j in range(d.count):
            arr[k] = d.value
            k += 1
from random import randint as ri
arr = [ri(1,10) for _ in range(ri(15,30))]
print(f"Original Array : {arr}")
sortByFreqAndIdx(arr)
print(f"Sorted Array : {arr}")