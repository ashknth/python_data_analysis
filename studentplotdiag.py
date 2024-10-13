import matplotlib.pyplot as plt

def plot_histogram():
    # Courses and number of students data
    courses = ['DSA', 'Programming in C', 'Python Programming']
    num_students = [45, 35, 50]  # Example data for the number of students in each course
    
    # Create a horizontal bar chart (horizontal histogram)
    plt.barh(courses, num_students, color=['blue', 'green', 'orange'])
    
    # Add labels and title
    plt.ylabel('Courses')  # Now the courses will be on the y-axis
    plt.xlabel('Number of Students')  # Number of students will be on the x-axis
    plt.title('Number of Students vs Courses')
    
    # Display the histogram
    plt.show()

if __name__ == "__main__":
    plot_histogram()
