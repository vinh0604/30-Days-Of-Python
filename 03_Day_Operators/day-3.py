# Arithmetic Operations in Python
# Integers

import math


print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

age = 32
height = 1.68
complex = 1 + 1j

base = float(input('Enter base: '))
height = float(input('Enter height: '))
print('The area of the triangle is ', 1/2 * base * height)

size_a = float(input('Enter side a: '))
size_b = float(input('Enter side b: '))
size_c = float(input('Enter side c: '))
print('The perimeter of the triangle is ', size_a + size_b + size_c)

rect_length = float(input('Enter rectangle length: '))
rect_width = float(input('Enter rectangle length: '))
print('The area of the rectangle is ', rect_length * rect_width)
print('The perimeter of the rectangle is ', 2 * (rect_length + rect_width))

circle_radius = float(input('Enter circle radius: '))
print('The area of the circle is ', math.pi * (circle_radius ** 2))
print('The circumference of the circle is ', math.pi * circle_radius * 2)

formula = 'y = 2x - 2'
slope1 = 2
print(f'The slope of {formula} is ', slope1)
print(f'The X-intercept of {formula} is (', (0 + 2) / 2, ', 0)')
print(f'The Y-intercept of {formula} is (0, ', (2 * 0) - 2, ')')

p1 = (2,2)
p2 = (6, 10)
slope2 = (p2[1] - p1[1]) / (p2[0] - p1[0])
print(f'The slope between {p1} and {p2} is', slope2)
print(f'The euclidean distance between {p1} and {p2} is', math.sqrt(((p2[1] - p1[1]) ** 2) +  ((p2[0] - p1[0]) ** 2)))

print(slope1 == slope2)
print(slope1 > slope2)

print('The value of x which y is going to be 0 in this formula (y = x^2 + 6x + 9) is ', 0 - 3)
print('The length of "python" is ', len('python'))
print('The length of "dragon" is ', len('dragon'))
print(len('python') != len('dragon'))
print(('on' in 'python') and ('on' in 'dragon'))
print('jargon' in 'I hope this course is not full of jargon')
print(('on' not in 'python') and ('on' not in 'dragon'))
print(str(float(len('python'))))

def is_even(num: int):
    if (num % 2) == 0: 
        return True
    return False

print((7 // 3) == int(2.7))
print(type('10') == type(10))
print(int(9.8) == 10)

hours = int(input('Enter hours: '))
rate_per_hr = int(input('Enter rate per hour: '))
print('Your weekly earning is ', hours * rate_per_hr)

years = int(input('Enter number of years you have lived: '))
seconds = years * 365 * 24 * 60 * 60
print(f'You have lived for {seconds} seconds.')

for i in range(5):
    for j in range(5):
        if j == 0:
            print('1', end=' ')
        else:
          print((i + 1) ** (j-1), end=' ')
    print('\n', end='')