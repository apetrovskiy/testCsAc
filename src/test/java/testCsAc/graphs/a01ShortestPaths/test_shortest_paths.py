from src.main.java.testCsAc.graphs.a01ShortestPaths.solution_shortest_paths import shortest_paths
from typing import List
import pytest


test_data = [
    (5, 7, 2, [[1, 2], [2, 1], [2, 2], [3, 2],
               [2, 5], [5, 3], [4, 5]], [1, 0, 2, -1, 1]),
    (2, 1, 2, [[1, 2]], [-1, 0]),
    (3, 3, 2, [[1, 2], [2, 3], [3, 1]], [2, 0, 1]),
    (2, 3, 2, [[1, 3], [3, 2], [2, 1]], [1, 0, 2]),
    (3, 2, 2, [[1, 2], [2, 3]], [-1, 0, 1]),
    (7, 12, 2, [[1, 2], [2, 1], [1, 3], [3, 1], [2, 4], [4, 2], [2, 5], [
     5, 2], [3, 6], [6, 3], [3, 7], [7, 3]], [1, 0, 2, 1, 1, 3, 3])
]


@pytest.mark.parametrize("N,M,v,data,expected_result", test_data)
def test_shortest_paths(N: int, M: int, v: int, data: List[List[int]], expected_result: List[int]):
    # TODO: user better comparison
    assert expected_result == shortest_paths(N, M, v, data)
