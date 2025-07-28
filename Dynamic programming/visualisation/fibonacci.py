import time

def fib_memoization(n, memo={}, trace=False):
    if n in memo:
        if trace:
            print(f"Retrieving fib({n}) = {memo[n]} from memo")
        return memo[n]
    
    if n <= 1:
        return n
    
    if trace:
        print(f"Computing fib({n})...")
    
    memo[n] = fib_memoization(n-1, memo, trace) + fib_memoization(n-2, memo, trace)
    return memo[n]

def fib_tabulation(n, trace=False):
    if n <= 1:
        return n
    
    table = [0] * (n + 1)
    table[1] = 1
    
    if trace:
        print("Building table...")
    
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
        if trace:
            print(f"table[{i}] = {table[i]}")
    
    return table[n]

def visualize():
    n = 10  # You can change this value for different outputs
    
    print("\nMemoization (Top-Down DP):")
    start = time.time()
    print(f"fib_memoization({n}) =", fib_memoization(n, {}, trace=True))
    print("Time taken:", round(time.time() - start, 4), "seconds\n")
    
    print("Tabulation (Bottom-Up DP):")
    start = time.time()
    print(f"fib_tabulation({n}) =", fib_tabulation(n, trace=True))
    print("Time taken:", round(time.time() - start, 4), "seconds\n")

if __name__ == "__main__":
    visualize()