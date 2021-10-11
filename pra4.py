weight = int(input('Enter Your Weight: '))
option = input('(L)bs or (K)gs')

#option.upper() = 'L':
if option == 'L' or 'l':
    converted = weight * 0.45
    print(f'You are {converted} Kilos')
else:
    converted = weight // 0.45
    print(f'You are {converted} pounds')