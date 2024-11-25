import heapq

class Ruta:
    @staticmethod
    def dijkstra(grafo, inicio, destino):
        distancias = {nodo: float('inf') for nodo in grafo}
        caminos = {nodo: [] for nodo in grafo}
        distancias[inicio] = 0
        caminos[inicio] = [inicio]
        pq = [(0, inicio)]

        while pq:
            distancia_actual, nodo_actual = heapq.heappop(pq)
            if distancia_actual > distancias[nodo_actual]:
                continue

            for vecino, peso in grafo[nodo_actual]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    caminos[vecino] = caminos[nodo_actual] + [vecino]
                    heapq.heappush(pq, (nueva_distancia, vecino))

        return distancias[destino], caminos[destino]