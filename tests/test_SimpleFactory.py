import unittest
from SimpleFactory import NotificationFactory, StudentNotification, CounselorNotification


class TestSimpleFactory(unittest.TestCase):
    def test_create_student_notification(self):
        """Test that a student notification is created successfully."""
        notification = NotificationFactory.create_notification(
            "student", "student@example.com", "Your appointment is confirmed."
        )
        self.assertIsInstance(notification, StudentNotification)
        self.assertEqual(notification.recipient, "student@example.com")
        self.assertEqual(notification.message, "Your appointment is confirmed.")

    def test_create_counselor_notification(self):
        """Test that a counselor notification is created successfully."""
        notification = NotificationFactory.create_notification(
            "counselor", "counselor@example.com", "A new appointment has been booked."
        )
        self.assertIsInstance(notification, CounselorNotification)
        self.assertEqual(notification.recipient, "counselor@example.com")
        self.assertEqual(notification.message, "A new appointment has been booked.")

    def test_invalid_user_type(self):
        """Test that an invalid user type raises a ValueError."""
        with self.assertRaises(ValueError):
            NotificationFactory.create_notification("admin", "admin@example.com", "Invalid user type.")


if __name__ == "__main__":
    unittest.main()

