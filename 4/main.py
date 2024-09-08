def minimize_ticket_price(ticket_price, k):
    price = list(ticket_price)
    length = len(price)
    stack = []
    
    for digit in price:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    while k > 0:
        stack.pop()
        k -= 1
    
    minimized_price = ''.join(stack).lstrip('0')
    
    return minimized_price if minimized_price else '0'

ticket_price = input().strip()
k = int(input().strip())
print(minimize_ticket_price(ticket_price, k))
