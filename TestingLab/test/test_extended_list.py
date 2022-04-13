from TestingLab.extended_list import IntegerList

#from unittest import TestCase, main

import unittest
class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.list_integers = IntegerList(5, 6, 7)

    def test_init(self):
        self.assertEqual([5,6,7],self.list_integers._IntegerList__data)

    def test_add_element_into_list(self):
        result = self.list_integers.add(10)
        self.assertEqual([5,6,7,10],result)

    def test_if_new_element_is_int_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integers.add(10.2)
        self.assertEqual("Element is not Integer",str(ex.exception))

    def test_all_elements_should_be_integers(self):
        list_integer = IntegerList(5.2, "6", 7.3)
        self.assertEqual([], list_integer._IntegerList__data)

    def test_remove_element_from_index(self):
        result = self.list_integers.remove_index(0)
        self.assertEqual(5,result)

    def test_remove_element_wrong_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.remove_index(100)
        self.assertEqual("Index is out of range",str(ex.exception))

    def test_get_element_at_index(self):
        result = self.list_integers.get(0)
        self.assertEqual(5,result)
        self.assertEqual([5,6,7],self.list_integers._IntegerList__data)

    def test_get_element_out_of_range_rases(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.get(100)
        self.assertEqual("Index is out of range",str(ex.exception))

    def test_insert_element(self):
        self.list_integers.insert(0,100)
        self.assertEqual([100,5,6,7], self.list_integers._IntegerList__data)

    def test_insert_if_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integers.insert(0,10.5)
        self.assertEqual("Element is not Integer",str(ex.exception))

    def test_insert_element_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integers.insert(100,2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_biggest(self):
        result = self.list_integers.get_biggest()
        self.assertEqual(7,result)

    def test_get_index_of_element(self):
        result = self.list_integers.get_index(5)
        self.assertEqual(0,result)


if __name__ == "__main__":
    unittest.main()