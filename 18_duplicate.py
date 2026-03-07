# check if the list have any duplicate or not

a = [1,2,3,1]
seen = set()
for num in a:
    if num in seen:
        print("Duplicate exists")
        break
    seen.add(num)
else:
    print("No duplicates")

# time complexity O(n)
# space complexity O((n)
