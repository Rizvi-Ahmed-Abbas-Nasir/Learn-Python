#Average of best 2 in marks of 3 tests
marks1=int(input("Enter test 1 marks : "))
marks2=int(input("Enter test 2 marks : "))
marks3=int(input("Enter test 3 marks : "))

minimum=min(marks1,marks2,marks3)
print(minimum)
sumofbest2=marks1+marks2+marks3-minimum
avgofbest2=sumofbest2/2
print("Average of best 2 = ", avgofbest2)

# Output
# Enter test 1 marks : 45
# Enter test 2 marks : 76
# Enter test 3 marks : 56
# ('Average of best 2 = ', 66)