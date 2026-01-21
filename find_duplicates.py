# Exercise: Find Duplicates
# Check for duplicates in the list.
# Print the characters which have duplicates in the list.

my_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "d",
    "m",
    "n",
    "z",  # repeated letters
]

duplicates = []

for value in my_list:
    if my_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
