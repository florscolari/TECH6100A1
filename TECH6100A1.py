# TECH6100 Assessment 1 Florencia Scolari ID 1847863 Apr 2025

## TASK 1 - Calculate statistics
def calculate_statistics(*numbers):
    if len(numbers) > 0:
        """To get the MEAN"""
        mean = sum(numbers) / len(numbers)  # average value

        """To get the MEDIAN"""
        median = sorted(numbers)
        """Calculate Median for 2 cases: list is odd or list is even"""
        m = len(numbers) // 2  # m is the middle point. '//' is floor division, rounded to min closest digit
        if len(numbers) % 2 != 0:  # reminder not equal to 0 = ODD
            median = numbers[m]
        elif len(numbers) % 2 == 0:  # reminder equals to 0 = EVEN
            median = (numbers[m - 1] + numbers[m]) / 2  # Calculating median for even numbers

        """To get the POPULATION STANDARD DEVIATION"""
        temp = []
        for item in numbers:
            item = (item - mean)  # 2. Subtract the mean from each data point.
            item = item * item  # 3. Square each deviation to make it positive.
            temp.append(item)  # Hold all squared deviations together (list)
        total = 0
        for num in temp:
            total += num  # 4. Sum of all squared deviations together
        variance = total / len(numbers)  # 5. Divide the sum by the number of data points (called Variance)
        deviation = variance ** 0.5  # 6. Get the square root of the variance (called population std deviation)

        return {
            'mean': float(mean),
            'median': float(median),
            'std_dev': round(deviation, 3)
        }
    else:
        message = "No numbers were given."
        return message

## TASK 2 - Merge dictionaries into a dictionary
#todo: add program menu
def main_menu():
    """Start the program with options available for users"""
    print("list of options from main menu")

### Task 2 with Pseudocode Guidance
def create_dictionaries(number_of_dict):
    """Creates number of dictionaries based on user's input with empty values as placeholders"""
    n = 0
    while n != number_of_dict:
        #todo: must check the key does not exist
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
            #todo: must check the key does not exist
            key = input(f"Enter the key: ")
            value = input(f"Enter the value: ")
            dict_value[key] = value
            i += 1
        for key, value in dict_value.items():
            result_dict[key] = value

    print(f"{'-'*10}\nYou have merged {len(kwargs.items())} dictionaries into 1.\nThe result has {len(result_dict.items())} key-value pairs.\n{result_dict}")

def valid_number_of_dict():
    """Checks that a valid number of dict (must be higher than 1) is input by the user to pass as the nums for create_dictionaries()."""
    while True:
        try:
            nums = int(input("Enter the number of dictionaries you would like to merge: "))
            if nums <= 1:
                print(f"{nums} is not a valid number. Please enter a number higher than 1 to merge dictionaries.")
                continue
            return nums
        except ValueError as e:
            print(f"{e}. Please enter a number")

print(f"\nThis is Task 1. Needs user inputs")
test3 = calculate_statistics(1, 2, 3, 4, 5)
test4 = calculate_statistics(10, 15, 20, 25, 30, 35)

print('Test 3', test3)
print('Test 4', test4)

## Running Program with User Inputs
print(f"\nThis is Task 2")
nums = valid_number_of_dict()
parent_keys_qty = {}

create_dictionaries(nums)
merge_dictionaries(**parent_keys_qty)