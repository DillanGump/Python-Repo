string = "1234567890"

#for char in string: 
 #   print(char)

'''
my_iterator = iter(string)
print(my_iterator)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

for char in string :
    print(char)
print("\n")
for char in iter(string):
    print(char)
'''
import random
numList = []
numListLength = random.randint(2, 10)

for i in range(0, numListLength) :
    numList.append(random.randint(0, 9))

numListIterator = iter(numList)

for i in range(0, len(numList)) :
    print(next(numListIterator))

print("\n")

for i in numList :
    print(i)

