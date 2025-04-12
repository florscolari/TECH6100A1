#checks for duplicated key
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


while True:
    value = input('Enter key: ')
    if value in my_dict:
        print("Key exists in the dictionary. Try again")
    else:
        print(value)
        break

