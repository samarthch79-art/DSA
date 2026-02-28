# checking palindrome by reversing the array

a=[1,2,3,4,5]
d=list(a)
b=0
c=len(a)-1
for i in range(len(a)//2):
    a[b],a[c]=a[c],a[b]
    b+=1
    c-=1
if a==d:
    print("palindrome")
else:
    print("not palindrome") 

# time complexity O(n)
