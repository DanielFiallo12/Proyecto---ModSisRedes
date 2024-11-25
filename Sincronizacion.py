class Sincronizacion:
    @staticmethod
    def sincronizar_tiempos(tiempo_javier, tiempo_andreina):
        if tiempo_javier < tiempo_andreina:
            diferencia = tiempo_andreina - tiempo_javier
            return f"Javier debe salir {diferencia} minutos después de Andreína."
        elif tiempo_andreina < tiempo_javier:
            diferencia = tiempo_javier - tiempo_andreina
            return f"Andreína debe salir {diferencia} minutos después de Javier."
        else:
            return "Ambos deben salir al mismo tiempo."