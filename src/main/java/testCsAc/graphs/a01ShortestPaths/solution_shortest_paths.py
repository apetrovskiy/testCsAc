'''
# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

N = get_number()
M = get_number()
v = get_number()
data = []
for i in range(1, M + 1):
    data.append([get_number(), get_number()])
'''

# a = get_number()
# b = get_number()

# res = a + b
# print(res)
# for i in input_parser:
#     print(i)
# print(N)
# print(M)
# print(v)
# print(data)

from collections import deque
from typing import List


def shortest_paths(N: int, M: int, v: int, data: List[List[int]]) -> List[int]:
    graph = build_adjacency_list(N, M, v, data)
    return [get_hops_number(graph, v, x) for x in range(1, N + 1)]


def build_adjacency_list(N: int, M: int, v: int, data: List[List[int]]) -> List[List[int]]:
    adjacency_list = []
    for node_index in range(1, N + 1):
        adjacency_list.append([x[1] for x in data if x[0] == node_index])
    return adjacency_list


def get_hops_number(graph: List[List[int]], source: int, target: int):
    counter = -1
    if target == source:
        counter = 0
        return counter
    if target in graph[source - 1]:
        counter = 1
        return counter
    queue = deque()
    # the first node
    queue.append(1)
    visited = [1]
    while len(queue) > 0:
        current_node = queue.popleft()
        for neighbor in graph[current_node - 1]:
            if target == current_node:
                return counter
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
        counter += 1
    counter = -1
    return counter


# result = ' '.join(str(x) for x in shortest_paths(N, M, v, data))
# print(result)
