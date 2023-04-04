a = True
while a:
    print("Python")
    a = False
print("Program")

result==>>
Python
Program

a = 10
i = 1
while i<=0:
    if (i % 2) == 0:
        print(i*i)
    i = i + 1


a = 8
c = 2
sum = 0
while c < a:
    sum = ((sum + a) + c)
    a = (a - 1)
    c = (c + 1)
print(sum)



a = 11
count = a+1
while count<=(a+10):
    print(count)
    count = count+1
result==>>
3
4
5
6
7
8
9
10
11
12

a = 7
b = 3
count = a
sum = 0
while count<(a+b):
    sum = sum+count
    count = count+1
print(sum)
reasult==>>24



n=4
count=0
while count<n:
    print("* "*(count+1))
    count=count+1
result==>>    
* 
* * 
* * * 
* * * * 


a=6
count=1 
sum=0
while count<=a:
    sum=(sum+count)
    count=(count+1) 
print(sum)

result==>>21


n=3,8,11,25
count = 0
sum = 0
while count<n:
    number = int(input())
    sum  = sum+number
    count = count+1
print(sum)
result==>>44



a = python
count = 0
lenght = len(a)
while count<(lenght):
    print(a[count])
    count=count+1
result==>>
P
y
t
h
o
n




a = Cool
lenght = len(a)
count = 0
while count<lenght:
    print(a[0])
    count=count+1
result===>>
C
C
C
C


a = shine
count=0
lenght = len(a)
while count<lenght:
    print(""+a[count])
    count=count+1
result==>>
s
h
i
n
e


a = 4 
count=1
while count<=a:
    repeat=1
    while repeat<=a:
        print(count,end="")
        repeat=repeat+1
    print()
    count=count+1

result==>>
1111
2222
3333
4444



a = 4
b = 5
row=1
while row<=a:
    col=1
    while col<=b:
        print("*",end="")
        col=col+1
    print()
    row=row+1
result==>>
*****
*****
*****
*****



a = 5
count=1
while count<=a:
    print((str(count)+" ")*count)
    count=count+1
result==>>
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 



a = 4
counter=1
while counter<a:
    print("* "*counter)
    counter=counter+1
print("+ "*a)

result==>>
* 
* * 
* * * 
+ + + + 


a = int(input())
count=1
second=1
while count<=a:
    while second<=a:
        print(second*str(second))
        second=second+1
    print(count*str(count))
    count=count+1
result==>>
1
22
333
1
22
333