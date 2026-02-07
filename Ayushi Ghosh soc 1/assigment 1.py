#create and access list elements
list=[1,2,3,4,5]
print(list)
#accessing elements 
print(list[2])
#adding and removing elements from list 
list.append(6)
print("list after adding 6:",list)
list.remove(3)
print("list after removing 3 :",list)
#insert an element 
list.insert (2,10)
print("list after inserting 10 at index 2:",list)
#removing  last elements 
list.pop()
print("list after popping last elemnt :",list)
#sorting the list in ascending order 
list.sort()
print("list after sorting in ascending order :",list)
#sorting the list in descending order 
list.sort(reverse=True)
print("list after sorting in descending order:",list)
#Reverse list elements
list.reverse()
print("list after reversing elements:",list)
print("list after sorting in descending order:",list)
#Reverse list elements 
list.reverse()
print("list after reversing elements :",list)
