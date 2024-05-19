letter='My name is {} and I am from {}'
name='Anushka'
country='India'
                                      # important to assign a variable
a=letter.format(name, country)        # .format is a function that puts the values inside {}
print(a)

# OR #

letter='My name is {1} and I am from {0}'
name='Anushka'
country='India'

a=letter.format(country, name )        
print(a)




# FOR CONVINIENCE #

print(f'My name is {name} and I am from {country}')   # f string: basically write the variable inside the {}
name='Anushka'                                        # and then assign values to variables THATS IT!!
country='India'

ans='best'
a=(f'I am the {ans}')
print(a)




txt='For only {price:.2f}'       # .2f makes the output to 2dp
print(txt.format(price=49.8596))


a=67.35462825494
print(round(a,3))               # round of the number to the nearest decimal stated
                         





















































