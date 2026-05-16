"""
Test module for student management system.
"""

import unittest
import json
import os
from student_management import Student, StudentManagement


class TestStudent(unittest.TestCase):
    """Test cases for Student class."""

    def test_student_creation(self):
        """Test that a student can be created with valid data."""
        student = Student("John Doe", "john@example.com", "123456789")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.email, "john@example.com")
        self.assertEqual(student.phone, "123456789")

    def test_student_to_dict(self):
        """Test that student can be converted to dictionary."""
        student = Student("Jane Doe", "jane@example.com", "987654321")
        student_dict = student.to_dict()
        self.assertIsInstance(student_dict, dict)
        self.assertEqual(student_dict["name"], "Jane Doe")
        self.assertEqual(student_dict["email"], "jane@example.com")
        self.assertEqual(student_dict["phone"], "987654321")


class TestStudentManagement(unittest.TestCase):
    """Test cases for StudentManagement class."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_file = "test_students.json"
        self.management = StudentManagement(self.test_file)

    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_student(self):
        """Test that a student can be added."""
        student = Student("Alice Smith", "alice@example.com", "111222333")
        self.management.add_student(student)
        self.assertEqual(len(self.management.students), 1)

    def test_find_student_by_name(self):
        """Test that a student can be found by name."""
        student = Student("Bob Jones", "bob@example.com", "444555666")
        self.management.add_student(student)
        found = self.management.find_student("Bob Jones")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Bob Jones")


if __name__ == "__main__":
    unittest.main()