from abc import ABC, abstractmethod

# Modelo
class Tarea(ABC):
    def __init__(self):
        self.estado = "No iniciada"

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def avanzar(self):
        pass

    @abstractmethod
    def finalizar(self):
        pass

class TareaDesarrollo(Tarea):
    def iniciar(self):
        self.estado = "Iniciada en Desarrollo"

    def avanzar(self):
        self.estado = "En progreso en Desarrollo"

    def finalizar(self):
        self.estado = "Finalizada en Desarrollo"

class TareaTesting(Tarea):
    def iniciar(self):
        self.estado = "Iniciada en Testing"

    def avanzar(self):
        self.estado = "En progreso en Testing"

    def finalizar(self):
        self.estado = "Finalizada en Testing"

# Vista
class Vista:
    def mostrar_tarea(self, tarea):
        print(f'Tarea {tarea.__class__.__name__} está {tarea.estado}')

# Controlador
class Controlador:
    def __init__(self):
        self.tareas = []
        self.vista = Vista()

    def crear_tarea(self, tipo):
        if tipo == 'desarrollo':
            tarea = TareaDesarrollo()
        elif tipo == 'testing':
            tarea = TareaTesting()
        else:
            raise ValueError('Tipo de tarea no reconocido')
        self.tareas.append(tarea)
        return tarea

    def iniciar_tarea(self, tarea):
        tarea.iniciar()
        self.vista.mostrar_tarea(tarea)

    def avanzar_tarea(self, tarea):
        tarea.avanzar()
        self.vista.mostrar_tarea(tarea)

    def finalizar_tarea(self, tarea):
        tarea.finalizar()
        self.vista.mostrar_tarea(tarea)



# Primero, instanciamos el controlador
controlador = Controlador()

# Luego, creamos algunas tareas
tarea_desarrollo = controlador.crear_tarea('desarrollo')
tarea_testing = controlador.crear_tarea('testing')

# Verificamos el estado inicial de las tareas
controlador.vista.mostrar_tarea(tarea_desarrollo)
controlador.vista.mostrar_tarea(tarea_testing)

# Iniciamos las tareas
controlador.iniciar_tarea(tarea_desarrollo)
controlador.iniciar_tarea(tarea_testing)

# Avanzamos las tareas
controlador.avanzar_tarea(tarea_desarrollo)
controlador.avanzar_tarea(tarea_testing)

# Finalizamos las tareas
controlador.finalizar_tarea(tarea_desarrollo)
controlador.finalizar_tarea(tarea_testing)
