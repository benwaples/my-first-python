start_message = 'Car started... ready to go'
stop_message = 'Car has stopped'
help_message = '''
say start to start your car
say stop to stop your car
say quit to quit game
'''
has_quit = False

while not has_quit:
    user_input = input('>')
    if user_input == 'start':
        print(start_message)
    if user_input == 'stop':
        print(stop_message)
    if user_input == 'help':
        print(help_message)
    if user_input == 'quit':
        print('game over')
        has_quit = True
    else:
        print('idk wtf you mean')


