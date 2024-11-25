import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from GrafoCiudad import GrafoCiudad
from Ruta import Ruta
from Sincronizacion import Sincronizacion

class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modelación de Sistemas en Redes")
        self.root.geometry("600x400")

        self.grafo_ciudad = GrafoCiudad()
        self.grafo_ciudad.construir_grafo()
        self.establecimientos = {
            "The Darkness": (50, 14),
            "La Pasión": (54, 11),
            "Mi Rolita": (50, 12)
        }

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Seleccione el establecimiento:").pack(pady=10)
        self.destino_var = tk.StringVar()
        self.combo_establecimientos = ttk.Combobox(
            self.root, textvariable=self.destino_var, values=list(self.establecimientos.keys())
        )
        self.combo_establecimientos.pack(pady=5)
        self.boton_calcular = tk.Button(
            self.root, text="Calcular Ruta", command=self.calcular_ruta
        )
        self.boton_calcular.pack(pady=10)
        self.texto_resultado = tk.Text(self.root, height=15, width=70)
        self.texto_resultado.pack(pady=10)

    def calcular_ruta(self):
        destino = self.destino_var.get()
        if destino not in self.establecimientos:
            messagebox.showerror("Error", "Seleccione un establecimiento válido.")
            return

        destino_coords = self.establecimientos[destino]
        ubicacion_javier = (54, 14)
        ubicacion_andreina = (52, 13)

        tiempo_javier, camino_javier = Ruta.dijkstra(
            self.grafo_ciudad.grafo, ubicacion_javier, destino_coords
        )
        tiempo_andreina, camino_andreina = Ruta.dijkstra(
            self.grafo_ciudad.grafo, ubicacion_andreina, destino_coords
        )
        sincronizacion = Sincronizacion.sincronizar_tiempos(tiempo_javier, tiempo_andreina)

        self.texto_resultado.delete("1.0", tk.END)
        self.texto_resultado.insert(
            tk.END,
            f"Camino de Javier: {camino_javier}\nTiempo: {tiempo_javier} minutos\n\n"
            f"Camino de Andreína: {camino_andreina}\nTiempo: {tiempo_andreina} minutos\n\n"
            f"{sincronizacion}"
        )
        self.graficar_grafo([camino_javier, camino_andreina], [ubicacion_javier, ubicacion_andreina], destino_coords)

    def graficar_grafo(self, caminos, inicios, destino):
        plt.figure(figsize=(8, 8))

        # Graficar cuadrícula
        for x in range(50, 56):
            plt.plot([10, 15], [x, x], color="gray", linestyle="--", linewidth=0.5)
        for y in range(10, 16):
            plt.plot([y, y], [50, 55], color="gray", linestyle="--", linewidth=0.5)

        # Graficar las trayectorias
        colores = ['blue', 'red']
        etiquetas = ["Trayectoria de Javier", "Trayectoria de Andreína"]
        for i, camino in enumerate(caminos):
            x_camino, y_camino = zip(*camino)
            plt.plot(y_camino, x_camino, label=etiquetas[i], color=colores[i], marker="o")

            # Añadir los pesos en las trayectorias
            for j in range(len(camino) - 1):
                origen, destino = camino[j], camino[j + 1]
                peso = next(
                    (p for vecino, p in self.grafo_ciudad.grafo[origen] if vecino == destino), None
                )
                if peso is not None:
                    mid_x = (origen[0] + destino[0]) / 2
                    mid_y = (origen[1] + destino[1]) / 2
                    plt.text(
                        mid_y, mid_x, f"{peso} min", color=colores[i], fontsize=8, ha="center"
                    )

            # Marcar los inicios
            plt.scatter(inicios[i][1], inicios[i][0], color=colores[i], label=f"Inicio {etiquetas[i].split()[-1]}", marker="s", s=100)

        # Marcar el destino
        plt.scatter(destino[1], destino[0], color="green", label="Destino", marker="*", s=150)

        # Configurar gráfico
        plt.title("Trayectorias óptimas en Bogotá (con pesos)")
        plt.xlabel("Carreras")
        plt.ylabel("Calles")
        plt.xlim(9.5, 15.5)
        plt.ylim(49.5, 55.5)
        plt.xticks(range(10, 16))
        plt.yticks(range(50, 56))
        plt.legend()
        plt.grid(True)
        plt.show()

    def ejecutar(self):
        self.root.mainloop()