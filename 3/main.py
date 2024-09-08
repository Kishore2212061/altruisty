from collections import deque

def get_stepping_numbers(n, m):
    result = []
    if n == 0:
        result.append(0)
    q = deque([i for i in range(1, 10)])
    while q:
        step_num = q.popleft()
        if n <= step_num <= m:
            result.append(step_num)
        if step_num == 0 or step_num > m:
            continue
        last_digit = step_num % 10
        if last_digit > 0:
            q.append(step_num * 10 + (last_digit - 1))
        if last_digit < 9:
            q.append(step_num * 10 + (last_digit + 1))
    return sorted(result)

n, m = map(int, input().split())
result = get_stepping_numbers(n, m)
print(" ".join(map(str, result)))
