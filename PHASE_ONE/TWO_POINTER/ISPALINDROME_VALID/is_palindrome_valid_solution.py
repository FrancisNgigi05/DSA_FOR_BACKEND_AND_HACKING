# Function checks if a given string can be a palindrome
# Input: Palindrome string,  Output: True
# Input: None palindrome string, Output: False
"""
Edge case:
> String should include:
 - Combination of lowercase english letters
 - numbers
 - spaces
 - panctuations
"""

def is_palindrome_valid(data: str) -> bool:
    # Checki if string is NULL
    if not data:
        return False
    # Should be more than one letter
    if len(data) < 2:
        return False
    # Convert string to lowercase
    data_lower_case = data.lower()
    # Filter out any characters that are not alphanumeric
    white_listed_string =  ''.join(char for char in data_lower_case if char.isalnum())
    # If input is whitespace
    if len(white_listed_string) < 2:
        return False
    print(white_listed_string)
    # Convert the data to an array
    data_arr = list(white_listed_string)
    # Initializing the pointers
    left, right = 0, len(white_listed_string) - 1

    while left < right:
        # Check if left and right elements are equal
        if data_arr[left] == data_arr[right]:
            # IF True move left forward right backwards
            left += 1
            right -= 1
        else:
            return False
    return True


data = 'a dog! a panic in a pagoda.'
data2 = 'racecar'

# Expected output
# Output:True
# Output: Fasle

print('Output:', is_palindrome_valid(data=data))
print('Output:', is_palindrome_valid(data=data2))

