# Exercise: Pub Entry Checker (Input Version)
# Check if a user is allowed to enter a pub based on age


def check_pub_entry():
    age_input = input("Please enter your age: ")

    if not age_input.isdigit():
        print("Invalid input. Please enter a number.")
        return

    age = int(age_input)

    if age < 18:
        print("Entry denied. You must be 18 or older.")
    elif age == 18:
        print("Welcome! First legal year—drink responsibly.")
    else:
        print("Entry granted. Enjoy your time at the pub!")


check_pub_entry()
