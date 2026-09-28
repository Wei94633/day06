# 1.1

def analyze_grades(grades):
    print(max(grades))
    print(min(grades))
    print(sum(grades)/len(grades))

analyze_grades([90, 85, 100])

# 1.2
def reverse_string(text):
    if text == "":
        return ""
    else:
        return reverse_string(text[1:]) + text[0]


print(reverse_string("Epitech"))

# 1.3
def make_custom_sandwich(ingredients):
    has_ham_or_tomato = any(
        item == "ham" or item == "tomato"
        for item in ingredients
    )

    bread_count = ingredients.count("bread")

    if not has_ham_or_tomato:
        print("Error: A sandwich needs ham or tomato!")
        return

    if bread_count < 2:
        print("Error: A sandwich needs top and bottom bread!")
        return

    for item in ingredients:
        print(item)


ingredients = ["bread", "lettuce", "tomato", "ham", "bread"]
make_custom_sandwich(ingredients)