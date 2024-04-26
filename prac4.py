time=int(input("Enter the time according to 24hr clock: "))
print(time)

if(time>=0000 and time<1200):
    print("Good morning!")

elif(time>=1200 and time<=1600):
    print('Good afternoon!')

elif(time>1600 and time<=2400):
    print('Good night!')

else:
    print('ERROR!')