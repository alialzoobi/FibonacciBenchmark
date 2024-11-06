import time
import matplotlib.pyplot as plt

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dynamic(n):
    if n <= 1:
        return n
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Compute Fibonacci numbers iteratively
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update values for next Fibonacci number
    
    return b

def fib_dynamic_rec(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_dynamic(n - 1, memo) + fib_dynamic(n - 2, memo)
    return memo[n]

def fib_matrix(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    def matrix_mult(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
        ]

    def matrix_pow(M, p):
        if p == 1:
            return M
        if p % 2 == 0:
            half_pow = matrix_pow(M, p // 2)
            return matrix_mult(half_pow, half_pow)
        return matrix_mult(M, matrix_pow(M, p - 1))

    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1)
    return result[0][0]

def main():
    # Input limits for each method
    max_n_recursive = 35#int(input("Enter the largest n for recursive: "))
    max_n_dynamic = 140000#int(input("Enter the largest n for dynamic programming: "))
    max_n_matrix = 140000#int(input("Enter the largest n for matrix exponentiation: "))
    step = 1000
    T = 5  # Time limit in seconds

    results = {
        'n': [],
        'recursive': [],
        'dynamic': [],
        'matrix': []
    }

    # Test recursive method
    for n in range(max_n_recursive + 1):
        start_time = time.time()
        try:
            fib_recursive(n)
            execution_time = time.time() - start_time
            if execution_time <= T:
                results['n'].append(n)
                results['recursive'].append(execution_time)
            else:
                break
        except RecursionError:
            print(f"RecursionError for n={n}")

    # Test dynamic programming method
    for n in range(max_n_dynamic + 1):
        if (n > 1000 and n%1000!=0):
            continue
        start_time = time.time()
        fib_dynamic(n)
        execution_time = time.time() - start_time
        if execution_time <= T:
            results['dynamic'].append(execution_time)
        else:
            break

    # Test matrix exponentiation method
    for n in range(max_n_matrix + 1):
        if (n > 1000 and n%1000!=0):
            continue
        start_time = time.time()
        fib_matrix(n)
        execution_time = time.time() - start_time
        if execution_time <= T:
            results['matrix'].append(execution_time)
        else:
            break

    # Adjust the n values to match the results length
    results['n'] = results['n'][:len(results['recursive'])]


    # Output the Fibonacci values for 7, 10, and 28
    test_values = [7, 10, 28]
    print("Fibonacci values for specific indices:")
    for n in test_values:
        print(f"Fibonacci({n}) - Recursive: {fib_recursive(n)}, Dynamic: {fib_dynamic(n)}, Matrix: {fib_matrix(n)}")

    # Plotting results
    plt.figure(figsize=(12, 6))
    
    if results['recursive']:
        plt.plot(results['n'], results['recursive'], label='Classical Recursive', marker='o')
    if results['dynamic']:
        plt.plot(range(len(results['dynamic'])), results['dynamic'], label='Dynamic Programming', marker='o')  # Adjust x-values
    if results['matrix']:
        plt.plot(range(len(results['matrix'])), results['matrix'], label='Fast Matrix Exponentiation', marker='o')  # Adjust x-values

    plt.xlabel('Fibonacci Index (i if i < n ,else: 1000*i)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Fibonacci Calculation Time for Different Methods')
    plt.legend()
    plt.grid(True)
    plt.ylim(0, T + 1)  # Set y-axis limit based on T
    plt.show()

if __name__ == "__main__":
    main()
