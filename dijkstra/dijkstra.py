from typing import List, Dict, Any, Tuple
import heapq


def dijisktra(graph: Dict[str, any], start: str):

    # estado inicial
    # inicialmente os custos são infinitos pois não sabemos ainda
    # as distancias entre os vertices vizinhos
    costs: Dict[str, Any] = {node: float('infinity') for node in graph}

    # inicialmente os 'pais' são nulos pois não sabemos ainda
    # as relações entre os vertices
    parents: Dict[str, Any] = {node: None for node in graph}

    # o custo de deslocamento do inicio para o inicio será
    # sempre zero
    costs[start] = 0

    # Fila de valores que serão processados
    # inicialmente começando com o nó start
    # necessário usar um heap por ser ideal em casos de fila de
    # prioridade
    priority_queue: List[Tuple[int, str]] = []
    heapq.heappush(priority_queue, (0, start))

    # Executa enquanto a fila não for zerada
    while priority_queue:
        # retira valor da fila de prioridade para ser processados
        cost, node = heapq.heappop(priority_queue)

        # se o custo do nó atual for menor
        # que o contido na tabela de custos
        # então passe para a proxima iteração
        if cost > costs[node]:
            continue

        # Investigando nós vizinhos para obter custos
        # menores que o atual
        for neighbor, weight in graph[node].items():
            # um novo custo é calculado com o atual + o peso de seu vizinho
            new_cost = cost + weight

            # Se achou um caminho mais eficiente para o vizinho
            # considerando que o estado inicial é infinito então
            # sempre será verdade, porém não necessariamente será
            # verdade no caso de recalcular um valor que ja se tem
            # conhecimento
            if new_cost < costs[neighbor]:

                # atualiza o custo de deslocamento para o vizinho
                costs[neighbor] = new_cost

                # para que o caminho possa ser refeito então
                # o vizinho mais eficiente é adicionado a lista
                # de parents
                parents[neighbor] = node

                # adiciona o vizinho e seu custo para serem processados
                # na proxima iteração
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return costs, parents


def main():
    graphs: List[Dict[str, Any]] = [
        ('F', {
            'A': {'B': 5, 'C': 2},
            'B': {'E': 2, 'D': 4},
            'C': {'B': 8, 'E': 7},
            'D': {'F': 3, 'E': 6},
            'E': {'F': 1},
            'F': {}
        }),
        ('E', {
            'A': {'B': 10},
            'B': {'D': 20},
            'C': {'B': 1},
            'D': {'E': 30, 'C': 1},
            'E': {},
        })
    ]

    for index, graph in enumerate(graphs):
        print('===============================')
        print('Graph: {0}'.format(index + 1))
        costs, parents = dijisktra(graph[1], 'A')
        print('Grafo: {0}'.format(graph[1]))
        print('Menor custo para {0}: {1}'.format(graph[0], costs[graph[0]]))
    print('===============================')


if __name__ == "__main__":
    main()
