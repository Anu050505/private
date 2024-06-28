# LESSON Trial ------------------------------------------------------------------------------------------------------------

'''print('Hello World')
x=[1,2,3,5,67,2,35]
print(x)
t=sum(x)
print(t)
x.sort()
print(x)
x=['one','two','zero','apple']
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)
x=[2,5,3,23,4,64,3,4,5]
y=x[::-1]                       # reverse the numbers 
print(x,y)'''







# LESSON 1 ---------------------------------------------------------------------------------------------------------------


# Create a list of f10 elements of fibonacci series (0 to 100) that are multiple of 3 and 7.

'''l=list()
x=0
for num in range(101):
    if num%3==0 and num%7==0:
        l.append(num)

print(l)'''


# Create a list of 10 elements of fibonacci series
# 0,1,1,2,3,5,8,13,21

'''a=0
b=1
f=[]
f.append(a)
f.append(b)
for r in range (2,10):
    t=a+b
    f.append(t)
    a=b
    b=t
print(f)'''


# check whether the number 121 is a fibonacci element or not

'''a=0
b=1
f=[]
f.append(a)
f.append(b)
flag=0
for r in range (2,100): 
    t=a+b
    f.append(t)
    a=b
    b=t
    if f[r] == 121:
        flag=1
        break
if flag ==1:
    print('yes')
else:
    print('no')'''







# LESSON 2 ---------------------------------------------------------------------------------------------------------------


# Given a 3 digit number, separate the digits using // and % operator

'''num = int(input("Enter the 3 digit number: "))
a = num//100  # 1
b = (num%100)//10   # 2
c = (num%100)%10     # 3
print('a =',a)
print('b =',b)
print('c =',c)'''



# Given a 4 digit number, sum of all the digits.

'''num=int(input('enter a 4 digit number: '))
print(num)
a=num//1000
b=num%1000
c=(num%1000)//100
d=(num%1000)%100
e=d//10
f=d%10
print(a,c,e,f)
sum=a+c+e+f
print(sum)'''



'''x=[1,3,5,6,86,45,22,3,5]
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)

a=0
for values in x:
    a=a+values
print(a)

y=sum(x)
print(y)'''



# find the sum of the first 5 elements in the fibonacci series
# 0,1,1,2,3,5,8,13,21

'''a=0
b=1
f=[]
f.append(a)
f.append(b)
for r in range (2,5):
    t=a+b
    f.append(t)
    a=b
    b=t
print(f)
print(sum(f))'''



# switching the numbers
'''a=5
b=3'''

# using a third value
'''c=a
a=b
b=c
print(a,b)'''

# using assignment operator
'''a,b=b,a
print(a,b)'''

# arthemetic operation
'''a=a+b #8
b=a-b #8-3=5
a=a-b #8-5=3'''







# LESSON 3 ---------------------------------------------------------------------------------------------------------------


# half the given value
'''a=10
b=a>>1
print(b)''' 

# double the given value
'''c=10
d=c<<1
print(d)'''



# given x=10 and y=24 do the logical and, or, xor, not operation and find the output

'''x=10
y=24

print('x = ',x,'\t','{:08b}'.format(x))
print('y = ',y,'\t','{:08b}'.format(y))

print('{:08b}'.format(x))                 # gives the answer in 8 bit format 

a1=x & y
print('x & y = ',a1,'\t','{:08b}'.format(a1))


a2=x | y
print('x | y = ',a2,'\t','{:08b}'.format(a2))


a3=x ^ y
print('x ^ y = ',a2,'\t','{:08b}'.format(a3))


a4=~x
print('~x= ',a4,'\t',bin(a4))


q=x<<1
q2=x>>1
print(q,q2)'''


# note: 'and' operator used when you want to get a T or F answer. it works with the bool output (1 or 0)
# but the '&' operator is used when you want to get a specific value. works with numericals







# LESSON 4 ---------------------------------------------------------------------------------------------------------------


# Create a dictionary of numbers (0 tpo 1000) multiple of 3, 11, and 13.

'''
d3=[]
d11=[]
d13=[]
for v in range(0,1000):
    if v%3==0:
        d3.append(v)
    if v%11==0:
        d11.append(v)
    if v%13==0:
        d13.append(v)

d={
    3: d3
    11: d11
    13: d13
}

print(d[3])
print(d[11])
print(d[13])'''




# Create a dictionary of numbers whose sum is 10, 20 and 30

'''d10=[]
d20=[]
d30=[]
for num in range(0,1001):
    a=num//100                  # double slash --> gives integer value
    b=num%100
    c=b//10
    d=b%10
    sum1=a+c+d
    if sum1==10:
        d10.append(num)
    if sum1==20:
        d20.append(num)
    if sum1==30:
        d30.append(num)

d={
        10: d10,
        20: d20,
        30: d30
    }

print(d[10])
print(d[20])
print(d[30])
'''



'''import os

project_path=os.getcwd()
print(project_path)                       # finds the project pathway (which place it is stored)

file_name = project_path + '//test.txt'   # creates a text file in the given pathway

fpt = open(file_name,"w")

fpt.write("This is a test file")          # command given to write inside the file

# if you want to print numbers inside the file
for r in range(0,10):
    fpt.write(str(r))                     # writes the numbers in string inside the file
    fpt.write('\n')                       # gives a line spacing

    fpt.write('%d\t%d\t%d\n'%(r,2*r,3*r)) # writes the numbers and their corresponding multiplication of x2 and x3

    # means print value, tab space, value, tab space, value and then a line spacing.
    # inside the bracket shows to write r (first value) then 2*r (second value) and then 3*r (third value)


fpt.close();                              # must end the code with this. (should be the last line)'''







# LESSON 5 ---------------------------------------------------------------------------------------------------------------

# Using Pin no. 11, 13 and 15 as GPIO. Control 3 leds ON/OFF one after another.

'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

LED1 = 11
LED2 = 13
LED3 = 15

GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)

while(1):
    GPIO.output(LED1,GPIO.HIGH)
    GPIO.output(LED2,GPIO.LOW)
    GPIO.output(LED3,GPIO.LOW)
    time.sleep(3)                  # 3 is seconds

    GPIO.output(LED1,GPIO.LOW)
    GPIO.output(LED2,GPIO.HIGH)
    GPIO.output(LED3,GPIO.LOW)
    time.sleep(3)

    GPIO.output(LED1,GPIO.LOW)
    GPIO.output(LED2,GPIO.LOW)
    GPIO.output(LED3,GPIO.HIGH)
    time.sleep(3)


while(1):
    GPIO.output(LED1,GPIO.HIGH)
    GPIO.output(LED2,GPIO.HIGH)
    GPIO.output(LED3,GPIO.LOW)
    time.sleep(3)                  # 3 is seconds

    GPIO.output(LED1,GPIO.LOW)
    GPIO.output(LED2,GPIO.HIGH)
    GPIO.output(LED3,GPIO.HIGH)
    time.sleep(3)

    GPIO.output(LED1,GPIO.HIGH)
    GPIO.output(LED2,GPIO.LOW)
    GPIO.output(LED3,GPIO.HIGH)
    time.sleep(3)'''







# LESSON 6/7 ---------------------------------------------------------------------------------------------------------------

'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

P1 = 11
P2 = 13

GPIO.setup(P1,GPIO.OUT)
GPIO.setup(P2,GPIO.OUT)

def CW_Motion():
    GPIO.output(P1,GPIO.HIGH) 
    GPIO.output(P2,GPIO.LOW) 

def aCW_Motion():
    GPIO.output(P1,GPIO.LOW) 
    GPIO.output(P2,GPIO.HIGH) 

def stop_Motion():
    GPIO.output(P1,GPIO.LOW) 
    GPIO.output(P2,GPIO.LOW) 


CW_Motion()
time.sleep(2)

Stop_Motor()
time.sleep(2)

ACW_Motor()
time.sleep(2)'''






# Interface a dc motor with clock-wise and anti-clock wise motion.
# On CW-wise motion, LED-1 should glow, LED-2 should OFF
# On ACW motion, LED1 should OFF and LED2 should glow
# When motor stops, both LED should OFF
# Give beep sound thrice on clock wise motion at interval of 1 sec.
# Give beep sound twict on anti-clock wise motion at interval of 1 sec.
# Give beep sound five times on clock wise motion at interval of 1 sec.
# If IN1 is pressed, CW
# if in2 is pressed ACW
# in3 is pressed Stop Motor
# along with LED status as it is

'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

P1 = 11   # motor
P2 = 13
L1 = 15   # LED
L2 = 17
B1 = 18   # buzzer
In1 = 21
In2 = 23
In3 = 29

GPIO.setup(P1,GPIO.OUT)
GPIO.setup(P2,GPIO.OUT)
GPIO.setup(L1,GPIO.OUT)
GPIO.setup(L2,GPIO.OUT)
GPIO.setup(B1,GPIO.OUT)
GPIO.setup(In1,GPIO.IN)
GPIO.setup(In2,GPIO.IN)
GPIO.setup(In3,GPIO.IN)        # to check the status


def beep(n):
    for r in range(0,n):
            GPIO.output(B1,GPIO.HIGH) 
            time.sleep(1)
            GPIO.output(B1,GPIO.LOW) 
            time.sleep(1)

def CW_Motion():
    GPIO.output(P1,GPIO.HIGH) 
    GPIO.output(P2,GPIO.LOW) 
    GPIO.output(L1,GPIO.HIGH) 
    GPIO.output(L2,GPIO.LOW)
    beep(3) 

def aCW_Motion():
    GPIO.output(P1,GPIO.LOW) 
    GPIO.output(P2,GPIO.HIGH) 
    GPIO.output(L1,GPIO.LOW) 
    GPIO.output(L2,GPIO.HIGH)
    beep(2)

def stop_Motion():
    GPIO.output(P1,GPIO.LOW) 
    GPIO.output(P2,GPIO.LOW) 
    GPIO.output(L1,GPIO.LOW) 
    GPIO.output(L2,GPIO.LOW)
    beep(5)

if In1==LOW:           # means the devices are gonna work
    CW_Motion()
    time.sleep(2)      # means the time space like (2 seconds)

if(In3==LOW):
    stop_Motion()
    time.sleep(2)

if(In2==LOW):
    aCW_Motion()
    time.sleep(2)

CW_Motion()
time.sleep(2)
stop_Motion()
time.sleep(2)
aCW_Motion()
time.sleep(2)
'''






# LESSON 8 (no coding) ---------------------------------------------------------------------------------------------------------------







# LESSON 9---------------------------------------------------------------------------------------------------------------


#max voltage for analog is 3.3V
    
'''from rpi_hardware_pwm import HardwarePWM

DutyCycle = 50
pwm_freq=50
CHANNEL_0 = 0
CHANNEL_1 = 1

pwm = HardwarePWM(pwm_channel=CHANNEL_0, hz=pwnm_freq, chip=0)

pwm.change_duty_cycle(50)   # 0 to 100%

pwm.start(DutyCycle) # full duty cycle

#pwm.change_frequency(25_000)

pwm.stop()'''




# Conrol the LED intensity as below:
# Start with 0 V for 1 sec.
#   Then 1V for 1 sec.
#   Then 2 V for 2 sec.
#   Finally 3 V for 3 sec
#   And 0 V to start again


'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
from rpi_hardware_pwm import HardwarePWM

L1 = 15   # LED --> no need to state/define because you have to physically connect it to the pwm pin that is used during the code

DutyCycle = 0
pwm_freq = 50
CHANNEL_0 = 0
CHANNEL_1 = 1


pwm = HardwarePWM(pwm_channel=CHANNEL_0, hz=pwm_freq, chip=0)

while(1):
    pwm.start(0)
    time.sleep(0)

    pwm.change_duty_cycle(30.3)
    time.sleep(1)

    pwm.change_duty_cycle(60.6)
    time.sleep(2)
  
    pwm.change_duty_cycle(90.9)
    time.sleep(3)
    

pwm.start(DutyCycle) # full duty cycle
pwm.stop()'''






# Clock Pulse: Generate a clock of Freq. = 10 Hz on GPIO-18  (in case of clk it will either be high or low no middle)
# PWM is not intended to work for pulses 


'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
from rpi_hardware_pwm import HardwarePWM

CHANNEL_0 = 0
CHANNEL_1 = 1


pwm = HardwarePWM(pwm_channel=CHANNEL_0, hz=pwm_freq, chip=0)  # no need if we want to create a pulse

for r in range (0,20):
    pwm.start(0)
    time.sleep(0.05)          

    pwm.change_duty_cycle(100)
    time.sleep(0.05)

    
pwm.start(DutyCycle) 
pwm.stop()
'''




# whenever we want to create a pulse (sequence of high and low)   ---> use GPIO


'''import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

CLK_PIN = 37
GPIO.setup(CLK_PIN,GPIO.OUT)

clk_freq = 50         # hertz ----> tells us for how long the pulse is high and low


def clk_pulse(clk_pin,clk_freq):
    time_period = (1/clk_freq)/2
    GPIO.output(clk_pin,GPIO.LOW)
    time.sleep(time_period)
    GPIO.output(clk_pin,GPIO.HIGH)
    time.sleep(time_period)
 
clk_pulse(CLK_PIN,clk_freq)'''







# LESSON 10 ---------------------------------------------------------------------------------------------------------------

'''
    Slave Select Signal  Select the slave
    Put the data (8-bits data) on MOSI pin
    Put the data (8-bits data) on MISO pin
    Clock Pulse Initialization --> Send Clock
    One byte data communication complete
'''


'''import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


SSEL = 3
GPIO.setup(SSEL,GPIO.OUT)

MOSI = 5
GPIO.setup(MOSI,GPIO.OUT)

MISO = 7
GPIO.setup(MISO,GPIO.OUT)

CLK_PIN = 37
GPIO.setup(CLK_PIN,GPIO.OUT)

clk_freq = 50              # ( in hz)

ENABLE = 1
DISABLE = 0

def ssel(flag):
    flag = 1-flag     # to enable/disable the SSEL
    if(flag==0):
        GPIO.output(SSEL,GPIO.LOW)        # SSEL selected
    if(flag==1):
        GPIO.output(SSEL,GPIO.HIGH)       # SSEL disabled
    
def send_data(mosi,miso):
    for r in range(0,8):                # range refers to the 8 bit data
        a = (mosi >> r) & 0x01
        if(a==1):                       # bit =1, MOSI=high
            GPIO.output(MOSI,GPIO.HIGH)
        if(a==0):                       # bit =0, MOSI=low
            GPIO.output(MOSI,GPIO.LOW)

        a = (miso >> r) & 0x01
        if(a==1):
            GPIO.output(MISO,GPIO.HIGH)
        if(a==0):
            GPIO.output(MISO,GPIO.LOW)

        clk_pulse(clk_pin,clk_freq)         # for clk pulse to be generated  ( every clk we will be passing 1 digit)

        

def clk_pulse(clk_pin,clk_freq):
    time_period = (1/clk_freq)/2
    GPIO.output(clk_pin,GPIO.LOW)
    time.sleep(time_period)
    GPIO.output(clk_pin,GPIO.HIGH)
    time.sleep(time_period)


data = [0x23, 0x45, 0x42, 0x56, 0x10, 0x57]    # hexadecial
data = [10, 15, 3, 91]                         # decimal

ssel(SSEL,ENABLE)

for r in range(0,len(data)):     # range refers to the data that is being transfeered
    send_data(data[r],data[r])

# or

for r in data:    
    send_data(r,r)     # automatically converts it to binary format (8 bits)

ssel(SSEL,DISABLE)'''







# LESSON 11.5 ---------------------------------------------------------------------------------------------------------------

'''import serial

COM_PORT="COM6"

ser = serial.Serial(
                     port     = COM_PORT,           ####
                     baudrate = 2400,               ####
                     parity   = serial.PARITY_NONE,
                     stopbits = serial.STOPBITS_ONE,
                     bytesize = serial.EIGHTBITS,
                     timeout  = 1      
                    )
ser.write('a')

data = ser.read()
'''






# LESSON 12 (Data Visulizations)---------------------------------------------------------------------------------------------------------------

# In cmd prompt type -----> pip install matplotlib

'''x = [1, 2, 3, 4, 5,6,7,8,9,10]
y =[2, 34, 42, 12, 78,90,76,54,43,32]

plt.scatter(x,y,color='red')
plt.plot(x,y,color='green')
plt.xlabel('--- x --->')
plt.ylabel('--- y--->')
plt.title('x-y plot')
plt.grid()
plt.show()'''





# plot a scatter and line plot for first 15 elements of a fibonacii series.

'''import matplotlib.pyplot as plt

a=0
b=1
f=[]
f.append(a)
f.append(b)
x=[0,1]

for r in range (2,25):
    t=a+b
    f.append(t)
    a=b
    b=t
    x.append(r)
print(f)

plt.scatter(x,f,color='red')
plt.plot(x,f,color='green')
plt.xlabel('--- x --->')
plt.ylabel('--- f--->')
plt.title('x-f plot')
plt.grid()
plt.show()'''





'''x = [10, 20, 30, 50, 23]   #Total = 170
#y = [6, 12, 18, 29, 41]
ex  = [  0,       0.2,       0,     0,        0 ]
ttl = ['ten', 'twenty','thirty','fifty','seventy']
plt.pie(x,labels=ttl,explode=ex)
plt.title('No. of Students Vs Marks')
plt.show()'''





'''marks = [45, 76, 89]
nos = [34, 50, 67]

plt.bar(nos,marks)
plt.scatter(nos,marks)
plt.plot(nos,marks)
plt.xlabel('--- No. of Students --->')
plt.ylabel('--- Marks--->')
plt.title('No. of Students Vs Marks')
plt.grid()
plt.show()'''





'''x=[]
ex=[]
ttl=[]

for r in range (1,11):
    x.append(r)
    ex.append(0)
    ttl.append(str(x[r-1]))
y=sum(x)

for r in range (0,len(x)):
    t=(x[r]/y) *100
    if t>10:
        ex[r]=0.2

plt.pie(x,labels=ttl,explode=ex)
plt.show()'''







# LESSON 13 -------------------------------------------------------------------------------------------------

# Problem: Create a list of fibonacii series of 50 elements. And plot a bar graph of number that are divisible by 3, 5, and 7.

'''import matplotlib.pyplot as plt

a=0
b=1
f=[]
f.append(a)
f.append(b)
x=[0,1]

for r in range (2,50):
    t=a+b
    f.append(t)
    a=b
    b=t
    x.append(r)
print(f)

divi3=[]
divi5=[]
divi7=[]
for num in f:
    if num%3==0:
        divi3.append(num)
    
    if num%5==0:
        divi5.append(num)
    
    if num%7==0:
        divi7.append(num)

print(divi3)
print(divi5)
print(divi7)
     
c=[len (divi3), len (divi5), len (divi7)]
print(c)

h=[3,5,7]

plt.bar(h,c,color='red')
plt.xlabel('--- divisible by --->')
plt.ylabel('--- count--->')
plt.title('numbers divisible by 3, 5, 7')
plt.show()'''





































