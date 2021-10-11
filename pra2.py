x = int(input('Enters Your Temperacture: '))
if x >= 25:
    print('It\'s a hot day drink plenty of water')
elif x <= 12:
   print('It\'s So Cold Wear warm clothes')
else:
    print('It\'s a lovely day')


#execrsie of payment of house
good_credit = input('1.yes , 2.No: ')
if good_credit == '1':
    house_value = 1000000
    discount_value = house_value * (10 / 100)
    final_value = house_value - discount_value
    print(f'Original price of House: {house_value}/-')
    print(f'After Discount total price: {final_value}/- ')
    print(f'Discount value: {discount_value}/-')
elif good_credit == '2':
    house_value = 1000000
    discount_value = house_value * (20 / 100)
    final_value = house_value - discount_value
    print(f'Original price of House: {house_value}/-')
    print(f'After Discount total price: {final_value}/- ')
    print(f'Discount value: {discount_value}/-')


