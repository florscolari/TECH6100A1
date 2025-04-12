#checks for duplicated key
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


while True:
    value = input('Enter key: ')
    if value in my_dict:
        print("Key exists in the dictionary. Try again")
    else:
        print(value)
        break



        while i != number_of_pairs:
            print(f"{'-'*2} Key-value pair #{i+1} {'-'*2}")
            #todo: must check the key does not exist
            key = input(f"Enter the key: ")
            value = input(f"Enter the value: ")
            dict_value[key] = value
            i += 1
        for key, value in dict_value.items():
            result_dict[key] = value