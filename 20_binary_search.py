# searching element using binary search method

def binary(a,k):
    l=0
    r=len(a)-1
    while l<r:
        mid=(l+r)//2
        if a[mid]==k:
            return mid
        elif a[mid]<k:
            l=mid+1
        else :
            r=mid-1
    return -1 

a=[1,2,2,3,4]
k=3
print(binary(a,k))          

# timme complexity O(logn)
# space compplexity O(1)
