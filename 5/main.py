def getMaxToys(prices, money):
    start = 0
    total_cost = 0
    max_toys = 0
    
    for end in range(len(prices)):
        total_cost += prices[end]
        
        while total_cost > money:
            total_cost -= prices[start]
            start += 1
        
        max_toys = max(max_toys, end - start + 1)
    
    return max_toys

# Sample Input
n = 7
prices = [1, 4, 5, 3, 2, 1, 6]
money = 6

# Output
print(getMaxToys(prices, money))
