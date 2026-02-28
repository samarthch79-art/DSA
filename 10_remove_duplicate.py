# remove duplicates from array

a=[1,2,5,3,3,4,5]
d=set()
c=[]
for i in a:
    if i not in d:
       c.append(i) 
       d.add(i)    
print(c)

# time complexity O(n)
