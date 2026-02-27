# finding frequency of each element in an array

a=[1,2,5,3,3,4,5]
dict={}
for  i in range(len(a)):
    if a[i] in dict:
        dict[a[i]]+=1
    else:
        dict[a[i]]=1
for i in dict:        
     print(i,"--->",dict[i]) 

# time complexity O(n)
