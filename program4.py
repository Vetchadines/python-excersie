course = 'Python Course for begginers'
#slicing method
print(course[-1::-1])

print(course[0:])

print(course[0::2])

first = 'Dinesh Kumar'
middle = 'Satya Venkata'
last = 'Vetcha'
#formattng string method
msg = f'{middle} {first} {last} is a coder'

print(msg)

#comparing numbers
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number'))

if num1 > num2:
    print(f'{num1} is greater')
else:
    print(f'{num2} is Greater')