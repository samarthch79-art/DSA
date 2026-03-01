# checking for palindrome using two pointers

a=[1,2,5,3,5,2,1]
l=0
r=len(a)-1
while l<r:
    if a[l]!=a[r]:
        print("not palindrome")
        break 
    l+=1
    r-=1
else:
    print("palindrome")

# time complexity O(n)
