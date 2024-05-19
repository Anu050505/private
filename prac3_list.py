# Given a list, write a Python program to swap first and last element of the list.

'''def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList

newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# OR

def swapList(list):
     
    first = list.pop(0)   
    last = list.pop(-1)
     
    list.insert(0, last)       # .insert(idx, element to insert)
    list.append(first)         # add at the back
     
    return list

newList = [12, 35, 9, 56, 24]
print(swapList(newList))'''
    




# The task is to find the sum and average of the list. The average of the list is
# defined as the sum of the elements divided by the number of elements.

'''lst= [4, 5, 1, 2, 9, 7, 10, 8]
str1=lst.copy()
addition=sum(str1)
average=sum(str1)/len(str1)
print(addition)
print(average)
'''




# count the number of occurrences of x in the given list.

'''lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
a=lst.count(x)
print(a)
lst1 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
y = 16
b=lst1.count(y)
print(b)
'''


# Multiply numbers in the list
'''
def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
'''
    


# Find the smallest number in the list

'''list1 = [10, 20, 4]
minimum=min(list1)
print(minimum)
'''
# OR

'''list2 = [20, 10, 20, 1, 100]
list2.sort()
print(list2[0])'''



# find the second largest number

'''list2 = [70, 11, 20, 4, 100]
list2.sort()
print(list2[-2])'''




# program to print even numbers in a list

'''list1 = [2, 7, 5, 64, 14]
evenlst=list()
oddlst=list()
for num in list1:
    if num%2==0:
        evenlst.append(num)
    else:
        oddlst.append(num)

    print('Even numbers are: ', evenlst, end="   ")
    print('Odd numbers are: ',oddlst)
        '''

 


# program to print all even numbers in a range (Input: start = 4, end = 15)

'''evenlist=list()
oddlist=list()
for num in range(4,16):
    if num%2==0:
        evenlist.append(num)
    else:
        oddlist.append(num)

print(evenlist,oddlist)'''

# OR

'''start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")'''




# program to count Even and Odd numbers in a List

'''list1 = [2, 7, 5, 64, 14]
evencount=0
oddcount=0
for num in list1:
    if num%2==0:
        evencount+=1
    else:
        oddcount+=1
print(evencount,oddcount)'''





# program to print positive numbers in a list

'''list1 = [-10, -21, -4, 45, -66, 93]
for num in list1:
    if num>=0:
     print(num)'''
     
# OR

'''list1 = [-10, -21, -4, 45, -66, 93]
 
# using list comprehension
pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", *pos_nos)'''





# program to count positive and negative numbers in a list

'''list1 = [2, -7, 5, -64, -14]
pos=0
neg=0
for num in list1:
    if num>=0:
        pos+=1
    else:
        neg+=1

print(pos,neg)'''





# Remove multiple elements from a list in Python

'''list1=[12, 15, 3, 10]  # Remove = [12, 3]
newlist=list()
for num in list1:
    if num!=12 and num!=3:
        newlist.append(num)

print(newlist)'''


'''list1 = [11, 5, 17, 18, 23, 50] 
# removes elements from index 1 to 4
# i.e. 5, 17, 18, 23 will be deleted
del list1[1:5] 
                                         # pop function can be used for just 1 index value
print(list1)                             # del function can be used for slicing'''




# Unique elements from a list

'''def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))  '''



































































