from tareas import Agenda

def test_registrar_tarea():
    agenda = Agenda()
    agenda.registrar_tarea("Estudiar", "Scrum y XP")
    assert len(agenda.tareas) == 1
    assert agenda.tareas[0]["estado"] == "pendiente"

def test_listar_tareas():
    agenda = Agenda()
    agenda.registrar_tarea("Tarea 1", "Desc")
    assert len(agenda.listar_tareas()) == 1

def test_editar_tarea():
    agenda = Agenda()
    agenda.registrar_tarea("Viejo", "Desc")
    agenda.editar_tarea(0, "Nuevo", "Actualizado")
    assert agenda.tareas[0]["titulo"] == "Nuevo"

def test_eliminar_tarea():
    agenda = Agenda()
    agenda.registrar_tarea("Eliminar", "Desc")
    agenda.eliminar_tarea(0)
    assert len(agenda.tareas) == 0

def test_marcar_completada():
    agenda = Agenda()
    agenda.registrar_tarea("Finalizar", "Desc")
    agenda.marcar_completada(0)
    assert agenda.tareas[0]["estado"] == "completada"
