def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    n = 10
    result = fibonacci_recursive(n)
    print(f"Fibonacci({n}) = {result}")