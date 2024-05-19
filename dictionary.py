# dictionary functionsi are like list (dont have to assign any variable ---> alters the original)

'''
dic={'first': 'anushka', 'second': 'harry', 'third':'shole'}

print(dic['first'])

print(dic.keys())     # access all the keys available
print(dic.values())     # access all the values available

for key in dic.keys():   # prints out all the values
    print(dic[key])
    print(f'the values corresponding to the keys are {dic[key]}')   # fstring repeats the sentence with diff values
    print(f'the values to the key {key} is {dic[key]}')

print(dic)
print(dic.items())     # gives all key-value

for key,value in dic.items():
    print(f'the values to the key {key} is {value}')




ep1={123:59,456:79,754:80,986:72}
ep2={879:90,965:75}

ep1.update(ep2)        # adds elements of ep2 to ep1
print(ep1)
ep1.pop(123)          # removes the key-value of the given input
print(ep1)
ep1.popitem()         # removes the last key-value in the dictionary
print(ep1)
del ep1[456]         # deletes any key-value from the dictionary.    Imp to put []
print(ep1)
ep1.clear()           # makes a null {}
print(ep1)


dict1={}              # to create new empty dictionary
print(dict1)

dict2=dict()
print(dict2)
 
    
Dict = dict({1: 'Hcl', 2: 'WIPRO', 3:'Facebook'})     # Creating a Dictionary      
print(Dict)  




# Creating an empty Dictionary       
Dict = {}       
print("Empty Dictionary: ")       
print(Dict)       
        
# Adding elements to dictionary one at a time       
Dict[0] = 'Peter'      
Dict[2] = 'Joseph'      
Dict[3] = 'Ricky'      
print("\nDictionary after adding 3 elements: ")       
print(Dict)       
        
# Adding set of values        
# with a single Key       
# The Emp_ages doesn't exist to dictionary      
Dict['Emp_ages'] = 20, 33, 24      
print("\nDictionary after adding 3 elements: ")       
print(Dict)       
  
# Updating existing Key's Value       
Dict[3] = 'JavaTpoint'      
print("\nUpdated key value: ")       
print(Dict)            





Employee = {"Name": "Dev", "Age": 20, "salary":45000,"Company":"WIPRO"}         
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)        
print("Enter the details of the new employee....");        
Employee["Name"] = input("Name: ");        
Employee["Age"] = int(input("Age: "));        
Employee["salary"] = int(input("Salary: "));        
Employee["Company"] = input("Company:");        
print("printing the new data");        
print(Employee)


# for loop to print all the keys of a dictionary    
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}        
for x in Employee:        
    print(x) 

#for loop to print the values of the dictionary by using values() method.    
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}        
for x in Employee.values():        
    print(x)

#for loop to print the items of the dictionary by using items() method    
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}       
for x in Employee.items():        
    print(x)     



dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}  
print(len(dict)) 


dict = {7: "Ayan", 5: "Bunny", 8: "Ram", 1: "Bheem"}  
print(sorted(dict))  


dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# copy() method    
dict_demo = dict.copy()    
print(dict_demo)    
'''





        







































































