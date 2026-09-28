# 3.1
print(abs(2))
print(abs(-2))
print(abs(-3e4))  # -3x10^4

print(round(3.14159, 2))

print(max([-42, 3e2, 666]))
print("-" * 60)

# 3.2
text = "Beautiful is better than ugly."
print(min(text))
print("-" * 60)
# observation: The result is a space because min() compares the characters in the string.
# the space has a smaller value than the letters.

# 3.3
print(pow(73, 73))
print("-" * 60)

# 3.4
list1 = [False, False, True, False]
list2 = [True, True]

print(any(list1))
print(all(list2))
print("-" * 60)

# 3.5
L1 = [1, 2, 3, 4]
L2 = [5, 7, 9, 32]
L3 = [23, 13, 17, 14, 16, 309]
L4 = [10, 20, 30, 40]

print(sum(L1 + L2 + L3 + L4))
print("-" * 60)

# 3.6
names = ["Joe", "William", "Jack", "Averell"]

print(sorted(names, key=len))
print(sorted(names, key=len, reverse=True))
print("-" * 60)