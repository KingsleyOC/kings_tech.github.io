# Define the OnlineCodingClass class
class OnlineCodingClass:
    def __init__(self, course_name, instructor, start_date, end_date):
        """
        Initialize an instance of the OnlineCodingClass.

        Parameters:
            course_name (str): The name of the coding class.
            instructor (str): The name of the instructor.
            start_date (str): The start date of the class.
            end_date (str): The end date of the class.
        """
        # Initialize attributes
        self.course_name = course_name
        self.instructor = instructor
        self.start_date = start_date
        self.end_date = end_date
        self.students = []

    def add_student(self, student_name):
        """
        Add a student to the class.

        Parameters:
            student_name (str): The name of the student.
        """
        # Append student to the list
        self.students.append(student_name)
        print(f"{student_name} has been enrolled in {self.course_name}.")

    def display_course_info(self):
        """
        Display information about the coding class.
        """
        # Print course information
        print(f"Course Name: {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print("Enrolled Students:")
        for student in self.students:
            print(f"- {student}")

# Example Usage
# Create an instance of OnlineCodingClass
coding_class = OnlineCodingClass("Introduction to Python Programming", "John Doe", "2024-06-01", "2024-08-01")

# Add students to the class
coding_class.add_student("Alice")
coding_class.add_student("Bob")

# Display course information
coding_class.display_course_info()
