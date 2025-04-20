class Notification:
    """
    Base class for notifications.
    """

    def __init__(self, recipient: str, message: str):
        self.recipient = recipient
        self.message = message

    def send(self):
        """Send the notification."""
        raise NotImplementedError("Subclasses must implement the send method.")


class StudentNotification(Notification):
    """
    Notification for students.
    """

    def send(self):
        print(f"Sending Student Notification to {self.recipient}: {self.message}")


class CounselorNotification(Notification):
    """
    Notification for counselors.
    """

    def send(self):
        print(f"Sending Counselor Notification to {self.recipient}: {self.message}")


class NotificationFactory:
    """
    Simple factory to create notifications based on user type.
    """

    @staticmethod
    def create_notification(user_type: str, recipient: str, message: str) -> Notification:
        """
        Creates a notification based on the user type.

        Args:
            user_type (str): The type of user ('student' or 'counselor').
            recipient (str): The recipient of the notification.
            message (str): The notification message.

        Returns:
            Notification: An instance of the appropriate notification class.

        Raises:
            ValueError: If the user type is not recognized.
        """
        if user_type.lower() == "student":
            return StudentNotification(recipient, message)
        elif user_type.lower() == "counselor":
            return CounselorNotification(recipient, message)
        else:
            raise ValueError(f"Invalid user type: {user_type}")


# Client Code
if __name__ == "__main__":
    # Create and send a student notification
    student_notification = NotificationFactory.create_notification(
        "student", "student@example.com", "Your appointment is confirmed."
    )
    student_notification.send()

    # Create and send a counselor notification
    counselor_notification = NotificationFactory.create_notification(
        "counselor", "counselor@example.com", "A new appointment has been booked."
    )
    counselor_notification.send()

