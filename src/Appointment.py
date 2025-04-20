class Appointment:
    """
    Represents an appointment in the counseling appointment booking system.

    Attributes:
        appointment_id (str): The unique identifier for the appointment.
        date (str): The date of the appointment.
        time (str): The time of the appointment.
        status (str): The current status of the appointment (e.g., 'scheduled', 'canceled', 'completed').
        student_id (str): The ID of the student who booked the appointment.
        counselor_id (str): The ID of the counselor for the appointment.
    """

    def __init__(self, appointment_id: str, date: str, time: str, student_id: str, counselor_id: str, status: str = "scheduled"):
        """
        Initializes a new Appointment instance.

        Args:
            appointment_id (str): Unique identifier for the appointment.
            date (str): Date of the appointment.
            time (str): Time of the appointment.
            student_id (str): ID of the student who booked the appointment.
            counselor_id (str): ID of the counselor for the appointment.
            status (str): Current status of the appointment (default is 'scheduled').
        """
        self.__appointment_id = appointment_id
        self.__date = date
        self.__time = time
        self.__student_id = student_id
        self.__counselor_id = counselor_id
        self.__status = status

    # Getters
    def get_appointment_id(self) -> str:
        """Returns the appointment's ID."""
        return self.__appointment_id

    def get_date(self) -> str:
        """Returns the appointment's date."""
        return self.__date

    def get_time(self) -> str:
        """Returns the appointment's time."""
        return self.__time

    def get_status(self) -> str:
        """Returns the appointment's status."""
        return self.__status

    def get_student_id(self) -> str:
        """Returns the ID of the student who booked the appointment."""
        return self.__student_id

    def get_counselor_id(self) -> str:
        """Returns the ID of the counselor for the appointment."""
        return self.__counselor_id

    # Setters
    def set_date(self, date: str):
        """Sets the appointment's date."""
        self.__date = date

    def set_time(self, time: str):
        """Sets the appointment's time."""
        self.__time = time

    def set_status(self, status: str):
        """Sets the appointment's status."""
        self.__status = status

    # Methods
    def schedule(self):
        """Schedules the appointment."""
        self.__status = "scheduled"
        print(f"Appointment {self.__appointment_id} is scheduled for {self.__date} at {self.__time}.")

    def cancel(self):
        """Cancels the appointment."""
        self.__status = "canceled"
        print(f"Appointment {self.__appointment_id} has been canceled.")

    def reschedule(self, new_date: str, new_time: str):
        """
        Reschedules the appointment.

        Args:
            new_date (str): The new date for the appointment.
            new_time (str): The new time for the appointment.
        """
        self.__date = new_date
        self.__time = new_time
        self.__status = "rescheduled"
        print(f"Appointment {self.__appointment_id} has been rescheduled to {self.__date} at {self.__time}.")

    def notify_participants(self):
        """Notifies the student and counselor about the appointment details."""
        print(f"Notification: Appointment {self.__appointment_id} on {self.__date} at {self.__time} is {self.__status}.")

# Example Usage
if __name__ == "__main__":
    # Create an appointment instance
    appointment = Appointment("A12345", "2025-04-22", "10:00 AM", "S12345", "C98765")

    # Use methods
    appointment.schedule()
    appointment.notify_participants()
    appointment.reschedule("2025-04-25", "2:00 PM")
    appointment.cancel()

