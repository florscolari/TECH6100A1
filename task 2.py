### Task 2 Pseudocode Guidance
def create_dictionaries(number_of_dict):
    n = 0
    while n != number_of_dict:
        parent_key = input(f"Enter the Key for dictionary #{n+1}: ")
        parent_value = {}
        parent_keys_qty[parent_key] = parent_value
        n += 1

def merge_dictionaries(**kwargs):
    result_dict = {}
    for dict_name, dict_value in kwargs.items():
        print(f"{'-'*10}\nLet's work now on dictionary with key: {dict_name}")
        number_of_pairs = int(input("Enter the number of key-value pairs you would like to add: "))
        i = 0
        while i != number_of_pairs:
            print(f"{'-'*2} Key-value pair #{i+1} {'-'*2}")
            key = input(f"Enter the key: ")
            value = input(f"Enter the value: ")
            dict_value[key] = value
            i += 1
        for key, value in dict_value.items():
            result_dict[key] = value

    print(f"{'-'*10}\nYou have merged {len(kwargs.items())} dictionaries into 1.\nThe result has {len(result_dict.items())} key-value pairs.\n{result_dict}")


## Running Program with User Inputs
parent_keys_qty = {}
nums = int(input("Enter the number of dictionaries you would like to merge: "))
create_dictionaries(nums)
merge_dictionaries(**parent_keys_qty)