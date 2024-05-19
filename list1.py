# for list (you dont have to assign a new variable everytime you use the functions)
# for tuple (you have to assign a new variable before printing)


'''list=[21,2,13,54,44,5,6,27,18]
print(list)
list.append('Anushka')     # you have to initialise and then print 
print(list)                # adds a element to the end of the list

                            # the list has been altered and includes new variables

list.append(123)            
print(list)
list.sort()
print(list)                 # this sorts the list in increasing order

list.sort(reverse=True)     # this sorts the list in decreasing order
print(list)

print(list.index(2))        # gives the index of the element in the list

print(list.count(1))        # counts the number of times that element appears in the list

list.insert(1,100)          # adds a element in the given index "(idx,element)"
print(list)'''

l=[1,2,3,4,5,6,7,8]
m=[100,190,180]
l.extend(m)                 # extends the original list by adding the elements that are inside the ()
print(l)

print(l+m)            # same as extending/adding

del l[5]              # deletes the index of that list
print(l)



