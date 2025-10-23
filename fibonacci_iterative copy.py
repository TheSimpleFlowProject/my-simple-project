def fibonacci_iterative(n):
    """
    Calculates the nth Fibonacci number using an iterative approach.
    
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
    This function takes an integer `n` as input and returns the nth Fibonacci number.
    
    Args:
        n (int): The index of the Fibonacci number to be calculated.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        # Base cases: the 0th and 1st Fibonacci numbers are 0 and 1, respectively.
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        # Iteratively calculate the Fibonacci numbers by updating the variables `a` and `b`.
        a, b = b, a + b
    return b

if __name__ == "__main__":
    # This block of code is executed only when the script is run directly (not imported as a module).
    n = 20
    result = fibonacci_iterative(n)
    print(f"Fibonacci({n}) = {result}")
    # Print the 20th Fibonacci number.