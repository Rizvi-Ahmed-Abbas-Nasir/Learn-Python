# a List

list  = ['Abbas',3,4,45,9,"Rizvi",66,45,3]
print(list)
 
# Delete Elemets form the list using remove() method
list.remove('Abbas')
print("Remove the elements usign remove() Method: ",list)

# Delete Element from the list using pop() function
list.pop()
print("Remove the elemet usign pop function ",list) 

# Delete Elements from the list using del key word
del list[0]
print("Remove the elemet usign del keyword ",list)
#another example
del list[0:2]
print("Remove the elements usign del keyword e.g 2",list)

# Outputs
# ['Abbas', 3, 4, 45, 9, 'Rizvi', 66, 45, 3]
# Remove the elements usign remove() Method:  [3, 4, 45, 9, 'Rizvi', 66, 45, 3]
# Remove the elemet usign pop function  [3, 4, 45, 9, 'Rizvi', 66, 45]
# Remove the elemet usign del keyword  [4, 45, 9, 'Rizvi', 66, 45]
# Remove the elements usign del keyword e.g 2 [9, 'Rizvi', 66, 45]