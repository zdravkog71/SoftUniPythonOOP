from project.student import Student
from unittest import TestCase, main

class TestStudent(TestCase):
    def setUp(self):
        self.st = Student("Kuku")

    def test_student_init_without_course(self):
        self.assertEqual("Kuku", self.st.name)
        self.assertEqual({},self.st.courses)

    def test_enroll_student_existing_sourse(self):
        self.st.courses["Python"] = ["note1", "note2"]
        res = self.st.enroll("Python", ["note3"], "")
        self.assertEqual("Course already added. Notes have been updated.",res)

    def test_enroll_student_existing_sourse_notes(self):
        self.st.courses["Python"] = ["note1", "note2"]
        res = self.st.enroll("Python", ["note3"], "")
        self.assertEqual(["note1","note2","note3"],self.st.courses["Python"])

    def test_enroll_student_add_notes_yes(self):
        self.st.enroll("Python",["note1","note2"],"Y")
        self.assertEqual(["note1","note2"],self.st.courses["Python"])

    def test_enroll_student_add_notes_empty(self):
        self.st.enroll("Python",["note1","note2"],"")
        self.assertEqual(["note1","note2"],self.st.courses["Python"])

    def test_enroll_student_add_notes(self):
        res = self.st.enroll("Python",["note1","note2"],"")
        self.assertEqual("Course and course notes have been added.",res)

    def test_enroll_student_no_notes_to_add_return_msg(self):
        res = self.st.enroll("Python",["note1","note2"],"Z")
        self.assertEqual("Course has been added.",res)

    def test_enroll_student_no_notes_to_add(self):
        self.st.enroll("Python",["note1","note2"],"Z")
        self.assertEqual([],self.st.courses["Python"])

    def test_add_notes_existing_course_return_msg(self):
        self.st.courses["Python"] = []
        res = self.st.add_notes("Python","note1")
        self.assertEqual("Notes have been updated",res)

    def test_add_notes_existing_course(self):
        self.st.courses["Python"] = []
        self.st.add_notes("Python","note1")
        self.assertEqual(["note1"],self.st.courses["Python"])

    def test_add_notes_raises(self):
        with self.assertRaises(Exception) as ex:
            self.st.add_notes("Python","note1")
        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))

    def test_leave_course(self):
        self.st.courses["Python"] = []
        res = self.st.leave_course("Python")
        self.assertEqual("Course has been removed",res)

    def test_leave_course_raises(self):
        self.st.courses["Python"] = []
        with self.assertRaises(Exception) as ex:
            self.st.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.",str(ex.exception))


if __name__ == "__main__":
    main()