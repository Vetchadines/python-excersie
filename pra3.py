Name = input('Enter Your Name: ')

if len(Name) < 4:
    print('Name Should be Atlest 4 Charaters')
elif len(Name) > 35:
    print('Your name shouldn\'t exceed 35 charaters')
else:
    print('Looks Good')
    print(f' Welcome to the Event: {Name}')