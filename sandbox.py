### Task 2 v2
def create_dictionary_name(name, pairs):
    temp = {}
    i = 0
    while i != pairs:
        print(f"Values for key:value pair {i + 1}: ")
        key = input("Key: ")
        value = input("Value: ")
        temp[key] = value
        i += 1
    print(f"You have created a dictionary with {i} pairs: {name}={temp}")



create_dictionary_name(input("Enter dictionary's name: "), int(input("Enter how many key:value pairs for this dictionary (e.g. 3): ")))

print('-'*20)

### Task 2 v1
def create_dictionary(pairs):
    temp = {}
    i = 0
    while i != pairs:
        print(f"Values for key:value pair {i + 1}: ")
        key = input("Key: ")
        value = input("Value: ")
        temp[key] = value
        i += 1
    print(f"You have created a dictionary with {i} pairs: {temp}")


while True:
    try:
        create_dictionary(int(input("Enter how many key:value pairs for this dictionary (e.g. 3): ")))
    except ValueError as e:
        print(f"{e}. Please enter a number")
    #todo: exception for number 0
    else:
        break

print('-'*20)







print('-'*20)
def print_shopping_list(*items, **prices):
    for item in items:
        print(f"{item}: ${prices.get(item, 'N/A')}")

print_shopping_list('Apple', 'Banana', 'Orange', Apple=1.99, Orange=2.49)

thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict)




