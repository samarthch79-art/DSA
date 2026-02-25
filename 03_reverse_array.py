# reversing an array
a= [2,5,1,8,3]
b=[0]*len(a)
j=0
for i in range(len(a)-1,-1,-1):
    
        b[j]=a[i]
        j=j+1
print(b)  
# time complexity O(n)
