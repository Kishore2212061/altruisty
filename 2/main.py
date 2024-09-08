def wordBreak(n, s, dictionary):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
                break

    return 1 if dp[len(s)] else 0

# Example usage
n = 6
s = "ilike"
dictionary = { "i", "like", "sam", "sung", "samsung", "mobile"}
print(wordBreak(n, s, dictionary))  # Output: 1

s = "ilikesamsung"
print(wordBreak(n, s, dictionary))  # Output: 1
