temp = {'Chennai': 35.3,
        'Delhi': 37.4,
        'Goa': 30.7,
        'Kolkata':32.1,
        'Mumbai': 36.5,
        'Ahmedabad': 33.7,
        'Hyderabad': 38.7,
        'Nagpur': 33.0,
        'Patna': 37.9}
while True: 
    inp = input('Enter the city number to check the temperature: ')
    if inp in temp:
        print(f'The temperature in {inp} is {temp[inp]}°C')
    else:
        print('Invalid city name. Try again')
        