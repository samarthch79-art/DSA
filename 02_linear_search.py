# linear search

a=[2,5,1,8,3]
n=-1
m=int(input("enter the element to  be searched"))
for i in range(len(a)):
    if a[i]==m:
        n=i
        
if n==-1:
    print("element not found")
else:
    print("element found at index",n+1)

# time complexity O(n)
