class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        # (cost, node, flights_taken)
        minHeap = [(0, src, 0)]

        # Minimum cost to reach node using a given number of flights
        minCost = {}

        while minHeap:
            cost, node, flights_taken = heapq.heappop(minHeap)

            if node == dst:
                return cost

            if flights_taken == k + 1:
                continue

            for nei, price in graph[node]:
                new_cost = cost + price
                new_flights = flights_taken + 1

                state = (nei, new_flights)

                if state not in minCost or new_cost < minCost[state]:
                    minCost[state] = new_cost
                    heapq.heappush(
                        minHeap,
                        (new_cost, nei, new_flights)
                    )

        return -1