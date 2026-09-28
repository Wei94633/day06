# 2.1
def  find_longest_word(words):
    sorted2 = sorted(words, key=len, reverse=True)
    print(sorted2[0])

find_longest_word(["apple", "banana", "cherry", "kiwi"]) 

# 2.2
def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

print(count_digits(42000))