from typing import Union

def deep_copy(lst: Union[int, list]) -> Union[int, list]:
    if isinstance(lst, int):
        return lst
    else:
        return [deep_copy(x) for x in lst] # Method using a list comprehension; You will learn about these after reading week :P
    """
    Alternative solution without using list comprehension:
    This method is a bit more verbose and slightly slower (list comprehensions have bytecode optimizations that make them faster than for loops), but 
    it's easier to understand for beginners.

    to_return = [] # We're creating a new list to house all our new elements. We cannot use .copy here because we want to create a deep copy, not a shallow copy.
    for i in range(len(lst)): # We're iterating through the list, and for each element, we're calling deep_copy on it. If it is a list, we will get a new list in return. If it is an integer, we append it directly.
        to_return.append(deep_copy(lst[i]))
    return to_return
    """
    
    
def ibranatchi_iterative(n: int) -> int:
    # BASE CASES: These are copied verbatim to the recursive solutio
    # Sometimes base cases in iterative methods aren't as clear, so you'll need to employ partial tracing to figure those out 
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 5
    
    # Pay attention to the pattern in the iterative solution. We're using the same pattern in the recursive solution, just in reverse :p
    sequence = [0, 1, 5]
    for i in range(3, n + 1):
        next_value = sequence[i - 1] * 2 * sequence[i - 2] - 5 * sequence[i - 3]
        sequence.append(next_value) # Each time, we're appending the next value to the sequence. The sequence will hold all the elements from 0 to n 
        # Of the Ibranatchi sequence, and we can return the last element.
        # This was done this way to make the question easier; some midterm qeustions will have a,b,c variables that swap and change, and you will have to keep track of them.
        
        # The sequence list is an "iterative" representation of the call stack in the recursive solution. If you notice, the recursive solution is doing the same thing but in reverse with functino calls. Instead of working it's way up, it's working it's way down while delegating the work to the next function call.

    return sequence[-1]

def ibranatchi_recursive(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 5
    # Fun fact: we don't have to add an else because we're using return statements! This is called the Guard Clause pattern.
    
    # The key to notice is the shifting in the indicies we're using for the recursive calls.
    # Looking at the iterative solution, we can see that the recursive calls are based on the same indicies relative to the current index.
    # Also; Notice that next_value always stores the result of the recursive call. This is a hint that we can use the result of the recursive call directly.
    
    # With all this info, we get: 
    return 2 * ibranatchi_recursive(n - 1) * ibranatchi_recursive(n - 2) - 5 * ibranatchi_recursive(n - 3)
    # Remember the analogy: Recursion does the minimum amount of work to solve the problem in each recursive fall before delegating the rest of the work to the next recursive call. 
    # Here, we're working our way down to the base case, then through the method call stack we're working our way back up to the original call.
    # This is the *inverse* of the iterative solution, which works it's way up to the final value from the base case.


# DO NOT SCROLL DOWN UNLESS YOU WANT TO SEE THE SOLUTION FOR THE BONUS QUESTION
# I DO NOT SUGGEST LOOKING AT THE ANSWER BEFORE TRYING TO SOLVE THE QUESTION YOURSELF

# Hint for the bonus question: 
# Recall in MAT102 how we defined an even number as: 2k, k \in Z and an odd number as 2k + 1, k \in Z


def is_odd(n: int) -> bool:
    if n == 0: # Base case
        return False
    return is_even(n - 1) 

def is_even(n: int) -> bool:
    if n == 0: # Base case
        return True
    return is_odd(n - 1) 