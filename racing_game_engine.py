a = ''
started = False
print('type "help" if you dont undertand')
while True:
    a = input('>').lower()
    if a == 'start' and started == True:
        print('car is already stared !!!!')

    elif a == 'stop' and started == False:
        print('car is already stoped !!!!')

    elif a == 'start':
        print('car is started')
        started = True

    elif a == 'stop':
        print('car is stopped')
        started = False

    elif a == 'help':
        print('''
type-
'start' to start car
'stop' to stop car
'quit' to end programm
        ''')
    elif a == 'quit':
        print('bye bye!')
        break
    else:
        print('sorry i dont understand')