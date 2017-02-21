import unittest

import network
import algorithms

class AlgorithmsTestCase(unittest.TestCase):

    def setUp(self):
        self.network = network.Network()
        self.network.add_connection("A", "B", 5)
        self.network.add_connection("B", "C", 4)
        self.network.add_connection("C", "D", 8)
        self.network.add_connection("D", "C", 8)
        self.network.add_connection("D", "E", 6)
        self.network.add_connection("A", "D", 5)
        self.network.add_connection("C", "E", 2)
        self.network.add_connection("E", "B", 3)
        self.network.add_connection("A", "E", 7)

    def test_distance_abc(self):
        got = algorithms.get_distance(self.network, ["A", "B", "C"])
        self.assertEqual(got, 9)

    def test_distance_aebcd(self):
        got = algorithms.get_distance(self.network, ["A", "E", "B", "C", "D"])
        self.assertEqual(got, 22)

    def test_distance_aed_not_found(self):
        self.assertRaises(algorithms.RouteNotFound, algorithms.get_distance, self.network, ["A", "E", "D"])

    def test_count_max_stops(self):
        count = algorithms.count_max_stops(self.network, "C", "C", 3)
        self.assertEqual(count, 2)

    def test_count_exact_stops(self):
        count = algorithms.count_exact_stops(self.network, "A", "C", 4)
        self.assertEqual(count, 3)

    def test_count_distance(self):
        count = algorithms.count_max_distance(self.network, "C", "C", 30)
        self.assertEqual(count, 7)

    def test_shortest_distance(self):
        distance = algorithms.get_shortest_distance(self.network, "A", "C")
        self.assertEqual(distance, 9)

    def test_shortest_distance_no_route(self):
        self.assertRaises(algorithms.RouteNotFound, algorithms.get_shortest_distance, self.network, "D", "A")
