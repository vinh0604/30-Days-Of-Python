
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))
print(len(first_name))
print(len(first_name) > len(last_name))
num_five = 5
num_four = 4
total = num_five + num_four
print(total)
diff = num_five - num_four
print(diff)
product = num_five * num_four
print(product)
division = num_five / num_four
print(division)
remainder = num_five % num_four
print(remainder)
exp = num_five ** num_four
print(exp)
floor_division = num_five // num_four
print(floor_division)

radius = 30
area_of_circle = 3.14 * (radius ** 2)
print(area_of_circle)
circum_of_circle = 3.14 * radius * 2
print(circum_of_circle)

first_name = input("Please enter First Name: ")
last_name = input("Please enter Last Name: ")
country = input("Please enter Country: ")
age = int(input("Please enter Age: "))