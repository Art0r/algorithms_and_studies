"""
enquanto a fila não estiver vazia
    retire um vértice v da fila
        para cada vizinho w de v
            se w não está numerado
                então numere w
                    ponha w na fila
"""
from typing import List, Dict, Any, Tuple
import heapq


def breadth_first_search(
        graph: Dict[str, any],
        start: str,
        end: str
):

    pass


def main():
    graphs: List[Dict[str, Any]] = [
        ('F', {
            'A': ['B', 'C'],
            'B': ['E', 'D'],
            'C': ['B', 'E'],
            'D': ['F', 'E'],
            'E': ['F'],
            'F': []
        }),
        ('E', {
            'A': ['B'],
            'B': ['D'],
            'C': ['B'],
            'D': ['E', 'C'],
            'E': [],
        })
    ]

    for index, graph in enumerate(graphs):
        print('===============================')
        print('Graph: {0}'.format(index + 1))
        x = breadth_first_search(graph[1], 'A', graph[0])
        print(x)
    print('===============================')


if __name__ == "__main__":
    main()
