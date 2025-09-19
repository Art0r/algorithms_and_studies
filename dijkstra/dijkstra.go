package main

import (
	"container/heap"
	"fmt"
	"math"
)

type GraphNodeToFind struct {
	node_to_find string
	graph        map[string]map[string]uint64
}

var graphs = []GraphNodeToFind{
	{
		node_to_find: "F",
		graph: map[string]map[string]uint64{
			"A": {"B": 5, "C": 2},
			"B": {"E": 2, "D": 4},
			"C": {"B": 8, "E": 7},
			"D": {"F": 3, "E": 6},
			"E": {"F": 1},
			"F": {},
		},
	},
	{
		node_to_find: "D",
		graph: map[string]map[string]uint64{
			"A": {"B": 10},
			"B": {"D": 20},
			"C": {"B": 1},
			"D": {"E": 30, "C": 1},
			"E": {},
		},
	},
}

type Item struct {
	// 'name' of the node in this case
	value string
	// weight of the node in this case
	weight uint64
	index  int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	if pq[i] == nil && pq[j] == nil {
		return false
	}

	if pq[i] == nil {
		return false
	}

	if pq[j] == nil {
		return true
	}

	return pq[i].weight < pq[j].weight
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(node any) {
	n := len(*pq)
	item := node.(Item)
	item.index = n
	*pq = append(*pq, &item)
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // don't stop the GC from reclaiming the item eventually
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

func dijkstra(graph map[string]map[string]uint64, start string) (map[string]float64, map[string]any) {

	/*
	* estado inicial
	* inicialmente os custos são infinitos pois não sabemos ainda
	* as distancias entre os vertices vizinhos
	 */

	var costs = make(map[string]float64)
	for index := range graph {
		costs[index] = math.Inf(1)
	}

	/*
	* inicialmente os 'pais' são nulos pois não sabemos ainda
	* as relações entre os vertices
	 */
	var parents = make(map[string]any)
	for index := range graph {
		parents[index] = nil
	}

	/*
	* o custo de deslocamento do inicio para
	* o inicio será sempre zero
	 */
	costs[start] = 0

	var pq PriorityQueue = make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, Item{
		value:  start,
		weight: 0,
	})

	for pq.Len() > 0 {
		/*
		* Removendo/Obtendo proximo node fazendo cast para Item
		 */
		node := pq.Pop().(*Item)

		/*
		* se a prioridade/custo do nó atual for maior
		* que o contido na tabela de custos
		* então passe para a proxima iteração
		 */
		if node.weight > uint64(costs[node.value]) {
			continue
		}

		/*
		* Investigando nós vizinhos para obter custos
		* menores que o atual
		 */
		for node_value := range graph[node.value] {
			node_weight := graph[node.value][node_value]
			// um novo custo é calculado com o atual + o peso de seu vizinho
			new_cost := node.weight + node_weight

			/*
			* Se achou um caminho mais eficiente para o vizinho
			* considerando que o estado inicial é infinito então
			* sempre será verdade, porém não necessariamente será
			* verdade no caso de recalcular um valor que ja se tem
			* conhecimento
			 */
			if new_cost < uint64(costs[node_value]) {

				// atualiza o custo de deslocamento para o vizinho
				costs[node_value] = float64(new_cost)

				/*
				* para que o caminho possa ser refeito então
				* o vizinho mais eficiente é adicionado a lista
				* de parents
				 */
				parents[node_value] = node_value

				/*
				 * adiciona o vizinho e seu custo para serem processados
				 * na proxima iteração
				 */
				item := Item{
					weight: new_cost,
					value:  node_value,
				}
				pq = append(pq, &item)
			}

		}

	}

	return costs, parents
}

func main() {
	for _, graph := range graphs {
		fmt.Println("===============================")
		fmt.Println("Graph: ", graph.graph)
		costs, _ := dijkstra(graph.graph, "A")
		fmt.Println("Menor custo: ", costs[graph.node_to_find])
	}
	fmt.Println("===============================")
}
