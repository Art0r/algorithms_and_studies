package main

import (
	"container/heap"
	"math"
)

var graphs = [2]map[string]map[string]uint64{
	{
		"A": {"B": 5, "C": 2},
		"B": {"E": 2, "D": 4},
		"C": {"B": 8, "E": 7},
		"D": {"F": 3, "E": 6},
		"E": {"F": 1},
		"F": {},
	},
	{
		"A": {"B": 10},
		"B": {"D": 20},
		"C": {"B": 1},
		"D": {"E": 30, "C": 1},
		"E": {},
	},
}

type Item struct {
	// 'name' of the node in this case
	value string
	// weight of the node in this case
	priority uint64
	index    int
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

	return pq[i].priority < pq[j].priority
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

func dijkstra(graph map[string]map[string]uint64, start string) {

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
		value:    start,
		priority: 0,
	})

	for pq.Len() > 0 {
		print(pq.Pop())
	}
}

func main() {
	for _, graph := range graphs {
		dijkstra(graph, "A")
	}
}
