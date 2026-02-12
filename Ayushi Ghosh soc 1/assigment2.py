#create set
set = {1,2,3,4,5}
print(set)
#Accesing element in set 
print("Accessing set element:")
for element in set:
    print(element)
#Adding element to set 
set.add(6)
print("set after adding 6:",set)
#remove element from set
set.remove(3)
print("set after removing 3:",set)
#adding multiple elements to set 
set.update([7,8,9])
print("set after adding multiple elements7,8,9:",set)
#union of the elemts 
set2 = {10,11,12}
set_union = set.union(set2)
print("union of set and set 2 :",set_union)
#intersection of the elements 
set3 = {5,6,7,10}
set_intersection = set.intersection(set3)
print("intersection of set and set 3 :",set_intersection)
#difference of the elements
set_difference = set.difference (set3)
print("difference of set and set 3 :",set_difference)
