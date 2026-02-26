# finding second largest number in an array

a=[2,5,9,8,3]
b=float("-inf")
c=float("-inf")
for i in a:
    if i>b:
        c=b
        b=i
    elif i>c and  i !=b:
        c=i     
print("The largest number is",b)
print("The second largest number is",c)

# time complexity O(n)
