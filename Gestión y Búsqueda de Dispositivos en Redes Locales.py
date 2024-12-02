import platform
import psutil

# Obtener información del sistema
a = platform.node()  # Nombre del equipo
b = platform.architecture()  # Arquitectura
c = platform.machine()  # Tipo de sistema

# Uso de memoria
g = psutil.virtual_memory()

# Uso de disco
h = psutil.disk_usage('/')

print("///// Información ////")
print("Nombre del equipo:", a)
print("Arquitectura:", b)
print("Tipo de sistema:", c)

print("////// Uso del sistema //////")
print(f"Memoria Total: {g.total / (1024 ** 3):.2f} GB")
print(f"Memoria disponible: {g.available / (1024 ** 3):.2f} GB")
print(f"Uso de disco: {h.percent}%")
print(f"Espacio total en disco: {h.total / (1024 ** 3):.2f} GB")
print(f"Espacio disponible en disco: {h.free / (1024 ** 3):.2f} GB")
