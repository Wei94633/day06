# 2.1
def recursion_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursion_sum(n-1)

print(recursion_sum(42))
print("-" * 60)

# 2.2
def palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])


text = input("Enter a text: ")

clean_text = ""

for letter in text:
    if letter.isalnum():
        clean_text += letter.lower()

print(palindrome(clean_text))
print("-" * 60)

# 2.3
import os

def list_files(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        print(full_path)

        if os.path.isdir(full_path):
            list_files(full_path)


list_files(".")
print("-" * 60)