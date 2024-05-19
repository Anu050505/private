
#FUNCTIONS------------------------------------------------------------------------------

'''def average(a,b):
    print('the average is', (a+b)/2)

average(7,3)'''




# Defining a function    
'''def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    '''
    
# Calling function and passing arguments without using keyword    
'''print( "Without using keyword" )    
function( 50, 30)   '''    
        
# Calling function and passing arguments using keyword    
'''print( "With using keyword" )    
function( n2 = 50, n1 = 30)  '''  



'''
# Defining a function    
def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
# Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30    
print( "Passing out of order arguments" )    
function( 30, 20 )       '''
    





'''
def function( *args_list ):    
    ans = []    
    for l in args_list:    
        ans.append( l.upper() )    
    return ans    

# Passing args arguments    
object = function('Python', 'Functions', 'tutorial')    
print( object )    
    
# defining a function    
def function( **kargs_list ):    
    ans = []    
    for key, value in kargs_list.items():    
        ans.append([key, value])    
    return ans    
# Paasing kwargs arguments    
object = function(First = "Python", Second = "Functions", Third = "Tutorial")    
print(object)   '''






'''
# Defining a function with return statement    
def square( num ):    
    return num**2    
     
# Calling function and passing arguments.    
print( "With return statement" )    
print( square( 52 ) )    
    
# Defining a function without return statement     
def square( num ):    
     num**2     
    
# Calling function and passing arguments.    
print( "Without return statement" )    
print( square( 52 ) )    '''

'''
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))  '''






















