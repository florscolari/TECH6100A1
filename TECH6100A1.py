# TECH6100 Assessment 1 Florencia Scolari ID 1847863 Apr 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100A1.git

#### ----- GLOBAL ----- ####
# Menu options
menuOptions = {
    1: "Calculate Statistics: Get the mean, median and Population Standard Deviation of the given values.",
    2: "Merge Dictionaries: Get a single dictionary by merging as many dictionaries as you want.",
    3: "Format Strings: Get a string with your values by replacing its placeholders.",
    4: "Exit the program"
}
divider = ('-' * 80) # prints a divider to improve readability.


# Task 0.1 Welcome & Get the user's name -
def welcome(user):
    """To welcome the user when starting the program"""
    print("-" * 80)
    print("Welcome to ADMAS,", user.title(),
          ".\n" """I am Emma, your Data Manipulation Assistant. \nLet's run some analysis Today.""")


# Task 0.2 Display the main menu
def main_menu():
    """To display the main menu to the user"""
    print("-" * 80)
    print("What would you like to do? ")
    for number, task in menuOptions.items():
        print("[", number, "] :", task)
    while True:
        try:
            userMenuChoice = int(input("Choose a number: "))
            if userMenuChoice < 1 or userMenuChoice > 4:  # Checking that is a numeric value within the expected range
                print("Choose a valid number between 1 and 4 please.")
                continue
            return userMenuChoice
        except ValueError as e:
            print(f"{e}. Please enter a number")


## TASK 1 - Calculate statistics
#### T  1.1 values for calculation
def value_to_calculate():
    """Collects user inputs and returns the set of values to pass to calculate_statistics function."""
    list_of_value_to_calculate = []
    print(f"Add each number to the dataset by entering it and press enter. Do this for each of them.\nEnter the word "
          f"Done to close the set.")
    while True:
        value_input = input(f"Value: ")
        if value_input.lower() == "done":
            break
        else:
            pass
        try:
            value = float(value_input)
            list_of_value_to_calculate.append(value)
        except ValueError:
            print(f"This is not a valid value, please enter a number or done to close the dataset.")
    return list_of_value_to_calculate


#### T  1.2 - Calculate statistics
def calculate_statistics(*numbers):
    """Calculates the mean, median and population standard deviation of a given set of numbers (positional
    arguments)."""
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
            'mean': round(float(mean),2),
            'median': round(float(median),2),
            'std_dev': round(deviation, 3)
        }
    else:
        message = "No numbers were given."
        return message



## TASK 2 - Merge dictionaries into a dictionary
#### T  2.1 - Checks a valid number of dictionaries will be created (if not then shows error)
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

#### T  2.2 - Creates N dictionaries with key but empty values
def create_dictionaries(number_of_dict):
    """Creates number of dictionaries based on user's input with empty values as placeholders"""
    parent_keys_qty = {}
    n = 0
    while n != number_of_dict:
        #todo: must check the key does not exist
        parent_key = input(f"Enter the Key for dictionary #{n+1}: ")
        parent_value = {}
        parent_keys_qty[parent_key] = parent_value
        n += 1
    return parent_keys_qty

#### T  2.3 - Adds N key-pair values to each dictionary AND Merges all dictionaries into 1.
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



## TASK 3 - Formatting String by Using Placeholders - format_string()
#### T  3.1 - Checks a valid number of placeholders AND Collects the template text
def valid_number_of_placeholder():
    """ Collects numbers of placeholders AND template as string in a list. Also:
    Checks that a valid number of placeholders (must be at least 1) is input by the user to pass as
    the number to collect values for placeholder using function value_for_placeholder()."""
    placeholder = '{}' #valid placeholder structure
    while True:
        template = input("Write a text. Use {} for each placeholder you want to add. e.g. A {} jumps into the {}. ")
        if placeholder not in template: #checks if at least 1 placeholder is in the string
            print(divider)
            print(f"You have input: {template}\n🔴 No placeholders were found. Must have at least 1. ")
            print(divider)
        elif template.count("{") != template.count("}"): #checks the curly-brace pairs are balanced (= number for both)
            print(divider)
            print(f"You have input: {template}\n🔴 It has invalid structures.\nPlease use ""{} for each "
                f"placeholder you want to add.")
            print(divider)
        else:
            num = template.count(placeholder) #if passes, counts qty of placeholders. Returns an int
            return [num, template]

#### T  3.2 - Collects as many values as number of placeholders were previously collected.
def value_for_placeholder(num):
    """Collects the number of values(str type) on a list based on user's input for placeholders. e.g. if 4 placeholders, then collects 4 values"""
    n = 0
    list_of_value = []
    while n != num:
        value = input(f"Enter the value for placeholder #{n+1}: ")
        list_of_value.append(value)
        n += 1
    return list_of_value

#### T  3.3 - Takes the template text (string) AND Replaces placeholders for values.
def replace_placeholder_for_values(template, *args):
    """Takes the string with placeholders used as template, replaces the placeholders with variable length of
    positional values through string format method"""
    formatted_text = template.format(*args)
    return formatted_text


## Task 1 Main Function
def calculate_statistics_main():
    print(f"\n--- Task 1: Calculate Statistics ---")
    numbers = value_to_calculate()
    print(divider)
    print(f"Dataset: {numbers}")
    calculation = calculate_statistics(*numbers)
    print(f"Calculation Results:")
    for keys, values in calculation.items():
        print(f"{keys.title()}: {values}")

## Task 2 Main Function
def merge_dictionaries_main():
    print(f"\n--- Task 2: Merge Dictionaries ---")
    nums = valid_number_of_dict()
    parent_keys_qty = create_dictionaries(nums)
    merge_dictionaries(**parent_keys_qty)

## Task 3 Main Function
def format_string_main():
    print(f"\n--- Task 3: Format a Given String ---")
    placeholder_count = valid_number_of_placeholder() #Collects number of placeholders (function returns [0] placeholders, [1] template as string)
    template_text = placeholder_count[1] # This variable stores the template as s string.
    values = value_for_placeholder(placeholder_count[0]) #This variable stores the list of values (to be used as *args)
    output = replace_placeholder_for_values(template_text, *values) #passing template text & values to replace placeholder by using format method
    print(divider)
    print(f"You have entered:\nTemplate: {template_text}\nValues: {values}\nResult: {output}")


#### ------ Run The Program - User Interface ------ ####
print("You are just about to access to ADMAS, the Advanced Data Manipulation and Analysis System")
userName = input("Enter your name: ")
welcome(userName)

while True:
    userChoice = main_menu() # The main menu on a loop to run the program

    if userChoice == 1:
        calculate_statistics_main()
    elif userChoice == 2:
        merge_dictionaries_main()
    elif userChoice == 3:
        format_string_main()
    elif userChoice == 4:
        print("Exiting ADMAS, your ally for data manipulation and analysis. Until next time!")
        break
    else:
        print("Invalid choice. Please try again.")

## End of the script - 1847863 F. Scolari KBS Apr 2025 TECH6100 Assessment 1