import random


# A function to randomly select a item
# from stream[0], stream[1], .. stream[i-1] 
def select_random(x):
    # The resultant random number
    res = 0

    # Count of numbers visited  
    # so far in stream 
    count = 0

    # increment count of numbers  
    # seen so far 
    count += 1

    # If this is the first element  
    # from stream, return it 
    if count == 1:
        res = x
    else:
        # Generate a random number  
        # from 0 to count - 1 
        number = random.randrange(count)

        # Replace the prev random number  
        # with new number with 1/count  
        # probability 
        if number == count - 1:
            res = x
    return res


# Driver Code
stream = [1, 2, 3, 4]
n = len(stream)

# Use a different seed value  
# for every run. 
for i in range(n):
    print("Random number from first",
          (i + 1), "numbers is",
          select_random(stream[i]))
