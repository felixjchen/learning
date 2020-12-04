s = '*|*|*'

first, last = s.index('|'), s.rindex('|') + 1

print(s[first:last])
