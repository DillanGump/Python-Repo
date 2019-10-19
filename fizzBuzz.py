numbers = []

for i in range(0,201) :
    numbers.append(i)
# for i in numbers :
#     if (numbers[i] % 3 != 0) and (numbers[i] % 5 != 0) :
#         print(numbers[i])
#     elif (numbers[i] % 3 == 0) and (numbers[i] % 5 == 0) :
#         print("Fizzbuzz")
#     else :
#         if numbers[i] % 3 == 0 and numbers[i] % 5 != 0 :
#             print("Fizz")
#         elif numbers[i] % 3 != 0 and numbers[i] % 5 == 0 :
#             print("Buzz")
#         else :
#             print(i, "There has been an error")

for i in numbers :
    output = ""
    number = numbers[i]
    if number % 3 == 0 :
        output += "Fizz "
    if number % 5 == 0 :
        output += "Buzz "
    if number % 7 == 0 :
        output += "Bazz "
    if output == "" :
        print(number)
        continue        
    print(output)


