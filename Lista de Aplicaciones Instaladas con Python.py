import subprocess

comando = 'wmic product get name'
try:
    result = subprocess.run(comando, stdout=subprocess.PIPE, text=True, shell=True)
    
    aplicaciones = result.stdout.split('\n')
    aplicaciones = [app.strip() for app in aplicaciones if app.strip()]
    
    if len(aplicaciones) > 1:
        print("Aplicaciones instaladas en tu equipo:\n")
        for app in aplicaciones[1:]:  # Ignorar el primer elemento que es el encabezado
            print(app)
    else:
        print("No se encontraron aplicaciones instaladas")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando: {e}")
