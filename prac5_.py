
# Display three string “Name”, “Is”, “James” as “Name**Is**James”

'''print('My', 'Name', 'is', 'James', sep='**')'''


# Convert Decimal number to octal using print() output formatting

'''num = 8
print('%o' % num)'''


#  Display float number with 2 decimal places using print()

'''num = 458.541315
print(round(num,2))
print('%.2f' % num)'''


# Accept a list of 5 float numbers as an input from the user

'''numbers = []
for i in range(5):
    print("Enter number at location", i+1, ":")
    item = float(input())
    numbers.append(item)

print("User List:", numbers)'''


# Format variables using a f.string() method.

'''totalMoney = 1000
quantity = 3
price = 450

print(f'I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars.')
'''


# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

'''num1 = 40
num2 = 30

if num1*num2<=1000:
    print(num1*num2)
else:
    print(num1+num2)'''


# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

'''print("Printing current and previous number and their sum in a range(10)")

previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i'''


# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

'''numbers_y = [10, 20, 30, 40, 10]

if numbers_y[0]==numbers_y[-1]:
    print('True')
else:
    print('False')'''

# Write a program to find how many times substring “Emma” appears in the given string.

'''str_x = "Emma is good developer. Emma is a writer"
a=str_x.count('Emma')
print("Emma appeared",a,'times')'''



'''for num in range(10):
    for i in range(num):
        print (num, end=" ") # print number
    # new line after each row to display pattern correctly
    print("\n")'''
    

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

'''list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
l=[]

for num in list1:
    if num%2==1:
        l.append(num)

for num in list2:
    if num%2==0:
        l.append(num)

print(l)'''






























































