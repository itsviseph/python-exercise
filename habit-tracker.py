# -----------------------------
# Habit class
# -----------------------------
class Habit:
    def __init__(self, name):
        self.name = name
        self.completed = False


# -----------------------------
# HabitTracker class
# -----------------------------
class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def complete_habit(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name:
                habit.completed = True
                print(f"Habit '{habit_name}' marked as completed ✅")
                return
        print(f"Habit '{habit_name}' not found ❌")

    def view_habits(self):
        if not self.habits:
            print("No habits added yet.")
            return

        for habit in self.habits:
            status = "✅" if habit.completed else "❌"
            print(f"{habit.name} - {status}")

    def reset_habits(self):
        for habit in self.habits:
            habit.completed = False
        print("All habits have been reset 🔄")

    def get_progress(self):
        if not self.habits:
            return 0

        completed = 0
        for habit in self.habits:
            if habit.completed:
                completed += 1

        return int((completed / len(self.habits)) * 100)

    def view_progress(self):
        progress = self.get_progress()
        print(f"Progress: {progress}% 📊")


# -----------------------------
# CLI Application
# -----------------------------
tracker = HabitTracker()

while True:
    print("\n=== Habit Tracker ===")
    print("1. Add habit")
    print("2. Complete habit")
    print("3. View habits")
    print("4. View progress")
    print("5. Reset habits")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter habit name: ").strip()
        habit = Habit(name)
        tracker.add_habit(habit)
        print("Habit added ✅")

    elif choice == "2":
        name = input("Enter habit name to complete: ").strip()
        tracker.complete_habit(name)

    elif choice == "3":
        tracker.view_habits()

    elif choice == "4":
        tracker.view_progress()

    elif choice == "5":
        tracker.reset_habits()

    elif choice == "6":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice ❌")
