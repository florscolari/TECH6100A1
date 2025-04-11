### Task 2 Pseudocode Guidance



def merge_dictionaries(**kwargs):
    result_dict = {}
    for dict_name, dict_value in kwargs.items():
        print(f"You are updating dictionary: {dict_name}")
        number_of_pairs = int(input("How many key-value pairs do you want to add to this dictionary? "))
        i = 0
        while i != number_of_pairs:
            key = input("Key: ")
            value = input("Value: ")
            dict_value[key] = value
            i += 1
        for key, value in dict_value.items():
            result_dict[key] = value

    print(result_dict)



keys_qty = {}
number_of_dict = int(input("Number of dictionaries "))
i = 0
while i != number_of_dict:
    key = input("Key: ")
    value = {}
    keys_qty[key] = value
    i += 1
print(keys_qty)

merge_dictionaries(**keys_qty)