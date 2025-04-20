class Student:
    """
    Represents a student in the counseling appointment booking system.

    Attributes:
        student_id (str): The unique identifier for the student.
        name (str): The full name of the student.
        email (str): The email address of the student.
        phone (str): The phone number of the student.
        status (str): The current status of the student (e.g., 'active', 'inactive').
    """

    def __init__(self, student_id: str, name: str, email: str, phone: str, status: str = "active"):
        """
        Initializes a new Student instance.

        Args:
            student_id (str): Unique identifier for the student.
            name (str): Full name of the student.
            email (str): Email address of the student.
            phone (str): Phone number of the student.
            status (str): Current status of the student (default is 'active').
        """
        self.__student_id = student_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__status = status

    # Getters
    def get_student_id(self) -> str:
        """Returns the student's ID."""
        return self.__student_id

    def get_name(self) -> str:
        """Returns the student's name."""
        return self.__name

    def get_email(self) -> str:
        """Returns the student's email."""
        return self.__email

    def get_phone(self) -> str:
        """Returns the student's phone number."""
        return self.__phone

    def get_status(self) -> str:
        """Returns the student's status."""
        return self.__status

    # Setters
    def set_name(self, name: str):
        """Sets the student's name."""
        self.__name = name

    def set_email(self, email: str):
        """Sets the student's email."""
        self.__email = email

    def set_phone(self, phone: str):
        """Sets the student's phone number."""
        self.__phone = phone

    def set_status(self, status: str):
        """Sets the student's status."""
        self.__status = status

    # Methods
    def register(self):
        """Simulates student registration."""
        print(f"Student {self.__name} with ID {self.__student_id} has registered.")

    def login(self):
        """Simulates student login."""
        print(f"Student {self.__name} with email {self.__email} has logged in.")

    def book_appointment(self):
        """Simulates booking an appointment."""
        print(f"Student {self.__name} is booking an appointment.")

    def cancel_appointment(self):
        """Simulates canceling an appointment."""
        print(f"Student {self.__name} has canceled an appointment.")

    def submit_feedback(self, feedback: str):
        """
        Simulates submitting feedback.

        Args:
            feedback (str): The feedback provided by the student.
        """
        print(f"Student {self.__name} submitted feedback: '{feedback}'.")

# Example Usage
if __name__ == "__main__":
    # Create a student instance
    student = Student("S12345", "Jane Doe", "jane.doe@example.com", "555-1234")

    # Use methods
    student.register()
    student.login()
    student.book_appointment()
    student.submit_feedback("Great session!")

