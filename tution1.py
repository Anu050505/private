#import matplotlib.pyplot as plt

'''x = [1, 2, 3, 4, 5,6,7,8,9,10]
y =[2, 34, 42, 12, 78,90,76,54,43,32]

plt.scatter(x,y,color='red')
plt.plot(x,y,color='green')
plt.xlabel('--- x --->')
plt.ylabel('--- y--->')
plt.title('x-y plot')
plt.grid()
plt.show()'''



'''x = [10, 20, 30, 50, 70]   #Total = 170
#y = [6, 12, 18, 29, 41]  ------> basically tells us the proportion out of the total
ex  = [  0,       0.2,       0,     0,        0 ]
ttl = ['ten', 'twenty','thirty','fifty','seventy']
plt.pie(x, labels=ttl, explode=ex)
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
    if t>15:
        ex[r]=0.2

plt.pie(x,labels=ttl,explode=ex)
plt.show()'''





'''
x=[0,1,2,3,4,5,10]
y=[24,65,23,6,32,67,12]

plt.bar(x,y,color='red')
plt.scatter(x,y,color='green')
plt.plot(x,y,color='black')
plt.show()'''




































