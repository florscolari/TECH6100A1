### Task 3
#Requirements:
#should receive a variable number of positional arguments which are strings.
divider = ('-' * 25) # prints a divider to improve readability.

def valid_number_of_placeholder():
    """Checks that a valid number of placeholders (must be at least 1) is input by the user to pass as
    the nums for create_placeholder()."""
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
            return num
## Running Program with User Inputs
test = valid_number_of_placeholder()
print(test)