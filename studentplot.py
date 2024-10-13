import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class Student:
    """Represents a student with a name and a list of test scores."""
    
    def __init__(self, name: str, num_tests: int):
        """Initializes the student with a name and a given number of test scores."""
        self.name = name
        self.scores = [0] * num_tests  # Initialize test scores to 0

    def get_name(self):
        """Returns the student's name."""
        return self.name

    def set_score(self, test_number: int, score: int):
        """Sets the score for a given test (1-based index)."""
        if 1 <= test_number <= len(self.scores):
            self.scores[test_number - 1] = score

    def get_average_score(self):
        """Calculates and returns the average score."""
        return sum(self.scores) / len(self.scores)

    def get_highest_score(self):
        """Returns the highest test score."""
        return max(self.scores)

    def get_scores(self):
        """Returns a list of all test scores."""
        return self.scores

    def __str__(self):
        """Returns a string representation of the student's details."""
        return f"Student({self.name}, {self.scores})"


class StudentView:
    """Represents the view in a model-view-controller design. Responsible for displaying student data."""
    
    def display_student_details(self, student):
        """Displays the student's details."""
        print(f"Student Name: {student.get_name()}")
        for i, score in enumerate(student.scores, start=1):
            print(f"Test {i} Score: {score}")
        print(f"Average Score: {student.get_average_score():.2f}")
        print(f"Highest Score: {student.get_highest_score()}")
        print()

    def display_message(self, message):
        """Displays a generic message."""
        print(message)


class StudentController:
    """Handles the interaction between the Student model and the StudentView."""
    
    def __init__(self, student, view):
        self.student = student  # The Student object (model)
        self.view = view        # The StudentView object (view)

    def set_student_score(self, test_number, score):
        """Sets a student's test score."""
        self.student.set_score(test_number, score)
        self.view.display_message(f"Score for Test {test_number} set to {score}.")

    def show_student(self):
        """Displays the student's details using the view."""
        self.view.display_student_details(self.student)

    def update_student_name(self, new_name):
        """Updates the student's name."""
        self.student.name = new_name
        self.view.display_message(f"Student's name updated to {new_name}.")

    def plot_scores(self):
        """Plots the student's test scores using matplotlib."""
        scores = self.student.get_scores()
        tests = list(range(1, len(scores) + 1))

        plt.figure(figsize=(6, 4))
        plt.plot(tests, scores, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)
        plt.title(f"{self.student.get_name()}'s Test Scores")
        plt.xlabel("Test Number")
        plt.ylabel("Score")
        plt.grid(True)
        plt.show()


class StudentApp:
    """GUI for interacting with the Student model and controller."""

    def __init__(self, root):
        """Initializes the application window."""
        self.root = root
        self.root.title("Student Test Scores")

        self.student = Student("John Doe", 3)  # Example student with 3 test scores
        self.view = StudentView()
        self.controller = StudentController(self.student, self.view)

        # UI elements
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.insert(0, self.student.get_name())
        self.name_entry.pack()

        self.update_name_button = tk.Button(root, text="Update Name", command=self.update_student_name)
        self.update_name_button.pack()

        # Score entry fields
        self.score_entries = []
        for i in range(3):
            score_label = tk.Label(root, text=f"Test {i + 1} Score:")
            score_label.pack()

            score_entry = tk.Entry(root)
            score_entry.pack()
            self.score_entries.append(score_entry)

        self.set_scores_button = tk.Button(root, text="Set Scores", command=self.set_scores)
        self.set_scores_button.pack()

        # Plot scores button
        self.plot_scores_button = tk.Button(root, text="Plot Scores", command=self.plot_scores)
        self.plot_scores_button.pack()

    def update_student_name(self):
        """Updates the student's name from the entry field."""
        new_name = self.name_entry.get()
        self.controller.update_student_name(new_name)

    def set_scores(self):
        """Sets the student's scores based on entry fields."""
        try:
            for i, entry in enumerate(self.score_entries, start=1):
                score = int(entry.get())
                self.controller.set_student_score(i, score)
            messagebox.showinfo("Success", "Scores updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer scores.")

    def plot_scores(self):
        """Calls the controller to plot the student's test scores."""
        self.controller.plot_scores()


def main():
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
