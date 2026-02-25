# counting even numbers in an array

count=0
a=[2,5,1,8,3]
for i in a:
    if i%2==0:
        count+=1
print("total count of even numbers in array are", count) 

# time complexity O(n)
