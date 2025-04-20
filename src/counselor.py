class Counselor:
    """
    Represents a counselor in the counseling appointment booking system.

    Attributes:
        counselor_id (str): The unique identifier for the counselor.
        name (str): The full name of the counselor.
        email (str): The email address of the counselor.
        specialization (str): The area of expertise of the counselor.
        availability_status (str): The current availability status of the counselor.
    """

    def __init__(self, counselor_id: str, name: str, email: str, specialization: str, availability_status: str = "available"):
        """
        Initializes a new Counselor instance.

        Args:
            counselor_id (str): Unique identifier for the counselor.
            name (str): Full name of the counselor.
            email (str): Email address of the counselor.
            specialization (str): Area of expertise of the counselor.
            availability_status (str): Current availability status (default is 'available').
        """
        self.__counselor_id = counselor_id
        self.__name = name
        self.__email = email
        self.__specialization = specialization
        self.__availability_status = availability_status

    # Getters
    def get_counselor_id(self) -> str:
        """Returns the counselor's ID."""
        return self.__counselor_id

    def get_name(self) -> str:
        """Returns the counselor's name."""
        return self.__name

    def get_email(self) -> str:
        """Returns the counselor's email."""
        return self.__email

    def get_specialization(self) -> str:
        """Returns the counselor's specialization."""
        return self.__specialization

    def get_availability_status(self) -> str:
        """Returns the counselor's availability status."""
        return self.__availability_status

    # Setters
    def set_name(self, name: str):
        """Sets the counselor's name."""
        self.__name = name

    def set_email(self, email: str):
        """Sets the counselor's email."""
        self.__email = email

    def set_specialization(self, specialization: str):
        """Sets the counselor's specialization."""
        self.__specialization = specialization

    def set_availability_status(self, status: str):
        """Sets the counselor's availability status."""
        self.__availability_status = status

    # Methods
    def login(self):
        """Simulates counselor login."""
        print(f"Counselor {self.__name} with email {self.__email} has logged in.")

    def approve_appointment(self, appointment_id: str):
        """
        Simulates approving an appointment.

        Args:
            appointment_id (str): The ID of the appointment to approve.
        """
        print(f"Counselor {self.__name} approved appointment ID {appointment_id}.")

    def conduct_session(self, appointment_id: str):
        """
        Simulates conducting a session.

        Args:
            appointment_id (str): The ID of the appointment being conducted.
        """
        print(f"Counselor {self.__name} is conducting session for appointment ID {appointment_id}.")

    def update_availability(self, status: str):
        """
        Updates the counselor's availability status.

        Args:
            status (str): The new availability status.
        """
        self.__availability_status = status
        print(f"Counselor {self.__name}'s availability updated to: {status}.")

# Example Usage
if __name__ == "__main__":
    # Create a counselor instance
    counselor = Counselor("C98765", "Dr. John Smith", "john.smith@example.com", "Stress Management")

    # Use methods
    counselor.login()
    counselor.approve_appointment("A12345")
    counselor.conduct_session("A12345")
    counselor.update_availability("unavailable")

