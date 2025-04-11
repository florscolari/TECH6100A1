def main_menu():
    print("list of options from main menu")

### Task 2 Pseudocode Guidance
def create_dictionaries(number_of_dict):
    """Creates number of dictionaries based on user's input with empty values as placeholders"""
    n = 0
    while n != number_of_dict:
        parent_key = input(f"Enter the Key for dictionary #{n+1}: ")
        parent_value = {}
        parent_keys_qty[parent_key] = parent_value
        n += 1
    return parent_keys_qty

def merge_dictionaries(**kwargs):
    """Adds key-value pairs to the number of dictionaries created by create_dictionaries() and merges them into 1."""
    result_dict = {}
    for dict_name, dict_value in kwargs.items():
        print(f"{'-'*10}\nLet's work now on dictionary with key: {dict_name}")
        while True:
            try:
                number_of_pairs = int(input("Enter the number of key-value pairs you would like to add: "))
            except ValueError as e:
                print(f"{e}. Please enter a number")
            else:
                break
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


def valid_number_of_dict():
    while True:
        try:
            nums = int(input("Enter the number of dictionaries you would like to merge: "))
            if nums <= 1:
                print(f"{nums} is not a valid number. Please enter a number higher than 1 to merge dictionaries.")
                continue
            return nums
        except ValueError as e:
            print(f"{e}. Please enter a number")

## Running Program with User Inputs
nums = valid_number_of_dict()
parent_keys_qty = {}
create_dictionaries(nums)
merge_dictionaries(**parent_keys_qty)