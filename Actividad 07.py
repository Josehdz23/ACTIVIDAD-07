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
                            carnet = int(input("Ingrese el carnet del estudiante: "))
                            if carnet > 0:
                                break
                            else:
                                print("El carnet no es valido, reintente")
                        while True:
                            edad = int(input("Ingrese la edad del estudiante: "))
                            if edad > 0:
                                break
                            else:
                                print("La edad no es valida, reintente")
                    except Exception as ex2:
                        print(f"Ocurrió un error: {ex2}, reintente")
        except Exception as ex:
            print(f"Ocurrió un error: {ex}, reintente")

def main():
    while True:
        menu()
        try:
            op = int(input("Escoga una opción: "))
            match op:
                case 1:
                    registrar_Estudiantes()
                case 4:
                    print("Saliendo...")
                    break
                case _:
                    print("Esa opción no existe")

        except Exception as ex:
            print(f"Ocurrió un error: {ex}, reintente")

main()