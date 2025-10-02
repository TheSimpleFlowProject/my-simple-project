def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number using recursion.
    
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1. This function implements the recursive approach to calculate the
    nth number in the Fibonacci sequence.
    
    Args:
        n (int): The position of the Fibonacci number to calculate, starting from 0.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        # Base case: the first two Fibonacci numbers are 0 and 1
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    # Recursive case: calculate the nth Fibonacci number by calling the function
    # recursively with n-1 and n-2, and adding the results

if __name__ == "__main__":
    """
    The main entry point of the program.
    
    This block of code is only executed when the script is run directly (not imported as a module).
    It calculates the 10th Fibonacci number and prints the result.
    """
    n = 10
    result = fibonacci_recursive(n)
    print(f"Fibonacci({n}) = {result}")