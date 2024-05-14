
   
import numpy as np  
  
def find_ways(n, k, a):  
    # Create a DP array with 2 rows and k columns, initialized to zero  
    dp = np.zeros((2, k), dtype=int)  
      
    # Base case: There's one way to make remainder 0 with 0 items  
    dp[0][0] = 1  
      
    # Fill the DP table  
    for i in range(1, n + 1):  
        current = i % 2  
        previous = 1 - current  
          
        # Copy values from the previous row to the current row  
        # This is necessary because each new row should start as a copy of the previous row  
        dp[current] = dp[previous]  
          
        for j in range(k):  
            # Calculate the new index to add the values from  
            new_index = (j - a[i-1] % k + k) % k  
            dp[current][j] += dp[previous][new_index]  
      
    # The answer is in the last considered 'current' row for remainder 0  
    return dp[n % 2][0]  
  
# Example usage  
n = 5  # Number of packs  
k = 3  # The divisor  
a = [1, 2, 3, 4, 5]  # Cheese bites in each pack  
  
print(find_ways(n, k, a))  # Output the number of ways
import sys  
input = sys.stdin.read  
def main():  
    # Read input from standard input (for example, competitive programming environment)  
    #data = input().split()  
    data = "5 10 1 2 3 4 5".split()
    k = int(data[0])  
    n = int(data[1])  
    a = list(map(int, data[2:2+n]))  
      
    # Get the result from the function  
    result = find_ways(k, n, a)  
      
    # Print the result to standard output  
    print(result)  
  
if __name__ == "__main__":  
    main()  
    
    

