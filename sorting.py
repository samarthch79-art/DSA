# sorting  the array using bubble sorting

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=[1,5,4,3,]
bubble(a)
print(a)

# time complexity O(n^2)
# space complexity o(1)
