class Dispositivo:
    def __init__(self, nombre, ip):  
        self.nombre = nombre
        self.ip = ip

    def __str__(self):  
        return f"Dispositivo: {self.nombre}, IP: {self.ip}"


class Red:
    def __init__(self):  
        self.dispositivos = []

    def agregar_dispositivo(self, nombre, ip):
        dispositivo = Dispositivo(nombre, ip)
        self.dispositivos.append(dispositivo)
        print(f"{nombre} ha sido agregado a la red.")

    def eliminar_dispositivo(self, nombre):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == nombre:
                self.dispositivos.remove(dispositivo)
                print(f"{nombre} ha sido eliminado de la red.")
                return
        print(f"No se encontró el dispositivo {nombre}.")

    def listar_dispositivos(self):
        if not self.dispositivos:
            print("No hay dispositivos en la red.")
            return
        print("Dispositivos en la red:")
        for dispositivo in self.dispositivos:
            print(dispositivo)


def main():
    red = Red()
    while True:
        print("\nOpciones:")
        print("1. Agregar dispositivo")
        print("2. Eliminar dispositivo")
        print("3. Listar dispositivos")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del dispositivo: ")
            ip = input("Ingresa la dirección IP del dispositivo: ")
            red.agregar_dispositivo(nombre, ip)
        elif opcion == "2":
            nombre = input("Ingresa el nombre del dispositivo a eliminar: ")
            red.eliminar_dispositivo(nombre)
        elif opcion == "3":
            red.listar_dispositivos()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor intenta de nuevo.")


if __name__ == "__main__": 
    main()
