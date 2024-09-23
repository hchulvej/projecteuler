from time import time

# Memoization dictionary to store results for substrings
memo = {}

def partition_number(number):
    # Convert the number to string to handle partitions
    num_str = str(number)
    
    # Helper recursive function
    def helper(s):
        # If already computed, return from memo
        if s in memo:
            return memo[s]
        
        # Base case: if only one digit, return as a partition
        if len(s) == 1:
            return [(int(s),)]

        partitions = []
        
        # Partition the string in all possible ways
        for i in range(1, len(s)):
            left_part = int(s[:i])
            right_partitions = helper(s[i:])
            # Append the current partition (left_part, and all right partitions)
            for right in right_partitions:
                partitions.append((left_part,) + right)
        
        # Include the whole string as a partition (the original number)
        partitions.append((int(s),))

        # Store the result in memo
        memo[s] = partitions
        return partitions

    # Call the helper function on the entire number as a string
    return helper(num_str)






start = time()

# Fill the memo
for n in range(1,1000001):
    partition_number(n)

print(len(memo.keys()))

end = time()

print("Time: ", end - start)