# best  time to buy and sell stocks 

a=[1,2,4,3,4,5]
max_profit=float('-inf')
min=a[0]
for i  in a:
    if i<min:
        min =i
    elif i-min>max_profit:
        max_profit=i-min
print(max_profit) 

# time complexity O(n)
# space complexity O(1)
