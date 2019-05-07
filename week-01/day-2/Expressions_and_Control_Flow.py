# Modify this program to greet you instead of the World
print("Hello, Haoxiang!")

# Modify this program to print Humpty Dumpty riddle correctly
print("Humpty Dumpty sat on a wall,")
print("Humpty Dumpty had a great fall.")
print("All the king's horses and all the king's men.")
print("Couldn't put Humpty together again.")

# Greet 3 of your classmates with this program, in three separated lines
print('Hello, Ke!\nHello, Angela!\nHello, Santi!')

# Write a program that prints a few details to the terminal window about you
name = "Haoxiang Weng"
age = 25
height = 1.72
print(name)
print(age)
print(height)

# Create a program that prints a few operations on two numbers: 22 and 13
print(13 + 22)
print(22 - 13)
print(22 * 13)
print(22 / 13)
print(22 // 13)
print(22 % 13)

# coding_hours
daily = 6
semester = 17
workhour = semester * 52
workday = semester * 5
codinghour = daily * workday
print("The coding hour is " + str(codinghour))
print("The percentage of coding hour is " + str(round((codinghour / workhour) * 100, 2)) + '%')

# favorite number
favorite_number = 7
print("My favorite number is : " + str(favorite_number))

# swap value
a = 123
b = 526
a = 526
b = 123
print(a)
print(b)

# BMI
massInKg = 81.2
heightInM = 1.78
print("the BIM is: " + str(round(massInKg / (heightInM ** 2), 2)))

# Basic Info
My_name = "Haoxiang Weng"
My_age = 25
My_height = 1.72
Am_I_married = False

print(My_name)
print(My_age)
print(My_height)
print(Am_I_married)

# variable mutation
a = 3
a = a + 10
print(a)

b = 100
b = b - 7
print(b)

c = 44
c = c * 2
print(c)

d = 125
d = d / 5
print(d)

e = 8
e = e ** 3
print(e)

f1 = 123
f2 = 345
print(f1 > f2)

g1 = 350
g2 = 200
print(2*g2 > g1)

h = 1357988018575474
print(h%11 == 0)

i1 = 10
i2 = 3
print(i1 > i2**2 and i1 < i2**3)

j = 1521
print(j%3 == 0 or j%5 ==0)

# cuboid
length = 4.65
width = 3.21
height = 1.45
print("Surface Area: "+str(round(length*width*2+width*height*2+length*height*2)))
print("Volumn: "+str(round(length*width*height)))

# second in a day
current_hours = 14
current_minutes = 34
current_seconds = 42

print("The remining seconds is "+str(60-current_seconds+60*(59-current_minutes)+60*60*(23-current_hours)))

# Hello user
print("Please enter your name:")
b = input()
print("Hello, "+str(b)+"!")

# mile to kilometers
print("Please enter the mile:")
a = int(input())
b = a*1.6
print(str(round(b,2))+"km.")

# animals and legs
print("How many chickens the farmer has? ")
chicken = int(input())
print("How many pigs the farmer has?")
pig = int(input())
print("The total legs are: "+str(chicken*2 + pig*4))

# average_of_input
print("Please enter five integers")
input1 = int(input())
input2 = int(input())
input3 = int(input())
input4 = int(input())
input5 = int(input())
a = [input1,input2,input3,input4,input5]
b = sum(a)/5
print("Sum: "+ str(sum(a))+", Average: "+str(round(b,2)))

# odd or even
print("Please enter a number")
a = int(input())
if a%2 == 0:
    print("Even")
else:
    print("Odd")

# one two a_lot
print("Please enter a number")
a = int(input())
if a <= 0:
    print("Not enough")
elif a == 1:
    print("One")
elif a == 2:
    print("Two")
else:
    print("A lot")

# bigger one
print("Please enter two different numbers")
input1 = int(input())
input2 = int(input())
if input1 > input2:
    print(str(input1))
else:
    print(str(input2))

# Party indicator
print("How many girls come to party?")
girl = int(input())
print("How many boys come to party?")
boy = int(input())
total = girl + boy

if girl == boy and total > 20:
    print("The party is exllent!")
elif girl != boy and total > 20:
    print("Quite cool party!")
elif total < 20:
    print("Average Party...")
elif girl == 0:
    print("Sausage Party")

# conditional variable mutation
a = 24
out = 0
if a%2 == 0:
    out += 1
print(out)

b = 13
out2 = ""
if b >= 10 and b <= 10:
    out2 = "Sweet!"
elif b < 10:
    out2 = "Less!"
elif b > 20:
    out2 = "More!"
print(out2)

c = 123
credits = 100
is_bouns = False
if credits >= 50 and is_bouns == False:
    c -= 2
elif credits < 50 and is_bouns == False:
    c -= 1
elif is_bounds == True:
    c = c
print(c)

d = 8
time  = 120
out3=""
if d%4 == 0 and time <= 200:
    out3 = "check"
elif time > 200:
    out3 = "Time out"
else:
    out3 = "Run Forest Run!"
print(out3)

# I won't cheat on the exam
for i in range(0,100):
    print("I won\'t cheat on the exam ")

# print_even
for i in range(0,501):
    a = i
    if a%2 == 0:
        print(a)

# multiplication table
print("Please enter a number")
a = int(input())
for i in range(1,11):
    print(str(i)+" * "+str(a)+" = "+str(i*a))

# count from to
print("Please enter two numbers")
input1 = int(input())
input2 = int(input())
if input1 >= input2:
    print("The second number should be bigger")
else:
    for i in range(input1, input2):
        print(i)

# fizzbuzz
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

#draw triangle
print("Please enter a number")
a = int(input())
for i in range(1,a+1):
    print("*"*i)

# draw pyramid
print("Please enter a number")
a = int(input())
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))

# draw dimond
print("Please enter a number")
a = int(input())
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))
for i in range(a-1,0,-1):
    print(" " * (a - i) + "*" * (2 * i - 1))

# draw square
print("Please enter a number")
a = int(input())
for i in range(1,a+1):
    if i == 1 or i == a:
        print("%"*a)
    else:
        print("%"+" "*(a-2)+"%")

# draw diagnoal
print("I cannot solve this question. Sorry!")

# guess number
n = 20
print("Please enter your guess")
a = int(input())
while n != a:
    if n > a:
        print("The stored number is higher")
        print("Please guess again")
        a = int(input())
    elif n < a:
        print("The stored number is lower")
        print("Please guess again")
        a = int(input())
print("You found the number: "+str(n))

# parametric average
print("How many numbers do you want to calculate")
n = int(input())
print("Please enter those numbers")
l1 = []
for i in range(n):
    a = int(input())
    l1.append(a)
s = sum(l1)
ave = round(s/n,1)
print("Sum: "+str(s)+", "+"Average: "+str(ave))

# draw chess table
for i in range(8):
    if i%2 == 0:
        print("% "*4)
    else:
        print(" %"*4)

# substring
def substr(str, keyword):
    a = str.index(keyword)
    #still working on it
    ##if a:
        ##print(a)
    ##else:
        ##return -1

