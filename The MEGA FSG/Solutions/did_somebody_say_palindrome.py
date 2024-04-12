def is_palindrome_recursive(word: str) -> bool:
    if len(word) <= 1: # If we have an empty string or a string with one character, it is a palindrome. This is our base case.
        return True
    if word[0] == ' ': # If our "left" pointer is a space, we move it to the right and call the function again.
        return is_palindrome(word[1:])
    if word[-1] == ' ': # Similarly, if our "right" pointer is a space, we move it to the left and call the function again.
        return is_palindrome(word[:-1])
    return word[0] == word[-1] and is_palindrome(word[1:-1]) # If the characters at the left and right pointers are the same, we move both pointers towards the center and call the function again. If they are not the same, we return False.

def is_palindrome_iterative(word: str) -> bool:
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] == ' ':
            left += 1
            continue
        if word[right] == ' ':
            right -= 1
            continue
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

# Tests:
for is_palindrome in [is_palindrome_recursive, is_palindrome_iterative]:
    print("Testing", is_palindrome.__name__)
    print(is_palindrome('racecar')) # True
    print(is_palindrome('hello')) # False
    print(is_palindrome('taco cat')) # True
    print(is_palindrome('anna')) # True
    print(is_palindrome('borrow or rob')) # True
    print(is_palindrome('ewe')) # True
    print(is_palindrome('was it a car or a cat i saw')) # True
    print(is_palindrome('')) # True