import os



while True:

    menu_text = '''
    1. Acquire Rooted Mobile Device
    2. Extract Files from Created Dataset
    3. Parse All Collected Files from Extracted Files
    '''
    print(menu_text)
    choice = input('Choose from the following options\n')
    
    if choice == '1':
        print('You chose 1')
    elif choice == '2':
        print('You chose 2')
    elif choice == '3':
        print('You chose 3')
    else: 
        print('Choose a valid input')
        if os.name == 'nt':
            os.system('cls')
    