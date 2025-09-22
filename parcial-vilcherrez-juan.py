class Tarea:
    def __init__(self,titulo,descripcion,estado):
        self.titulo=titulo
        self.descripcion=descripcion
        self.estado=estado
    
class GestorTarea:
    def __init__(self):
        self.tareas=[]

    def agregar_tareas(self,tarea):
            self.tareas.append(tarea)
    
    def eliminar_tarea(self,titulo):
        for index,tarea in enumerate(self.tareas):
            if tarea.titulo==titulo:
                self.tareas.pop(index)
                break
    
    def mostrar_tareas(self):
        print("________TAREAS________")
        if len(self.tareas)==0:
            print("Aun no tiene tareas...")
        else:
            for index,tarea in enumerate(self.tareas):
                print(f"{index+1} |[Titulo] {tarea.titulo}")
                print(f"  |[Descripcion] {tarea.descripcion}")
                print(f"  |[Estado] {tarea.estado}")
                print("_________________________")
    
    def actualizar_estado(self,titulo,nuevo_estado):
        for index,tarea in enumerate(self.tareas):
            if tarea.titulo==titulo:
                self.tareas[index].estado=nuevo_estado
                break
            


def main():
    gestor=GestorTarea()
    #tarea_1=Tarea("Compras","Ir al Supermercado","Pendiente")
    #tarea_2=Tarea("Tramitar pasaporte","Presentar documentacion","Pendiente")
    #tarea_3=Tarea("Limpieza","Limpiar bañera","En Progreso")
    
    #gestor.agregar_tareas(tarea_1)
    #gestor.agregar_tareas(tarea_2)
    #gestor.agregar_tareas(tarea_3)
    
    while True:
        nav="\n________GESTOR DE TAREAS________\n1| Agregar Tarea\n2| Eliminar tarea\n3| Actualizar estado de tarea\n4| Mostrar todas\n0| Salir y mostrar tareas"
        print(f"{nav}\n")
        option=int(input("Seleccione una opcion: "))
        print("\n")
        if option>=0 and option<5:
            if option==1:
                print("\n________AGREGAR TAREA________")
                titulo=input("Titulo: ")
                descripcion=input("Descripcion: ")
                estado=input("Estado [Pendiente | En Progreso | Completada]: ")
                tarea=Tarea(titulo,descripcion,estado)
                gestor.agregar_tareas(tarea)
            elif option==2:
                print("\n________ELIMINAR TAREA________")
                titulo=input("Escriba el titulo de la tarea que quiere elinminar: ")
                gestor.eliminar_tarea(titulo)
            elif option==3:
                print("\n________ACTUALIZAR ESTADO DE TAREA________")
                titulo=input("Titulo: ")
                nuevo_estado=input("Nuevo estado [Pendiente | En Progreso | Completada]: ")
                gestor.actualizar_estado(titulo,nuevo_estado)
            elif option==4:
                gestor.mostrar_tareas()
            else:
                gestor.mostrar_tareas()
                print("\nSaliendo...")
                break
                
        else:
            print("¡Seleccione un opcion valida!\n")
    
main()
        
        
               