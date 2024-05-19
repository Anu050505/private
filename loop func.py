# IF ELSE FUNCTION--------------------------------------------------------------


'''time=int(input("Enter the time according to 24hr clock: "))
print(time)

if(time>=0000 and time<1200):
    print("Good morning!")

elif(time>=1200 and time<=1600):
    #print('Good afternoon!')

elif(time>1600 and time<=2400):
    print('Good night!')

else:
    print('ERROR!')'''





# FOR FUNCTION--------------------------------------------------------------------------

'''name='anushka'
for i in name:
    print(i, end=' ')  # end=' ' makes the value write with spacings in between
    print(i, end=',')   # end=',' makes the value write with comma seperator
    print(i)           #prints one by one in vertical format



colour=['red','blue','black','white','green']
for color in colour:
    print(color)     # prints each element one by one
    for i in color:
        print(i)     #further prints each letter in each element'''


# Creating a sequence which is a tuple of numbers  
'''numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  
  
# variable to store the square of the number  
square = 0  
  
# Creating an empty list  
squares = list()       # or squares = []
  
# Creating a for loop  
for value in numbers:  
    square = value ** 2  
    squares.append(square)  
print("The list of squares is", squares)  '''






'''string = "Python Loop"  
  
# Initiating a loop  
for s in string:  
    # giving a condition in if block  
    if s == "o":  
        print("If block")  
    # if condition is not satisfied then else block will be executed  
    else:  
        print(s) '''















#RANGE FUNCTION--------------------------------------------------------------------

#for i in range(5):
    #print(i)        # prints from 0 to 4 
    #print(i+1)       # prints from 1 to 5 (beacuse k+1)


#for i in range(1,9):
    #print(i)         # prints 1 to 8


#range(start,stop,step)      step basically increases start number by the given step number till the stop number



'''print(range(15))  
  
print(list(range(15)))  
  
print(list(range(4, 9)))  
  
print(list(range(5, 25, 4)))  

OUTPUTS:
range(0, 15)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[4, 5, 6, 7, 8]
[5, 9, 13, 17, 21]
'''

# WHILE LOOP--------------------------------------------------------------------------

'''i=0
while(i<3):
    print(i)
    i+=1


i=5
while(i>0):
    print(i)
    i-=1
else:
    print("I am done with the loop")'''




















