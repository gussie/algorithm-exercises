"""
Implement a topological sort function that, when given a graph, returns:
- a list of topologically sorted nodes (for DAGs)
- else: None (if the input is cyclic)

NOTES to self:
DFS -- start with
discovered []
processed []

"""

from dataclasses import dataclass
from typing import List, Tuple
from collections import defaultdict
import unittest


@dataclass
class Graph:
    start_node: int
    edges: List[Tuple[int, int]]


def dfs_topological_sort(graph):
    graph_dict = defaultdict(list)
    for (start_node, end_node) in graph.edges:
        graph_dict[start_node].append(end_node)
        if not graph_dict[end_node]:
            graph_dict[end_node] = []

    # # # Attempt 1
    # n = len(graph_dict)
    # visited = [False] * n
    # discovered = [graph.start_node]
    # processed = []
    #
    # for node in range(n):
    #     if not visited[node]:
    #         discovered.append(node)
    #         while discovered:
    #             vertex = discovered.pop()
    #             if visited[node]:
    #                 continue
    #             visited[node] = True
    #             for neighbor in graph_dict[vertex]:
    #                 if not visited[neighbor]:
    #                     discovered.append(neighbor)
    # return list(reversed(processed))

    # Attempt 2: Stuck in infinite loop at end
    discovered = [False] * len(graph_dict)
    processed = []
    stack = [graph.start_node]

    while len(stack) > 0:
        v = stack[-1]
        if not discovered[v]:
            discovered[v] = True

        for node in stack:
            for neighbor in graph_dict[node]:
                if not discovered[neighbor]:
                    if neighbor not in graph_dict:
                        processed.append(neighbor)
                    elif neighbor not in stack:
                        stack.append(neighbor)
                    else:
                        processed.append(stack.pop())
    processed.append(stack.pop())
    return list(reversed(processed))

    # # Attempt 3: Robert
    # visited = []
    # discovered = []
    # next_node = [graph.start_node]
    #
    # while len(next_node) > 0:
    #     node = next_node[-1]  # should be .peek()
    #     for neighbor in graph_dict[node]:
    #         if neighbor not in discovered:
    #             discovered.append(neighbor)
    #             next_node.append(neighbor)  # push
    #     next_node.pop()
    #     visited.append(node)
    #
    # return list(reversed(visited))


class TestSearch(unittest.TestCase):

    # def test_can_construct_graph(self):
    #     g = Graph(1, [(1, 2), (2, 3), (3, 4)])
    #     self.assertEqual(g.edges, [(1, 2), (2, 3), (3, 4)])
    #     print(g)

    def test_sort_line_graph(self):
        g = Graph(0, [(0, 1), (1, 2), (2, 3)])  # 0-->1-->2-->3
        self.assertEqual(dfs_topological_sort(g), [0, 1, 2, 3])
        print(dfs_topological_sort(g))

    # def test_sort_simple_graph(self):
    #     g = Graph(0, [(0, 1), (0, 2), (2, 3)])
    #     self.assertEqual(dfs_topological_sort(g), [0, 1, 2, 3])
    #     print(dfs_topological_sort(g))

    # def test_sort_branched_tree(self):
    #     g = Graph(1, [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)])
    #     self.assertEqual(dfs_topological_sort(g), [1, 2, 4, 6, 5, 3])
    #     print(dfs_topological_sort(g))
    #
    # def test_sort_branched_graph(self):
    #     g = Graph(1, [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6), (3,5)])
    #     self.assertEqual(dfs_topological_sort(g), [1, 2, 4, 3, 5, 6])
    #     print(dfs_topological_sort(g))

    # def test_sort_branched_graph(self):
    #     g = Graph(1, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 6), (5, 6), (6, 7)])
    #     self.assertEqual(dfs_topological_sort(g), [1, 2, 3, 4, 5, 6, 7])
    #     print(dfs_topological_sort(g))

#
# if __name__ == '__main__':
#     unittest.main()
