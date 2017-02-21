import sys

import algorithms
import network
import parser


def _distance_report(rails, paths):
    output = ""
    for path in paths:
        try:
            distance = algorithms.get_distance(rails, path)
        except algorithms.RouteNotFound:
            output += "NO SUCH ROUTE\n"
        else:
            output += "{}\n".format(distance)
    return output


def _shortest_distance_report(rails, paths):
    output = ""
    for first, last in paths:
        try:
            distance = algorithms.get_shortest_distance(rails, first, last)
        except algorithms.RouteNotFound:
            output += "NO SUCH ROUTE\n"
        else:
            output += "{}\n".format(distance)
    return output


def report(raw_data):
    rails = network.Network()
    for connection in parser.parse(raw_data):
        rails.add_connection(*connection)
    
    output = ""

    paths = [
        ["A", "B", "C"],
        ["A", "D"],
        ["A", "D", "C"],
        ["A", "E", "B", "C", "D"],
        ["A", "E", "D"],
    ]
    output += _distance_report(rails, paths)

    output += "{}\n".format(algorithms.count_max_stops(rails, "C", "C", 3))

    output += "{}\n".format(algorithms.count_exact_stops(rails, "A", "C", 4))

    paths = [
        ("A", "C"),
        ("B", "B"),
    ]
    output += _shortest_distance_report(rails, paths)

    output += "{}\n".format(algorithms.count_max_distance(rails, "C", "C", 30))

    return output


def main():
    for line in sys.stdin.readlines():
        print(report(line))


if __name__ == "__main__":
    main()
