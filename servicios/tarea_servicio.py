from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.contador = 1

    def agregar_tarea(self, descripcion):
        tarea = Tarea(self.contador, descripcion)
        self.tareas.append(tarea)
        self.contador += 1

    def obtener_tareas(self):
        return self.tareas

    def completar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas[index].marcar_completado()

    def eliminar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas.pop(index)