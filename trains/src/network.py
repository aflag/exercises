import collections


class Route:

    def __init__(self, path, distance):
        assert path, "path cannot be empty"
        self.path = path
        self.distance = distance

    def __eq__(self, other):
        return self.path == other.path and self.distance == other.distance

    def __repr__(self):
        return "{} ({})".format("->".join(self.path), self.distance)

    @property
    def connections(self):
        return list(zip(self.path, self.path[1:]))

    @property
    def first(self):
        return self.path[0]

    @property
    def last(self):
        return self.path[-1]

    @property
    def stops(self):
        return len(self.path) - 1

    def add(self, node, distance):
        return Route(self.path + [node], self.distance + distance)


class Network:

    def __init__(self):
        self.nodes = collections.defaultdict(lambda: {})

    def add_connection(self, a, b, distance):
        assert distance > 0, "distance must be greater than zero"
        self.nodes[a][b] = distance

    def _next_routes(self, current):
        for node, distance in sorted(self.nodes[current.last].items()):
            yield current.add(node, distance)

    def breadth_first_search(self, origin, expand=lambda *_: True):
        routes = list(self._next_routes(Route([origin], 0)))
        while routes:
            route = routes.pop(0)
            yield route
            for next_route in self._next_routes(route):
                if expand(route, next_route.last):
                    routes.append(next_route)
