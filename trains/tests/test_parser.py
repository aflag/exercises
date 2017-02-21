from functools import partial
import unittest

from parser import parse


class ParserTestCase(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(parse("AB5"), [("A", "B", 5)])

    def test_parse_two_edges(self):
        expected = [
            ("A", "B", 5),
            ("B", "C", 3),
        ]
        self.assertEqual(parse("AB5,BC3"), expected)

    def test_no_distance_fails(self):
        self.assertRaises(ValueError, parse, "AB")

    def test_single_node_fails(self):
        self.assertRaises(ValueError, parse, "A5")

    def test_bad_distance(self):
        self.assertRaises(ValueError, parse, "ABC")
