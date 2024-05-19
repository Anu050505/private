# Write a Python program to convert them into a dictionary in a way that 
# item from list1 is the key and item from list2 is the value


'''keys=['Ten', 'Twenty', 'Thirty']
values=[10,20,30]

# empty dictionary
res_dict = dict()    

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)'''


# Merge two Python dictionaries into one

'''dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)'''


# Print the value of key ‘history’ from the below

'''sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# solution
print(sampleDict['class']['student']['marks']['history'])'''



# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.


'''sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

sample_dict.pop('age')
print(sample_dict)
sample_dict.pop('city')
print(sample_dict)

# or

# keys to extract
keys = ["name", "salary"]

res = dict()   # new dict

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)'''



# Delete a list of keys from a dictionary

'''sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

res = dict()
res.update(sample_dict)
print(res)

for k in keys:
    res.pop(k)
    print(res)'''


# Write a Python program to check if value 200 exists in the following dictionary.

'''sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print('200 is present')
else:
    print('Not available')'''



# Write a program to rename a key city to a location in the following dictionary.

'''sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)'''




# Get the key of a minimum value from the following dictionary

'''sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75,
  'science': 12
}
low = min(sample_dict.values())
print(low)

if low in sample_dict.values():
    print('Yes')

print(min(sample_dict, key=sample_dict.get))'''



# Write a Python program to change Brad’s salary to 8500 in the following dictionary.

'''sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

# a = sample_dict.get('emp3')
# print(a)

sample_dict['emp3']['salary'] = 8500
print(sample_dict)'''












# DICTIONARY RULES -------------------------------------------------------------------------------



'''dict1={}
print(dict1)

dict2=dict()
print(dict2)'''




# Creating an empty Dictionary       
'''Dict = {}       
print("Empty Dictionary: ")       
print(Dict)    '''   
        
# Adding elements to dictionary one at a time       
'''Dict[0] = 'Peter'      
Dict[2] = 'Joseph'      
Dict[3] = 'Ricky'      
print("\nDictionary after adding 3 elements: ")       
print(Dict)    '''   
        
# Adding set of values        
# with a single Key       
# The Emp_ages doesn't exist to dictionary      
'''Dict['Emp_ages'] = 20, 33, 24      
print("\nDictionary after adding 3 elements: ")       
print(Dict)  '''     
  
# Updating existing Key's Value       
'''Dict[3] = 'JavaTpoint'      
print("\nUpdated key value: ")       
print(Dict)         '''




'''Employee = {"Name": "Dev", "Age": 20, "salary":45000,"Company":"WIPRO"}         
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)        
print("Enter the details of the new employee....");        
Employee["Name"] = input("Name: ");        
Employee["Age"] = int(input("Age: "));        
Employee["salary"] = int(input("Salary: "));        
Employee["Company"] = input("Company:");        
print("printing the new data");        
print(Employee)     '''





'''Employee = {"Name": "David", "Age": 30, "salary":55000,"Company":"WIPRO"}         
     
print("Deleting some of the employee data")         
del Employee["Name"]        
del Employee["Company"]        
print("printing the modified information ")        
print(Employee)        
print("Deleting the dictionary: Employee");        
del Employee        
print("Lets try to print it again ");        
print(Employee)   '''



# Creating a Dictionary       
'''Dict1 = {1: 'JavaTpoint', 2: 'Educational', 3: 'Website'}   '''    
# Deleting a key        
# using pop() method       
'''pop_key = Dict1.pop(2)       
print(Dict1)  '''  


# for loop to print all the keys of a dictionary    
'''Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}        
for x in Employee:        
    print(x) '''

#for loop to print the values of the dictionary by using values() method.    
'''Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}        
for x in Employee.values():        
    print(x)'''

#for loop to print the items of the dictionary by using items() method    
'''Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}       
for x in Employee.items():        
    print(x)     '''


'''dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}  
print(len(dict))'''

'''dict = {7: "Ayan", 5: "Bunny", 8: "Ram", 1: "Bheem"}  
print(sorted(dict))  '''


# copy() method
'''dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}        
dict_demo = dict.copy()    
print(dict_demo)    '''


# pop() method 
'''dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}       
dict_demo = dict.copy()    
dict_demo.pop(1)    
print(dict_demo) '''


# keys() method 
# values() method 
# items() method
'''dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}      
print(dict.keys())  
print(dict.values())   
print(dict.items()) '''


# get() method -------> gets the value of that key
'''dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}        
print(dict.get(3)) '''


# update() method 
'''dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}       
dict.update({3: "TCS"})    
print(dict)    
dict[3]='we'
print(dict)'''



































































