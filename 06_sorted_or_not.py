# checking if an array is sorted or not

a=[1,2,3,4,5]
for i in range (len(a)-1):
    if a[i]>a[i+1]:
        print("array is  not sorted")
        break
else:
    print ("array is sorted") 

# time complexity O(n)
