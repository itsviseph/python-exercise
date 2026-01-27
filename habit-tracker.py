# class hobit
class Habit:
    def __init__(self, name):
        self.name = name
        self.completed = False


# class habit tracker
class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def complete_habit(self, habit_name):

        for habit in self.habits:
            if habit.name == habit_name:
                habit.completed = True
                print(f"Habit {habit_name} marked as completed")
                return
        print(f"The habit {habit_name} is not logged")

    def view_habits(self):
        for habit in self.habits:
            status = "✅" if habit.completed else "❌"
            """
            if habit.completed:
                status = '✅'
            else: 
                status = '❌'
            """
            print(f"{habit.name} - {status}")

    def reset_habits(self):
        for habit in self.habits:
            habit.completed = False
        print("Your habits been reset")

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
        print(f"\nProgress: {progress}%")


# CLI menu to enter habits
