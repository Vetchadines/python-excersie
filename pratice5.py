print('To know how to run the Car enter help to know the features')
command = " "
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car Started')
        else:
            started = True
            print('Car already running')
    #elif 'start' == True:
    elif command == 'stop':
        print('Car Stopped')
    elif command == 'help':
        print('''help: start: To start the Car \nstop: To stop the car\n quit: To quit''')
    elif command == 'quit':
        break
    else:
        print('Sorry, I don\'t Understand')
        break
