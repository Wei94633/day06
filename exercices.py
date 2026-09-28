# No builtin functions

# Make a function to check if a number n is even or odd

def is_even(n):
    if n % 2 == 0:
        print("odd")
    else:
        print("even")

is_even(int(input("is_even - enter a number: ")))

# Make a function to print the last char of a string

def last_char(string):
    print(string[-1])

last_char(input("last_char - enter a string: "))

# Make a function to print the n first char of a string

def n_first_char(string, n):
    print(string[:n])

n_first_char(input("n_first_char - enter a string: "), int(input("n_first_char - enter a number: ")))

# Make a function to print the n last char of a string

def n_last_char(string, n):
    print(string[-n:])

n_last_char(input("n_last_char - enter a string: "), int(input("n_last_char - enter a number: ")))

# Make a function to replace every char x with y

def my_replace(string, x, y):
    result = ""
    for i in string:
        if i == x:
            result += y
        else:
            result += i
    return result

my_replace(input("my_replace - enter a string: "), input("my_replace - enter a char: "), input("my_replace - enter a char: "))

# Make a function that tell if the number a is bigger than the number b

def my_bigger(a, b):
    if a > b:
        print("number", a, "is bigger than the number",  b)
    else:
        print("number", b, "is bigger than the number",  a)

my_bigger(int(input("my_bigger - enter number a: ")), int(input("my_bigger - enter number b: ")))

# Make a function that print a value depending on the input
# n = 42, output "a"
# n < 21, output "b"
# n divisible by 5, output "c"

def select(n):
    if n == 42:
        print("a")
    if n < 21:
        print("b")
    if n % 5 == 0:
        print("c")

select(int(input("select - input a number: ")))

# Make a function that reverse a string

def reverse(string):
    print(string[::-1])

reverse(input("reverse - enter a string: "))

# Make a function that add a at the beggining and b at the end of a list

def my_add(l, a, b):
    print([a] + l + [b])


my_add([5, 75, 4, 9], int(input("my_add - enter a number: ")), int(input("my_add - enter a number: ")))

# Make a function to sort a list, no list.sort()

def my_sort(l):
    for i in range(len(my_sort)-1):
        for j in range(len(my_sort)-1-i):
            if my_sort[i] > my_sort[i+1]:
                l[j], l[j+1] = l[j+1], l[j]
        return[l]

my_sort([5, 75, 4, 9])

# Make a function to remove duplicate element in a list, no builtin function

def remove_duplicate(l):
    result = []

    for i in l:
        if i not in result:
            result.append(i)
            
    return result

remove_duplicate([5, 'hello', 47, '5', 'hello', 5, 74, 'hi'])
