

#LIST--------------------------------------------------------------------------------

'''list=[1,2,3,4,5,6,7,8]

print(list[0])
print(list[-1])

print(list[-2])          #both have the same meaning of code
print(len(list)-1)'''


# "if....in..." means checking if that element is in the list or not
'''if 5 in list:          
    print('YES')
else:
    print('NO')'''



'''list1=[1,2,4,6,'Anushka',True,7,8,9,4]
if True in list1:
    print('Hehe')
else:
    print('Haha')

if 'nush' in 'nushka':
    print('YES')
else:
    print('NO')'''


 #slicing
'''print(list1)
print(list1[1:-1])
print(list1[0:10:2])         
print(list1[0:7:3])'''



# basically from 0 to 100 is stored in i and lst=i
lst=[i for i in range(101)]   
print(lst)


#for the lst element just print if they are multiple of 2
lst=[i for i in range(101) if i%2==0]  
print(lst)












