class details:
    def __init__(self, name, age):
        self.person = name
        self.age = age

Name1 = input('Enter Your Name: ')
names = details(Name1)

Age1 = int(input('Enter Your Age: '))
ages = details(Age1)

print(names.name)
print(ages.age)

