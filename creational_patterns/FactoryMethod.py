from abc import ABC, abstractmethod

# Abstract Product
class Notification(ABC):
    """
    Abstract base class for notifications.
    """

    @abstractmethod
    def send(self, recipient: str, message: str):
        pass


# Concrete Product: Student Notification
class StudentNotification(Notification):
    def send(self, recipient: str, message: str):
        print(f"Sending Student Notification to {recipient}: {message}")


# Concrete Product: Counselor Notification
class CounselorNotification(Notification):
    def send(self, recipient: str, message: str):
        print(f"Sending Counselor Notification to {recipient}: {message}")


# Abstract Creator
class NotificationFactory(ABC):
    """
    Abstract Factory that declares the factory method.
    """

    @abstractmethod
    def create_notification(self) -> Notification:
        pass


# Concrete Creator: Student Notification Factory
class StudentNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return StudentNotification()


# Concrete Creator: Counselor Notification Factory
class CounselorNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return CounselorNotification()


# Client Code
def send_notification(factory: NotificationFactory, recipient: str, message: str):
    """
    Sends a notification using the factory method.
    """
    notification = factory.create_notification()
    notification.send(recipient, message)


if __name__ == "__main__":
    # Send a notification to a student
    print("Sending a notification to a student:")
    student_factory = StudentNotificationFactory()
    send_notification(student_factory, "student@example.com", "Your appointment is confirmed.")

    print("\nSending a notification to a counselor:")
    # Send a notification to a counselor
    counselor_factory = CounselorNotificationFactory()
    send_notification(counselor_factory, "counselor@example.com", "A new appointment has been booked.")

