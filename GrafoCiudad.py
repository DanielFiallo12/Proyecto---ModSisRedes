class GrafoCiudad:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, origen, destino, peso):
        if origen not in self.grafo:
            self.grafo[origen] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[origen].append((destino, peso))
        self.grafo[destino].append((origen, peso))

    def construir_grafo(self):
        for calle in range(50, 56):
            for carrera in range(10, 15):
                nodo_actual = (calle, carrera)
                if carrera < 14:
                    tiempo_carrera_javier = 6 if carrera in [12, 13, 14] else 4
                    tiempo_carrera_andreina = tiempo_carrera_javier + 2
                    self.agregar_arista(nodo_actual, (calle, carrera + 1), tiempo_carrera_javier)
                    self.agregar_arista(nodo_actual, (calle, carrera + 1), tiempo_carrera_andreina)
                if calle < 55:
                    tiempo_calle_javier = 8 if calle == 51 else 4
                    tiempo_calle_andreina = tiempo_calle_javier + 2
                    self.agregar_arista(nodo_actual, (calle + 1, carrera), tiempo_calle_javier)
                    self.agregar_arista(nodo_actual, (calle + 1, carrera), tiempo_calle_andreina)