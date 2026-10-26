from src.registro import registrar_ingreso, cargar


def menu():
    while True:
        print("\n=== ESTACIONAMIENTO TECMI ===")
        print("1. Registrar ingreso de vehículo")
        print("2. Ver vehículos dentro")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            placa = input("Placa: ")
            tipo = input("Tipo (auto/moto): ")
            try:
                r = registrar_ingreso(placa, tipo)
                print(f"Ingreso registrado: {r['placa']} ({r['tipo']}) a las {r['hora_ingreso']}")
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "2":
            vehiculos = cargar()
            if not vehiculos:
                print("No hay vehículos dentro.")
            for v in vehiculos:
                print(f"- {v['placa']} | {v['tipo']} | {v['hora_ingreso']}")
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
