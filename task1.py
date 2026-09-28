# 1.1
def f1():
    return 42

def f2(x):
    return 2 * x

print(f1(), f2(5) + f1())
# prediction: answer -> 42, 52
print("-" * 60)

# 1.2
def bread():
    print("<//////////>")

def lettuce():
    print("~~~~~~~~~~~~")

def tomato():
    print("O O O O O O")

def ham():
    print("============")

bread()
lettuce()
tomato()
ham()
ham()
bread()
print("-" * 60)

# 1.3
def sandwich_count(a):
    if not isinstance(a, int):
        print("I can't do this!")
    else:
        for i in range(a):
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()
            print()

sandwich_count(3)
print("-" * 60)

# 1.4
def sandwich_count(a, veg=False):
    if not isinstance(a, int):
        print("I can't do this!")
    else:
        for i in range(a):
            bread()
            if veg:
                lettuce()
                lettuce()
                tomato()
                tomato()
            else:
                lettuce()
                tomato()
                ham()
                ham()

            bread()
            print()

sandwich_count(2, True)
print("-" * 60)