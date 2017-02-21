import unittest

import reports


class ReportsTestCase(unittest.TestCase):

    def test_report(self):
        output = reports.report("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
        expected = """9
5
13
22
NO SUCH ROUTE
2
3
9
9
7
"""
        self.assertEqual(output, expected)
