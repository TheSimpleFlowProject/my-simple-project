def fibonacci_iterative(n):
    """
    Calculates the nth Fibonacci number using an iterative approach.
    
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1. This function calculates the nth Fibonacci number by iteratively
    updating the values of the previous two Fibonacci numbers until the nth number is reached.
    
    Args:
        n (int): The index of the Fibonacci number to calculate, where n >= 0.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        # If n is 0 or 1, return n, as the first two Fibonacci numbers are 0 and 1 respectively.
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        # Iteratively update the values of the previous two Fibonacci numbers until the nth number is reached.
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = 10
    result = fibonacci_iterative(n)
    print(f"Fibonacci({n}) = {result}")
    # Call the fibonacci_iterative function with n=10 and print the result.