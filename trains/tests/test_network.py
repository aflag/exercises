import unittest

from network import Network, Route

class RouteTestCase(unittest.TestCase):

    def test_last_property_route_one_item(self):
        route = Route(["A"], 5)
        self.assertEqual(route.last, "A")

    def test_last_property_two_items(self):
        route = Route(["A", "B"], 5)
        self.assertEqual(route.last, "B")

    def test_first_property(self):
        route = Route(["A", "B"], 5)
        self.assertEqual(route.first, "A")

    def test_connections(self):
        route = Route(["A", "B", "C"], 7)
        self.assertEqual(route.connections, [("A", "B"), ("B", "C")])

    def test_no_path(self):
        self.assertRaises(AssertionError, Route, [], 7)

    def test_add_new_node(self):
        route1 = Route(["A", "B"], 1)
        route2 = route1.add("C", 3)
        self.assertEqual(route2.path, ["A", "B", "C"])
        self.assertEqual(route2.distance, 4)
        self.assertEqual(route1.path, ["A", "B"])
        self.assertEqual(route1.distance, 1)


class NetworkTestCase(unittest.TestCase):

    def test_add_connection(self):
        network = Network()
        network.add_connection("A", "B", 5)
        self.assertEqual(network.nodes["A"], {"B": 5})

    def test_zero_distance_connection(self):
        network = Network()
        self.assertRaises(AssertionError, network.add_connection, "A", "B", 0)

    def test_update_route(self):
        network = Network()
        network.add_connection("A", "B", 5)
        network.add_connection("A", "B", 7)
        self.assertEqual(network.nodes["A"], {"B": 7})

    def test_bfs_in_order(self):
        network = Network()
        network.add_connection("A", "B", 5)
        network.add_connection("A", "E", 1)
        network.add_connection("A", "F", 1)
        network.add_connection("F", "G", 1)
        network.add_connection("B", "C", 2)
        network.add_connection("B", "D", 1)
        network.add_connection("C", "D", 1)
        got = list(network.breadth_first_search("A"))
        expected = [
            Route(["A", "B"], 5),
            Route(["A", "E"], 1),
            Route(["A", "F"], 1),
            Route(["A", "B", "C"], 7),
            Route(["A", "B", "D"], 6),
            Route(["A", "F", "G"], 2),
            Route(["A", "B", "C", "D"], 8),
        ]
        self.assertEqual(got, expected)

    def test_bfs_big_loop_max_3_stops(self):
        network = Network()
        network.add_connection("A", "B", 5)
        network.add_connection("B", "C", 2)
        network.add_connection("C", "A", 4)
        def expand(route, _):
            return route.stops < 3
        got = list(network.breadth_first_search("A", expand=expand))
        expected = [
            Route(["A", "B"], 5),
            Route(["A", "B", "C"], 7),
            Route(["A", "B", "C", "A"], 11),
        ]
        self.assertEqual(got, expected)

    def test_bfs_small_loop_max_3_stops(self):
        network = Network()
        network.add_connection("A", "B", 5)
        network.add_connection("B", "C", 2)
        network.add_connection("C", "B", 4)
        network.add_connection("C", "D", 7)
        def expand(route, _):
            return route.stops < 3
        got = list(network.breadth_first_search("A", expand=expand))
        expected = [
            Route(["A", "B"], 5),
            Route(["A", "B", "C"], 7),
            Route(["A", "B", "C", "B"], 11),
            Route(["A", "B", "C", "D"], 14),
        ]
        self.assertEqual(got, expected)
