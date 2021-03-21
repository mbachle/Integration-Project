# Mason Bachle
# I could not think of any creative ideas, so I am really just making a combination of code
string1 = 'Hello, operator',
print(string1 * 3)  # the * string repetition operator creates replicates of the string the amount inserted after *
print('Whom am I speaking to today?', sep='')  # sep adds or removes spaces
name = input("Enter your name: ")
age = input("Enter your age: ")
print("How old are you?", age)
print("Hello", name + " What can I assist you with today?", end="\n")
string1 = "calculator function examples: "
string2 = " addition calculations:"
print(string1 + string2)  # the concatenate operator adds 2 strings to the same line
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
sum = num1 + num2  # the + symbol represents addition
print("addition = ", sum)
print("subtraction calculations:")
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
difference = num1 - num2  # the - symbol represents subtraction
print("Difference = ", difference)
print("multiplication calculations:")
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
product = num1 * num2  # the * symbol represents multiplication
print("Multiplication = ", product)
print("division calculations:")
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
quotient = num1 / num2  # the / symbol represents division
print("Division = ", quotient)
print("Floor division calculations:")
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
quotient = num1 // num2  # the // symbol represents floor division which rounds to the last whole number
print("Floor division = ", quotient)
print("exponential calculations:")
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
product = num1 ** num2  # the ** symbol represents exponents
print("Exponential = ", product)
print("modulus calculations:")
firstNumber = input("Enter a number: ")
secondNumber = input("Enter another number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
quotient = num1 % num2  # the % symbol represents modulus which is the remainder of how many times a full number can
# go into another number, will always be 0-one less than the dividing number
print("Modulus = ", quotient)
print("standard conditional statements: ")
firstNumber = input("Enter a: ")
secondNumber = input("Enter b: ")
a = int(firstNumber)
b = int(secondNumber)
if b > a:
    print("b is greater than a") # prints "b is greater than a" if b is greater than a
elif a == b:
    print("a and b are equal") # prints "a and b are equal" if a is equal to b
else:
    print("a is greater than b") # prints a is greater than b if nothing else
firstNumber = input("Enter a: ")
secondNumber = input("Enter b: ")
a = int(firstNumber)
b = int(secondNumber)
print(a != b) # produces true if inputs are not equal, false if they are equal
print(a == b) # produces true if a and b are equivalent, false if they are not
print(a >= b) # produces true if a is greater than or equal to be, false if a is neither 
print("Boolean operators: ")
firstNumber = input("Enter a: ")
secondNumber = input("Enter b: ")
thirdNumber = input("Enter c: ")
a = int(firstNumber)
b = int(secondNumber)
c = int(thirdNumber)
print(a < b and a < c) # produces a True output if a is less than b and c, false if not
print(a < b or a < c) # produces a True ouput if one condition is true, false if not
print(not(a < b and a < c)) # not reverses the result
print(" For Loops:")
for x in range(3, 25, 3): # in implements iterative structures
    print(x) # the for loop uses a range function starts at 3, increases by 3 as much as it can hitting 30
print(" While Loops:")
count = 0
while count < 8:
    print(count)
    count += 2 # The while loop continues as long as all boolean expressions are met
def my_function(friend1, friend2, friend3, friend4,):
    print("My newest friend is " + friend4) #
my_function(friend1 = "Nick", friend2 = "Devan", friend3 = "Dylan", friend4 = "Nathan")# I created a code using a keyword so that the argument didnt rely on the order



