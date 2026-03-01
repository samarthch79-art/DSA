# finding maximum subarray sum 
# kadane's approach:

a=[-1,2,-5,3,-52,1]
max=float("-inf")
sum=0
for i in range(len(a)):
     sum+=a[i]
     if sum>max:
         max=sum
     if sum<0:
         sum=0         
print(max)  

# time complexity O(n)
# space complexity O(1)
