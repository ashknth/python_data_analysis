class Student:
    """Represents a student with a name and a list of test scores."""

    def __init__(self, name, number_of_tests):
        """Initializes a new Student object."""
        self.name = name  # Student's name
        self.scores = [0] * number_of_tests  # Initialize test scores to 0

    def get_name(self):
        """Returns the student's name."""
        return self.name

    def set_score(self, test_number, score):
        """Sets the score for a specific test."""
        if 0 < test_number <= len(self.scores):
            self.scores[test_number - 1] = score
        else:
            print("Error: Test number out of range.")

    def get_score(self, test_number):
        """Returns the score for a specific test."""
        if 0 < test_number <= len(self.scores):
            return self.scores[test_number - 1]
        else:
            print("Error: Test number out of range.")
            return None

    def get_average_score(self):
        """Returns the average score of the student."""
        if len(self.scores) > 0:
            return sum(self.scores) / len(self.scores)
        else:
            return 0.0

    def get_highest_score(self):
        """Returns the highest score of the student."""
        if len(self.scores) > 0:
            return max(self.scores)
        else:
            return 0

    def __str__(self):
        """Returns a string representation of the student's information."""
        scores_str = ", ".join(map(str, self.scores))
        return f"Student: {self.name}, Scores: {scores_str}, Average: {self.get_average_score():.2f}"

def main():
    """Main function to test the Student class."""
    
    # Create a new Student object
    student = Student("John Doe", 3)

    # Display initial state of the student
    print("Initial Student Information:")
    print(student)

    # Set the scores for the student
    student.set_score(1, 85)
    student.set_score(2, 92)
    student.set_score(3, 78)

    # Print the student's information after setting the scores
    print("\nAfter setting scores:")
    print(student)

    # Get and print specific test scores
    print("\nGetting specific test scores:")
    print(f"Score for Test 1: {student.get_score(1)}")
    print(f"Score for Test 2: {student.get_score(2)}")
    print(f"Score for Test 3: {student.get_score(3)}")

    # Calculate and print the average score
    average_score = student.get_average_score()
    print(f"\nAverage Score: {average_score:.2f}")

    # Get and print the highest score
    highest_score = student.get_highest_score()
    print(f"Highest Score: {highest_score}")

if __name__ == "__main__":
    main()
