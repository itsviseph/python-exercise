from functools import reduce

transactions = [
    {"amount": 1200, "category": "rent"},
    {"amount": 300, "category": "food"},
    {"amount": 150, "category": "transport"},
    {"amount": 80, "category": "subscriptions"},
    {"amount": 220, "category": "food"},
    {"amount": 60, "category": "subscriptions"},
]

# 1️⃣ filter — expenses over 100
filtered_transactions = list(filter(lambda t: t["amount"] > 100, transactions))

# 2️⃣ map — extract amounts
amounts = list(map(lambda t: t["amount"], transactions))

# 3️⃣ reduce — total expense
total = reduce(lambda acc, t: acc + t["amount"], transactions, 0)

print(filtered_transactions)
print(amounts)
print(total)


# 4️⃣ loop version (baseline comparison)
def total_with_loop(transactions):
    total = 0
    for t in transactions:
        total += t["amount"]
    return total


print(total_with_loop(transactions))
