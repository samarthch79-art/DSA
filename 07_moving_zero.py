# moving all zeros to  right

a=[1,0,3,0,5,6]
b=0
for i in range (len(a)):
   if a[i]!=0:
       a[b],a[i]=a[i],a[b] 
       b+=1
print(a)

# time complexity O(n)
