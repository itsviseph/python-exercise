# zip
categories = ["rent", "food", "transport"]
budgets = [1500, 500, 300]

budget_map = dict(zip(categories, budgets))
print(budget_map)


# List Comprehension
transactions = [
    {"amount": 1200, "category": "rent"},
    {"amount": 300, "category": "food"},
    {"amount": 150, "category": "transport"},
    {"amount": 80, "category": "subscriptions"},
    {"amount": 220, "category": "food"},
    {"amount": 60, "category": "subscriptions"},
]

amounts_over_200 = [t["amount"] for t in transactions if t["amount"] > 200]
print(amounts_over_200)

# Dictionary Comprehension (sum by category)
category_totals = {
    category: sum(t["amount"] for t in transactions if t["category"] == category)
    for category in {t["category"] for t in transactions}
}

print(category_totals)


# Decorator
def safe_run(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            print("Something went wrong")

    return wrapper


@safe_run
def divide(a, b):
    return a / b


divide(10, 0)


# Generator
def large_expenses(limit):
    for t in transactions:
        if t["amount"] > limit:
            yield t


for expense in large_expenses(200):
    print(expense)
