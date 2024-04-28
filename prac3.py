#strings are immutable(does not change the variable)
 #functions will always have "()" 

name='Anushka bist'
print(name.upper())   # ".upper" means everything capital
print(name.lower())   # ".lower" means everything small
print(name.replace('Anushka', 'Marry'))    # ".replace" 

name1='blue eyes??????'
print(name1.rstrip('?'))   # ".rstrip" removes the repeating thing
print(name1.replace('blue', 'mule'))   

name2='anushka.... anushka.... anushka...'
print(name2.split(' '))    # ".split" splits the variable and makes them into a list
print(name2.count('anushka')) # ".count" counts the number of repeatition

name3='oMAY i am gooD'
print(name3.capitalize())    # ".capitalize" caps only the first letter of the value and the rest to lower case
print(name3.endswith('D'))
print(name3.endswith('d'))   # ".endswith" tells what the str ends with and gives output in True or False

name4='welcome to the program. This is the best. The program is good'
print(name4.endswith('me',0 ,7))   # tells that from idx [0:7] if variable ends with 'me'
print(name4.find('the'))  # ".find" asks to tell the idx when the word first appeared
print(name4.islower())    # ".islower" asks whether the variable has all small letter or not (True/False)
print(name4.istitle())    # ".istitle" asks whether the first word ONLY of the variable is caps (T/F)

# "\n" shifts everythiing to a new line




