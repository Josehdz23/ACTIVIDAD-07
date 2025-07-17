estudiantes = {}
def menu():
    print("\n===== MENÚ PRINCIPAL =====\n1. Registrar estudiantes\n2. Mostrar todos los estudiantes y cursos\n3. Buscar estudiante por carnet\n4. Salir")

def registrar_Estudiantes():
    while True:
        try:
            print("\n===== REGISTRAR ESTUDIANTES =====")
            cantidad = int(input("\n¿Cuántos estudiantes quiere registrar?: "))
            for i in range(cantidad):
                    try:
                        while True:
                            carnet = int(input(f"Ingrese el carnet del estudiante {i + 1}: "))
                            if carnet > 0:
                                break
                            else:
                                print("\nEl carnet no es valido, reintente")
                        while True:
                            nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
                            if nombre or nombre.isspace():
                                break
                            else:
                                print("\nEl nombre del estudiante no es valido, reintente")
                        while True:
                            edad = int(input(f"Ingrese la edad del estudiante {i + 1}: "))
                            if edad > 18 and edad < 60:
                                break
                            else:
                                print("\nLa edad no es valida, reintente")
                        while True:
                            carrera = input(f"Ingrese la carrera del estudiante {i + 1}: ")
                            if carrera or carrera.isspace():
                                break
                            else:
                                print("\nEl nombre de la carrera no es valida, reintente")
                        while True:
                            try:
                                cursos = int(input(f"Ingrese cuantos cursos se le agregaran al estudiante {i + 1}: "))
                                for j in range(cursos):
                                    while True:
                                        nombreCurso = input(f"Ingrese el nombre del curso {j + 1}: ")
                                        if nombreCurso or nombreCurso.isspace():
                                            break
                                        else:
                                            print("\nEl nombre del curso no es valido, reintente")
                                    while True:
                                        notaTareas = float(input(f"Ingrese la nota del curso {j + 1}: "))
                                        if notaTareas > 0 and notaTareas < 30:
                                            break
                                        else:
                                            print("\nLa nota de las tareas no es valida, reintente")
                                    while True:
                                        notaParcial = float(input(f"Ingrese la nota del curso {j + 1}: "))
                                        if notaParcial > 0 and notaParcial < 30:
                                            break
                                        else:
                                            print("\nLa nota del parcial no es valida, reintente")
                                    while True:
                                        notaProyecto = float(input(f"Ingrese la nota del curso {j + 1}: "))
                                        if notaProyecto > 0 and notaProyecto < 40:
                                            break
                                        else:
                                            print("\nLa nota del proyecto no es valida, reintente")
                                    estudiantes[carnet] = {
                                        "Nombre": nombre,
                                        "Edad": edad,
                                        "Carrera": carrera,
                                        "Cursos":{
                                            "Nombre Curso":{
                                                "Notas Tareas":notaTareas,
                                                "Notas Parcial":notaParcial,
                                                "Notas Proyecto":notaProyecto
                                            }
                                        }
                                    }
                            except Exception as ex3:
                                print(f"\nOcurrió un error: {ex3}, reintente")
                    except Exception as ex2:
                        print(f"\nOcurrió un error: {ex2}, reintente")
        except Exception as ex:
            print(f"\nOcurrió un error: {ex}, reintente")

def mostrar_estudiantes():
    for clave, datos in estudiantes.items():
        print(f"Carnet: {clave}, Nombre: {datos['Nombre']}, Edad: {datos['Edad']}, Carrera: {datos['Carrera']}\nCursos: ")
        for dato in datos['Cursos']:
            print(f"Nombre Curso: {datos['Cursos']["Nombre Curso"]}")
            print(f"Nota de tareas: {datos['Cursos']["Nota Tareas"]}\nNota Parcial: {datos['Cursos']["Nota Parcial"]}\nNota Proyecto: {datos['Cursos']["Nota Proyecto"]}")

def main():
    while True:
        menu()
        try:
            op = int(input("Escoga una opción: "))
            match op:
                case 1:
                    registrar_Estudiantes()
                case 2:
                    mostrar_estudiantes()
                case 4:
                    print("\nSaliendo...")
                    break
                case _:
                    print("\nEsa opción no existe")

        except Exception as ex:
            print(f"\nOcurrió un error: {ex}, reintente")

main()