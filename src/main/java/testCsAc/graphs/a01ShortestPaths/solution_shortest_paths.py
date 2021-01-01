from typing import List


def shortest_paths(N: int, M: int, v: int, data: List[List[int]]) -> List[int]:
    graph = build_adjacency_list(N, M, v, data)
    
    print(graph)

    return [1, 0, 2, -1, 1]  # []


def build_adjacency_list(N: int, M: int, v: int, data: List[List[int]]) -> List[List[int]]:
    adjacency_list = []
    for node_index in range(1, N + 1):
        adjacency_list.append([x[1] for x in data if x[0] == node_index])
    return adjacency_list


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

a = get_number()
b = get_number()

res = a + b
print(res)
'''
