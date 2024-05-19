# Suppose you want to write a program that prints numbers from 1 to 10, formatted like this:
# Current value: 1
# Current value: 2
# ...
# Current value: 10

'''for num in range(10):
    print('Current value: ', (num+1))'''

# OR

'''num=1
while num<=10:
    print("Current value:" ,num)
    num+=1'''

          


'''countries = ['Thailand', 'Vietnam', 'Malaysia', 'UAE']

idx=0
while idx<4:
    print(countries[idx],'contains',len(countries[idx]), 'letters')
    idx+=1'''

# OR

'''for country in countries:
    print(country, 'contains', len(country), 'letters!')'''






#  Given a list of tuples, it removes people whose job titles contain the word "SQL" from the list

'''def remove_sql_specialists(people_list):
    for person in people_list[:]:
        if 'SQL' in person[1]:
            people_list.remove(person)
            print(people_list)

new_hires = [('Mark Adams', 'SQL Analyst', 4000),
             ('Leslie Burton', 'HR Specialist', 2300),
             ('Dorothy Castillo', 'UX Designer', 3100)]
remove_sql_specialists(new_hires)'''

# wrong
'''list=new_hires.copy()
for words in new_hires:
    if 'SQL' in words:
        list.pop(words)
        print(list)
    else:
        list.append(words)
        print(list)'''
    




# Create a function that accepts the following dictionary and returns the difference between the best and worst exam results.

'''exam_results = {
'Dominic Vargas': 67,
'Marion Riley': 89,
'Candice White': 45,
'Doreen Goodwin': 82,
'Janet Hunter': 98,
'Jaime Page': 32,
'Neil Fernandez': 76,
'Jana Frank': 28,
'Adrienne Perkins': 100,
'Rosa Mccarthy': 34
}

difference=max(exam_results.values())-min(exam_results.values())
print(difference)'''

# OR

'''def get_results_range(result_dict):
    max = 0
    min = 100
    for v in result_dict.values():
        if v > max:
            max = v
        if v < min:
            min = v
    return max - min

print(get_results_range(exam_results))'''






# Create a function called count_vowels that returns the total amount of vowels in a string. (a, e, i, o, u)
'''
def count_vowels(string):
vowels='a','e','i','o','u'
    count=0
    for words in string:
        print(words in vowels)
        if words in vowels==True:
            count+=1
            print(count)
        else:
            print('not applicable')
    return count

count_vowels('hellio')'''

# OR

'''def count_vowels(string):
    vowels = 'a','e','i','o','u'
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

print(count_vowels('anushkka anushanus ahsi'))'''












































































































































