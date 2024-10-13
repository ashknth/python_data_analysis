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


def main():
    # Create a student (model)
    student = Student("John Doe", 3)

    # Create the view
    view = StudentView()

    # Create the controller with the model and view
    controller = StudentController(student, view)

    # Display initial student details
    controller.show_student()

    # Set scores for the student
    controller.set_student_score(1, 85)
    controller.set_student_score(2, 92)
    controller.set_student_score(3, 78)

    # Display updated student details
    controller.show_student()

    # Update student name
    controller.update_student_name("Jane Doe")

    # Display the updated student name and details
    controller.show_student()


if __name__ == "__main__":
    main()
