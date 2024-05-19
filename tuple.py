# tuples are immutable (cannot be changed)


tup1=(1,)                  # In tuple always have comma in the end when there is only 1 element
print(type(tup1),tup1)
tup2=(1,2,3,4,5,6,7,1)
print(type(tup2),tup2)

tup2=(12,67,45,60,32,13,4)
print(tup2[0])            # indexing
print(tup2[2])
print(tup2[3])
print(tup2[5])

if 67 in tup2:
    print('YES')          # checks for the element


    

tup3=('india', 'singapore', 'vietnam', 'australia', 'canada')
a=list(tup3)     # list is a function that can be changed
                 # we are making the tup into a list form by using the list function
print(a)
a.append('bhutan')
print(a)
a.pop(3)         # for pop, use index not str value
print(a)
a[4]='switzerland'
print(a)

tup1000=tuple(a)  # tuple is a function that changes anything to class tup
print(tup1000)




tup=('india', 'singapore', 'vietnam', 'australia', 'canada')
tup1=('maldives', 'pakistan', 'thailand', 'phillipines', 'united kingdom')
print(tup + tup1)       # combines the two tuples

a=tup.count('india')      #counts the occurance of that value
print(a)
print(len(tup))

b=tup.index('canada')   # find out the index of the given value
print(b)







