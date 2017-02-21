class RouteNotFound(Exception):
    pass


def get_distance(network, path):
    stops = len(path) - 1
    def expand(route, _):
        return route.stops < stops
    def valid_route(route):
        return route.path == path

    routes = network.breadth_first_search(path[0], expand=expand)
    routes = list(filter(valid_route, routes))
    if routes:
        return routes[0].distance
    else:
        raise RouteNotFound


def count_max_stops(network, first, last, stops):
    def expand(route, _):
        return route.stops < stops
    def valid_route(route):
        return route.last == last

    routes = network.breadth_first_search(first, expand=expand)
    routes = filter(valid_route, routes)
    return len(list(routes))


def count_exact_stops(network, first, last, stops):
    def expand(route, _):
        return route.stops < stops
    def valid_route(route):
        return route.stops == stops and route.last == last

    routes = network.breadth_first_search(first, expand=expand)
    routes = filter(valid_route, routes)
    return len(list(routes))


def count_max_distance(network, first, last, distance):
    def expand(route, _):
        return route.distance < distance
    def valid_route(route):
        return route.last == last and route.distance < distance

    routes = network.breadth_first_search(first, expand=expand)
    routes = filter(valid_route, routes)
    return len(list(routes))


def get_shortest_distance(network, first, last):
    visited = set()
    def expand(route, next_node):
        return (route.last, next_node) not in visited

    min_distance = None
    routes = network.breadth_first_search(first, expand=expand)
    for route in routes:
        visited = visited.union(route.connections)
        if route.last == last and (min_distance is None or route.distance < min_distance):
            min_distance = route.distance

    if min_distance is None:
        raise RouteNotFound
    return min_distance
