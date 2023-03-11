# List
list = [1,2,3,4,5,65,7,"Abbas"]

# Accessign the list by usign Indexing
e1 = list[0]
# eg 2
e2 = list[5]
print("List Access by Indexing ", e1 ," ",e2)

#Accessing the list by using Negative Indexing
e3 = list[-1]
print("List Access by Negative Indexing ",e3)

#Accessing the list by Slicing(slicing index) operator
e4 = list[0:5]
print("List Access by Slicing Operator Indexing ",e4)
#eg 2
e5 = list[4:]
print("List Access by Slicing Operator Indexing ", e5)

# Accessign the lsit by using Negative Slicing operator
e6 = list[-4:-2]
print("List Access by Negative Slicing Operator Indexing ",e6)

# Accessign  the list by usign for loog
print("Accessig all the elemets using for loop")
for i in list:
    print(i)


# outputs
# List Access by Indexing  1   65
# List Access by Negative Indexing  Abbas
# List Access by Slicing Operator Indexing  [1, 2, 3, 4, 5]    
# List Access by Slicing Operator Indexing  [5, 65, 7, 'Abbas']
# List Access by Negative Slicing Operator Indexing  [5, 65]   
# Accessig all the elemets using for loop
# 1
# 2
# 3
# 4
# 5
# 65
# 7
# Abbas