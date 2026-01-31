class Agenda:
    def __init__(self):
        self.tareas = []

    def registrar_tarea(self, titulo, descripcion):
        tarea = {
            "titulo": titulo,
            "descripcion": descripcion,
            "estado": "pendiente"
        }
        self.tareas.append(tarea)

    def listar_tareas(self):
        return self.tareas

    def editar_tarea(self, indice, nuevo_titulo, nueva_descripcion):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["titulo"] = nuevo_titulo
            self.tareas[indice]["descripcion"] = nueva_descripcion

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["estado"] = "completada"
