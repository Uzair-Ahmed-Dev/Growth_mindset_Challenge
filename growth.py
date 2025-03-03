class GrowthMindsetTracker:
    def __init__(self):
        self.goals = []
        self.reflections = []

    def set_goal(self, goal):
        self.goals.append(goal)
        print(f"Goal added: {goal}")

    def log_reflection(self, reflection):
        self.reflections.append(reflection)
        print("Reflection logged.")

    def view_goals(self):
        print("\nYour Learning Goals:")
        for idx, goal in enumerate(self.goals, start=1):
            print(f"{idx}. {goal}")

    def view_reflections(self):
        print("\nYour Reflections:")
        for idx, reflection in enumerate(self.reflections, start=1):
            print(f"{idx}. {reflection}")

    def celebrate_effort(self):
        print("\nCelebrating Your Efforts!")
        print("Remember, every step you take is part of your learning journey. Keep going!")

def main():
    tracker = GrowthMindsetTracker()

    while True:
        print("\n--- Growth Mindset Tracker ---")
        print("1. Set a Learning Goal")
        print("2. Log a Reflection")
        print("3. View Goals")
        print("4. View Reflections")
        print("5. Celebrate Effort")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            goal = input("Enter your learning goal: ")
            tracker.set_goal(goal)
        elif choice == '2':
            reflection = input("Enter your reflection: ")
            tracker.log_reflection(reflection)
        elif choice == '3':
            tracker.view_goals()
        elif choice == '4':
            tracker.view_reflections()
        elif choice == '5':
            tracker.celebrate_effort()
        elif choice == '6':
            print("Exiting the Growth Mindset Tracker. Keep growing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
