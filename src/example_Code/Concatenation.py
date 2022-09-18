# pyhon concatenation +

firstName = "Rizvi"
secondName = "Abbas"
print(firstName + secondName) # String to String Concatenation is done normally in python

# but problem arise when we concate int with str
#print(firstName + 5) # This is not acceptable in pyhon

# this Error will show after you  try to concate int with string
#Traceback (most recent call last):
#  File "D:\Learn-Py\src\example_Programs\ex1.py", line 8, in <module>
 #   print(firstName + 5) # This is not acceptable in pyhon
# TypeError: can only concatenate str (not "int") to str

# cast Typing in python
print(firstName + str(22))