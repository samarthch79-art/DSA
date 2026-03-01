# finding the maximum subarray sum
# bruteforce approach:

a=[1,2,5,3,-5,2,1]
max=float("-inf")
sum=0
for i in range(len(a)):
    for j in range(i,len(a)):
        sum+=a[j]
        if sum>max:
            max=sum    
    sum=0
print(max)  

# time complexity O(n)
# space complexity O(1)
