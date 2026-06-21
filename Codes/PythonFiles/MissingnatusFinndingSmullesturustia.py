def findSmallestMissing(nums,l = None,r = None):
    if l is None and r is None:
        (left,right) = (0,len(nums)-1)
    if l > r:
        return l
    mid = l + (r - l) // 2
    if nums[mid] == mid:
        return findSmallestMissing(nums,mid+1,r)
    else:
        return findSmallestMissing(nums,l,mid-1)
from random import randint as ri
arr = [ri(0,100) for _ in range(ri(10,25))]
arr.sort()
res = findSmallestMissing(arr)
print("Array : {}".format(arr))
print("The smallest missing element in the array is {}.".format(res))