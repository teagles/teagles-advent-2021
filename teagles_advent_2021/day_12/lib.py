from collections import namedtuple

Connection = namedtuple('Connection', ['a', 'b'])

START_STR = 'start'
END_STR = 'end'


class Node:
    def __init__(self, label):
        self.label = label
        self.is_start = label == START_STR
        self.is_end = label == END_STR
        self.is_small = label.islower()
        self.connections = set()


class CaveSystem:
    def __init__(self):
        self._start = Node(START_STR)
        self._end = Node(END_STR)
        self.caves = {START_STR: self._start, END_STR: self._end}

    def get_cave(self, label):
        if label not in self.caves:
            a_node = Node(label)
            self.caves[label] = a_node
        else:
            a_node = self.caves[label]
        return a_node

    def _connect(self, a, b):
        self.get_cave(a).connections.add(b)
        self.get_cave(b).connections.add(a)

    def populate(self, connections):
        for connection in connections:
            self._connect(*connection)

    def traverse(self, target_cave, path_to_here, visited_small_caves):
        if target_cave == END_STR:
            return [tuple(path_to_here + [END_STR])]
        else:
            cave = self.get_cave(target_cave)
            if cave.is_small:
                new_visited_small_caves = frozenset().union(visited_small_caves, frozenset([target_cave]))
            else:
                new_visited_small_caves = visited_small_caves
            paths_from_here = []
            for c in cave.connections:
                if c not in visited_small_caves:
                    paths_from_here.extend(
                        self.traverse(c, path_to_here.copy() + [target_cave], new_visited_small_caves))
            return paths_from_here

    def traverse_2(self, target_cave, path_to_here, visited_small_caves, revisited_small_cave):
        if target_cave == END_STR:
            return [tuple(path_to_here + [END_STR])]
        else:
            cave = self.get_cave(target_cave)
            if cave.is_small:
                new_visited_small_caves = frozenset().union(visited_small_caves, frozenset([target_cave]))
            else:
                new_visited_small_caves = visited_small_caves
            paths_from_here = []
            for c in cave.connections:
                if c not in visited_small_caves:
                    paths_from_here.extend(self.traverse_2(c, path_to_here.copy() + [target_cave],
                                                           new_visited_small_caves, revisited_small_cave))
                elif c != START_STR and not revisited_small_cave:
                    paths_from_here.extend(
                        self.traverse_2(c, path_to_here.copy() + [target_cave], new_visited_small_caves,
                                        c))
            return paths_from_here


def parse_input(stream):
    for line in stream:
        yield Connection(*line.strip().split('-'))
