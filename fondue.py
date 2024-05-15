MOD = 10**9 + 7  
  
def find_ways(n, k, a):  
    # Create a DP array with 2 rows and k columns, initialized to zero  
    dp = [[0] * k for _ in range(2)]  
  
    # Base case: There's one way to make remainder 0 with 0 items  
    dp[0][0] = 1  
  
    # Fill the DP table  
    for i in range(1, n + 1):  
        current = i % 2  
        previous = 1 - current  
  
        # Copy values from the previous row to the current row  
        # This is necessary because each new row should start as a copy of the previous row  
        for j in range(k):  
            dp[current][j] = dp[previous][j]  
  
        for j in range(k):  
            # Calculate the new index to add the values from  
            new_index = (j - a[i-1] % k + k) % k  
            dp[current][j] = (dp[current][j] + dp[previous][new_index]) % MOD  
  
    # The answer is in the last considered 'current' row for remainder 0  
    return dp[n % 2][0]  
  
# Read input from standard input (for example, competitive programming environment)  
n, k = map(int, input().split())  
a = list(map(int, input().split()))  
  
# Get the result from the function  
result = find_ways(n, k, a)  
  
# Print the result to standard output  
print(result)  
