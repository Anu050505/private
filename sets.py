s={1,2,3,4,5,1,6,7,4,5}        # sets make repeated values not to  be counted
                               # the order can be different than the actual one
                               # values inside sets cannot be replaced 
print(s)

a1=set()    # to make an empty set do 'set()'
for value in s:
    print(value)     # for...in.. can be used


a={1,2,5,6}
b={3,6,7}
print(a.union(b))  # .union() combines the element into 1 set

print(a,b)
a.update(b)      # a.update(b) adds element of b to a. Elements of b remain unchanged
print(a,b)


a1={1,2,3,4,2,3,5,4,7,1,3}
a2={2,5,8,9,1}
a3=a1.intersection(a2)       # .intersection tells the same elements that are found in th sets
print(a3)
a1.intersection_update(a2)   # .intersection_update updates a1.    no need to create new variable name
print(a1)


a1={1,2,3,4,2,3,5,4,7,1,3}
a2={2,5,8,9,1}
b=a1.symmetric_difference(a2)   # .symmetric_difference prints the not similar values
print(b)






