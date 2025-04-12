## Task 1 values for calculation
def value_to_calculate():
    value = ""
    list_of_value_to_calculate = []
    print(f"Add each number to the dataset by entering it and press enter. Do this for each of them.\nEnter X when you want to close the set.")
    while value.lower() != 'x':
        value = input(f"Value: ")
        list_of_value_to_calculate.append(value)
        if value.lower() == "x":
            list_of_value_to_calculate.pop(-1)
            break
    return print(f"You have entered the dataset: {list_of_value_to_calculate}")

value_to_calculate()