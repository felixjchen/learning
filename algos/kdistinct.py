s = "pqpqs"
k = 2


def kDistinctChars(s, k):
    substrings = []

    for i in range(len(s)):
        for j in range(i, len(s)):
            substrings.append(s[i:j+1])

    count = 0
    for substring in substrings:

        distinctChars = set([char for char in substring])
        if len(distinctChars) == k:
            count += 1

    return count


print(kDistinctChars(s, k))


if
if
if
if
