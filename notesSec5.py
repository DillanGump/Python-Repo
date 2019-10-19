'''
greeting = "Hello" 
name = input("My name is: ")
print(greeting + ", " + name)
'''

#splitString = "This string \nhas been \nsplit over \nseveral lines"
#print(splitString)

#greeting = "Bruce"
#age = 22
#print(greeting + )

'''
a= 12
b= 3
print(a + b / 3 - 4 *12)
print((((a+b) / 3) -4 )*12)

c = a + b
d = c / 3
e = d -4
print(e*12)
'''

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2])
print(parrot[0:6:3])

'''
#starts at 0; skips 1,2,3,; prints 4(0); repeats thru
number = "9,223,327,036,854,775,807"
print(number[1::4])
numbers = "1, 2, 3, 4, 5"
print(numbers[0::3])
string1 = "he's"
string2 = "probably"
print(string1 + " " + string2)
print("hello " *5 + "4")
today = "thursday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")
'''

age = 22
print("My age is " + str(age) + " years")

#replacement fields
print("My age is {0} years".format(age))
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2} """.format(28, 30, 31))

#string formatting operator, legacy py2, need to know
#at least know how to convert to replacement fields
print("My age is %d years " % age)
print("My age is %d %s %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))
    #the number allocates space for formatting

#setting precision of a float
print("Pi is about %12.50f \n" % (22/7))

#formatting with replacement fields
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:4}".format(i, i ** 2, i** 3))

print("Pi is about {0:12.50f} \n".format(22/7))

