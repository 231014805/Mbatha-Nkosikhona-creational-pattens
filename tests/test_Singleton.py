import unittest
from Singleton import Singleton


class TestSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        """Test that only one instance of the Singleton class is created."""
        obj1 = Singleton("First Instance")
        obj2 = Singleton("Second Instance")
        self.assertIs(obj1, obj2, "Singleton instances should be the same.")
        self.assertEqual(obj1.get_value(), "First Instance")
        self.assertEqual(obj2.get_value(), "First Instance")

    def test_singleton_attribute_preservation(self):
        """Test that attributes are preserved across instances."""
        obj1 = Singleton("First Instance")
        obj2 = Singleton("New Value")
        self.assertEqual(obj1.get_value(), "First Instance")
        self.assertEqual(obj2.get_value(), "First Instance")


if __name__ == "__main__":
    unittest.main()

