import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Teo", {"Python": []})

    def test_init(self):
        self.assertEqual(self.student.name, "Teo")
        self.assertEqual(self.student.courses, {"Python": []})

    def test_init_none_dict(self):
        student = Student("Teo")
        self.assertEqual(student.name, "Teo")
        self.assertEqual(student.courses, {})

    def test_enroll_add_notes_course_exists(self):
        self.assertEqual(self.student.enroll("Python", ["note"]), "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses, {"Python": ['note']})

    def test_enroll_add_notes_course_not_exists_add_y(self):
        student = Student("Teo")
        self.assertEqual(student.enroll("Python", ['note'], 'Y'), "Course and course notes have been added.")
        self.assertEqual(student.courses, {"Python": ['note']})

    def test_enroll_add_notes_course_not_exists_add_y2(self):
        student = Student("Teo")
        self.assertEqual(student.enroll("Python", ['note'], ""), "Course and course notes have been added.")
        self.assertEqual(student.courses, {"Python": ['note']})

    def test_enroll_add_notes_course_not_exists_add_y3(self):
        student = Student("Teo")
        self.assertEqual(student.enroll("Python", ['note']), "Course and course notes have been added.")
        self.assertEqual(student.courses, {"Python": ['note']})

    def test_enroll_add_notes_course_not_exists_add_n(self):
        student = Student("Teo")
        self.assertEqual(student.enroll("Python", ['note'], 'n'), "Course has been added.")
        self.assertEqual(student.courses, {"Python": []})

    def test_add_notes(self):
        self.assertEqual(self.student.add_notes("Python", "note"), "Notes have been updated")
        self.assertEqual(self.student.courses["Python"], ['note'])

    def test_add_notes_course_not_exists(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes("Java", "note")
        self.assertEqual(str(error.exception), "Cannot add notes. Course not found.")

    def test_leave_course(self):
        self.assertEqual(self.student.leave_course("Python"), "Course has been removed"),
        self.assertEqual(self.student.courses, {})

    def test_leave_course_not_exists(self):
        with self.assertRaises(Exception) as error:
            self.student.leave_course("Java")
        self.assertEqual(str(error.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Compete/Index/1949#3
