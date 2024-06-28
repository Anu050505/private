# Sorting Dictionary By Key

'''myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
print(myKeys)
sorted_dict = {i: myDict[i] for i in myKeys}                          ##############
 
print(sorted_dict)'''



'''for key in sorted(myDict):  
    print({key: myDict[key]})'''





# Displaying the Keys in Sorted Order

# Function calling
'''def dictionary():
    # Declare hash function
    key_value = dict()
 
# Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
 
    print("Task 1:-\n")
 
    print("key_value", key_value)
 
    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(key_value.keys()):                 # sorted basically arranges 
        print(i, end=" ")
 
 
def main():
    # function calling
    dictionary()
 
 
# Main function calling
if __name__ == "__main__":
    main()'''




# Sorting the Keys and Values Alphabetically Using the Key

# function calling
def dictionairy():
 
    # Declaring the hash function
    key_value = {}
 
# Initialize value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
     
    print("key_value",key_value)
 
    print("Task 2:-\nKeys and Values sorted in",
          "alphabetical order by the key  ")
     
 
    # sorted(key_value) returns a sorted list
    # of the Dictionary’s keys.
    for i in sorted(key_value):
        #print(i)
        print((i, key_value[i]), end=" ")
 
 
def main():
        # function calling
    dictionairy()
 
 
# main function calling
if __name__ == "__main__":
    main()





# Handling Missing Keys in Python Dictionaries 

'''ele = {'a': 5, 'c': 8, 'e': 2}
if "q" in ele:
    print(ele["d"])
else:
    print("Key not found")'''

# OR            ".get(key,def_val)"

'''country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
 
# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))        # If the key is present, the value associated with the key is 
                                                     # printed, else the def_value passed in arguments is returned.
 
# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))'''



# Python dictionary with keys having multiple inputs

'''# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
          ("28.33'34.1", "77.06'16.6"):"Delhi"}
 
print(places)
print('\n')
 
# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])             # referring to the key
    long.append(i[1])
    plc.append(places[i[0], i[1]])         # referring to the value
 
print(lat)
print(long)
print(plc)'''





# program to find the sum of all items in a dictionary

'''def addition(value):
    output=0
    for num in value.values():
        output=output+num
    
    print(output)'''

# OR

'''def addition(value):
    print(sum(value.values()))'''


'''addition({'a': 25, 'b':18, 'c':45})
print(addition)'''





# Merging two Dictionaries

'''dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict1.update(dict2)
print(dict1)'''



# Program to create grade calculator 

'''print("Enter Marks Obtained in 5 Subjects: ")
total1 = int(input())
total2 = int(input())
total3 = int(input())
total4 = int(input())
total5 = int(input())
 
tot = total1 + total2 + total3 + total4 + total4
avg = tot / 5
 
if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 71 and avg < 81:
    print("Your Grade is B1")
elif avg >= 61 and avg < 71:
    print("Your Grade is B2")
elif avg >= 51 and avg < 61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E1")
elif avg >= 0 and avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")'''



# methods to get the values

'''person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# access value using key name in []
print(person['name'])

#  get key value using key name in get()
print(person.get('telephone'))'''




#  iterate through a dictionary using a for-loop and access the individual keys and their corresponding values

'''person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# Iterating the dictionary using for-loop
print('key', ':', 'value')
for key in person:
    print(key, ':', person[key])

# using items() method
print('key', ':', 'value')
for key_value in person.items():
    # first is key, and second is value
    print(key_value[0], key_value[1])'''




# how does len work (count number of keys present in  a dictionary)

'''person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(len(person)) '''





# update dictionary by adding 2 new keys (2 methods)

'''person = {"name": "Jessa", 'country': "USA", "telephone": 1178}

person["weight"] = 50
person.update({"height": 6})

# print the updated dictionary
print(person)'''





# we can add more than one key using the update() method.

'''person = {"name": "Jessa", 'country': "USA"}
person.update({"weight": 50, "height": 6})
print(person)

# pass new keys as as list of tuple
person.update([("city", "Texas"), ("company", "Google",)])
print(person)'''





# Set default value to a key

'''person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}

# set default value if key doesn't exists
person_details.setdefault('state', 'Texas')

# key doesn't exists and value not mentioned. default None
person_details.setdefault("zip")

# key exists and value mentioned. doesn't  change value
person_details.setdefault('country', 'Canada')

# Display dictionary
for key, value in person_details.items():                                         
    print(key, ':', value)'''






# Modify the values of the dictionary keys

'''person = {"name": "Jessa", "country": "USA"}

# updating the country name
person["country"] = "Canada"
# print the updated country
print(person['country'])

# updating the country name using update() method
person.update({"country": "USA"})
# print the updated country
print(person['country'])'''







# Removing items from the dictionary

'''person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

# Remove last inserted item from the dictionary
deleted_item = person.popitem()
print(deleted_item)  # output ('height', 6)
# display updated dictionary
print(person)  
# Output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50}

# Remove key 'telephone' from the dictionary
deleted_item = person.pop('telephone')
print(deleted_item)  # output 1178
# display updated dictionary
print(person)  
# Output {'name': 'Jessa', 'country': 'USA', 'weight': 50}

# delete key 'weight'
del person['weight']
# display updated dictionary
print(person)
# Output {'name': 'Jessa', 'country': 'USA'}

# remove all item (key-values) from dict
person.clear()
# display updated dictionary
print(person)  # {}

# Delete the entire dictionary
del person'''





'''person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}
a=person.popitem()
print(a)
print(person)
b=person.pop('name')
print(b)
print(person)'''






# Checking if key is available

'''person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# Get the list of keys and check if 'country' key is present
key_name = 'country'
if key_name in person.keys():
    print("country name is", person[key_name])
else:
    print("Key not found")'''







# Nested dictionary

'''address = {"state": "Texas", 'city': 'Houston'}

# dictionary to store person details with address as a nested dictionary
person = {'name': 'Jessa', 'company': 'Google', 'address': address}

# Display dictionary
print("person:", person)

# Get nested dictionary key 'city'
print("City:", person['address']['city'])

# Iterating outer dictionary
print("Person details")
for key, value in person.items():
    if key == 'address':
        # Iterating through nested dictionary
        print("Person Address")
        for nested_key, nested_value in value.items():                       #################
            print(nested_key, ':', nested_value)
    else:
        print(key, ':', value)'''







# How nested sictionary works

'''# each dictionary will store data of a single student
jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}

# Outer dictionary to store all student dictionaries (nested dictionaries)
class_six = {'student1': jessa, 'student2': emma, 'student3': kelly}

# Get student3's name and mark
print("Student 3 name:", class_six['student3']['name'])
print("Student 3 marks:", class_six['student3']['marks'])

# Iterating outer dictionary
print("\nClass details\n")
for key, value in class_six.items():
    # Iterating through nested dictionary
    # Display each student data
    print(key)
    for nested_key, nested_value in value.items():
        print(nested_key, ':', nested_value)
    print('\n')
'''





# Sorting of the dictionary

'''dict1 = {'c': 45, 'b': 95, 'a': 35}

# sorting dictionary by keys                                   # for dic use sorted() not .sort
print(sorted(dict1.items()))
# Output [('a', 35), ('b', 95), ('c', 45)]

# sort dict eys
print(sorted(dict1))
# output ['a', 'b', 'c']

# sort dictionary values
print(sorted(dict1.values()))
# output [35, 45, 95]'''




# max,min,sum functions in dictionary

'''dict1 = {'c': 45, 'b': 95, 'a': 35}

max_val=max(dict1.values())
print(max_val)
min_val=min(dict1.values())
print(min_val)
addition=sum(dict1.values())
print(addition)'''





# Converting list to dictionary

'''keys = ["name", "age", "city"]
values = ["John", 25, "New York"]
 
new_dict = dict(zip(keys, values))
print(new_dict)'''




# -----------------------------------------------------------------------------------------------------------------


'''Sample= {0: 10, 1: 20}
Sample[2]= 30
print(Sample)'''


'''dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4) '''


'''n = int(input("Input a number "))
d = dict()
# Iterate through numbers from 1 to 'n' (inclusive).
for x in range(1, n + 1):
    # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
    d[x] = x * x
print(d) '''
    

'''# Create a dictionary 'd' with color names as keys and corresponding numerical values as values.
d = {'Red': 1, 'Green': 2, 'Blue': 3}

# Iterate through the key-value pairs in the dictionary 'd' using a for loop.
for color_key, value in d.items():
    # Print the color name, 'corresponds to', and its corresponding numerical value.
    print(color_key, 'corresponds to ', value) '''


'''my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
addition=0
for val in my_dict.values():
    addition=addition+val                               
print(addition)'''

# OR

'''my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result=sum(my_dict.values())
print(result)'''


'''my_dict = [{'data1': 100, 'data2': -54, 'data3': 247}]                           #IMPORTANT
a=my_dict[0]
print(a)
n=sum(a.values())                                                        # force to remove the list and make a dic 
print(n)'''


'''my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
mult=1
for num in my_dict.values():
    mult=mult*num                                        #
print(mult)'''



# max, min for a dictionary

'''my_dict = {'x': 500, 'y': 5874, 'z': 560}
for item in my_dict.values():
    a=max(my_dict.values())
    b=min(my_dict.values())
print(a,b)'''



'''
my_dict = {}
if my_dict=={}:
    print('True')
else:
    print('False')'''


