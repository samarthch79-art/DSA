# find two numbers whoes sum equals the target

a=[1,2,5,3,3,4,5]
target=10
flag=0
dict={}
for  i in a:
    b=target-i
    if b in dict:
        print(i,",",b)
        flag=1
        break
    dict[i]=1
if(flag==0):
    print("no pair found")

# time complexity O(n)
# space complexity O(n)
