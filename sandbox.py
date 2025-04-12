### Task 3
#Requirements:
#should receive a variable number of positional arguments which are strings.
divider = ('-' * 25) # prints a divider to improve readability.

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

def value_for_placeholder(num):
    """Collects the number of values(str type) on a list based on user's input for placeholders. e.g. if 4 placeholders, then collects 4 values"""
    n = 0
    list_of_value = []
    while n != num:
        value = input(f"Enter the value for placeholder #{n+1}: ")
        list_of_value.append(value)
        n += 1
    return list_of_value

def replace_placeholder_for_values(template, *args):
    formatted_text = template.format(*args)
    return formatted_text.capitalize()

## Running Program with User Inputs
placeholder_count = valid_number_of_placeholder() #Collects number of placeholders (function returns [0] placeholders, [1] template as string)
template_text = placeholder_count[1] # This variable stores the template as s string.
values = value_for_placeholder(placeholder_count[0]) #This variable stores the list of values (to be used as *args)
output = replace_placeholder_for_values(template_text, *values) #passing template text & values to replace placeholder by using format method
print(divider)
print(f"You have entered:\nTemplate: {template_text}\nValues: {values}\nResult: {output}")