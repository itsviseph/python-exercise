transactions = [
    {"amount": 1200, "category": "rent"},
    {"amount": 300, "category": "food"},
    {"amount": 150, "category": "transport"},
    {"amount": 80, "category": "subscriptions"},
    {"amount": 220, "category": "food"},
    {"amount": 60, "category": "subscriptions"},
]

# filter()

filtered_transactions = filter(
    lambda transaction: transaction["amount"] > 100, transactions
)

filtered_transaction = list(filtered_transactions)

print(filtered_transaction)


# map()

amounts = map(lambda transaction: transaction["amount"], transactions)
amount = list(amounts)
print(amount)


# reduce()

from functools import reduce

total = reduce(lambda acc, transaction: acc + transaction["amount"], transactions, 0)

print(total)


# trying with a for loop insted of reduce


def totals(transactions):
    tots = 0
    for transaction in transactions:
        tots += transaction["amount"]
    return tots


print(totals(transactions))
