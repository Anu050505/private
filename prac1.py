# Write a function, add_it_up(), that takes a single integer as input and 
# returns the sum of the integers from zero to the input parameter.
# (The function should return 0 if a non-integer is passed in.)

'''
def add_it_up(n):
    sum = 0                 # important to initialize the variable
    if isinstance(n,(str, float)):
        print('NOT APPLICABLE')     
    else:               
        for num in range(n + 1):
            sum += num
    return sum

print(add_it_up(5))'''



# He wants to know his average expenses for each semester. Using a for loop, calculate John’s average 
# expenses for the first semester (January to June) and the second semester (July to December).

'''monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

sem1=[]
sem2=[]
sem1.append(monthly_spending[0:6])
print(sem1)
sem2.append(monthly_spending[6:])
print(sem2)
                                                    
for i in sem1:
    ave1=sum(i)/len(i)
    print(round(ave1,2))

for l in sem2:
    ave2=sum(l)/len(l)
    print(round(ave2,2))'''





# They want to find out how many months John spent more money than Sam. Use a for loop to compare their
# expenses for each month. Keep track of the number of months where John spent more money.

'''john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
 
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]


months_john_spent_more = 0
 
for i in range(len(john_monthly_spending)):
    if john_monthly_spending[i] > sam_monthly_spending[i]:                   
        months_john_spent_more += 1
 
print("Number of months John spent more money than Sam:", months_john_spent_more)
'''





# Combine both lists into a single list that contains all of their friends. 
# Don’t include duplicate entries in the resulting list.

'''paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

del tina_friends[0]
print(tina_friends)
del tina_friends[1]
print(tina_friends)'''

# or

'''tina_friends.pop(0)
print(tina_friends)
tina_friends.pop(1)
print(tina_friends)

friends=list(paul_friends+ tina_friends)
print(friends)'''






# In this exercise, we’ll use a for loop to get a list of their common friends.

'''paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

common_friends = list()
for friend in paul_friends:
    if friend in tina_friends:
        common_friends.append(friend)
 
print("Common friends:", common_friends)'''






# Use a dictionary to tally up the votes in the poll.

'''poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]

vote_tally = dict()
for language in poll_results:
    if language in vote_tally:
        vote_tally[language] += 1                      
    else:
        vote_tally[language] = 1
    print(vote_tally)
 
print("Vote Tally:", vote_tally)'''






# Create a dictionary where each player is represented by the dictionary key
# and the corresponding total score is the dictionary value.

scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), 
          ('John', 5), ('John', 8), ('Tom', 8), ('Tom', 9)]

'''dic1=dict()
dic2=dict()
dic3=dict()

dic1['Mike']= 10+8+6
print(dic1)
dic2['John']= 7+8+5+8
print(dic2)
dic3['Tom']= 8+9
print(dic3)'''
# or
'''total_scores = {}
for player, score in scores:
    if player in total_scores:
        total_scores[player] += score
    else:                                                         
        total_scores[player] = score
 
print("Total Scores:", total_scores)'''







# write a function that returns a tuple, containing the list’s maximum value, sum of values, and mean value

'''def calc(numbers):
    list1=list()
    maxvalue=0
    maxvalue=max(numbers)
    list1.append(maxvalue)
    print(list1)

    sumvalue=0
    sumvalue=sum(numbers)
    list1.append(sumvalue)
    print(list1)

    meanvalue=0
    meanvalue=sum(numbers)/len(numbers)
    list1.append(meanvalue)
    print(list1)

    tup1=tuple(list1)
    print(tup1)

    return tup1

numbers = [10, 3, 5, 9, 18, 3, 0, 7]
calc(numbers)'''








# find the longest and the shortest word in the list.

'''word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
longest_word = word_list[0]
shortest_word = word_list[0]
 
for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) < len(shortest_word):
        shortest_word = word
 
print("Longest word:", longest_word)
print("Shortest word:", shortest_word)'''







# create a new list containing only the numbers that occur at least three times in the list.

'''number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]
modified_list = list()
for num in number_list:
    if number_list.count(num) >= 3:
        modified_list.append(num)
 
print("Numbers occurring at least three times:", modified_list)'''






# Find the second-highest score in the list.

'''exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]
exam_results.sort()
print(exam_results[-2])'''






# create a function that returns whether a list is symmetrical. In this case, a symmetrical list is a list 
# that remains the same after it is reversed – i.e. it’s the same backwards and forwards.

'''def check_sym(lst):
    
    if lst[0]==lst[-1] and lst[1]==lst[-2]:
        print('symmetrical')
    else:
        print('not symmetrical')
    
check_sym([1, 2, 3, 2, 1])
check_sym([1, 1, 2, 2, 3])'''

#OR

'''def is_symmetrical(input_list):
    lst = input_list.copy()
    lst.reverse()     # lst is updated here
    if lst == input_list:
        print('symmetrical')
    else:
        print('not symmetrical')
    
is_symmetrical([1, 2, 3, 2, 1])
is_symmetrical([1, 1, 2, 2, 3])'''





'''
k=[3,5,7,3,6,4,90,4]
k.reverse()
print(k)
k.sort(reverse=True)
print(k)'''





# Create a function that sorts the mixed list above using the following logic:
        # If the element is a string, the length of the string is used for sorting.
        # If the element is a number, the number itself is used.

'''mixed_list = ["apple", 5, 3.14, "banana", 7, 2.5, "orange", 10, 1.618, "grape"]
def custom_sort(element):
    if isinstance(element, str):       # The function checks whether each element is a string or a number using the isinstance() function
        return len(element)
    elif isinstance(element, (int, float)):      
        return element
 
sorted_mixed_list = sorted(mixed_list, key=custom_sort)           # NOT FOR LAB
 
print("Sorted mixed list:", sorted_mixed_list)'''



'''if isinstance(5, str):
    print(1)
else:
    print(0)'''






# create a function that does two things: filters out any words with three or fewer 
# characters and sorts the resulting list alphabetically.


'''things = ["Car", "Computer", "Building", "Bed", "Microwave", "TV"]

def filter_and_sort(input_list):
    filtered_list = []
    for word in input_list:
        if len(word) > 3:
            filtered_list.append(word)
    sorted_list = sorted(filtered_list)             # sorted basically sorts numericals and alphabets
    return sorted_list
 
result = filter_and_sort(things)
print("Filtered and sorted list:", result)'''
    
        


































