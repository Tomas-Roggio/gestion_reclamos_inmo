import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('reclamos.db')
cursor = conn.cursor()

# Crear tabla 
cursor.execute('''
CREATE TABLE IF NOT EXISTS reclamos (
    id_reclamo INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    direccion_propiedad TEXT NOT NULL,
    propietario TEXT NOT NULL,
    gremio TEXT NOT NULL,
    empleado TEXT NOT NULL,
    estado_reclamo TEXT NOT NULL
)
''')

# Función para agregar un reclamo
def agregar_reclamo():
    fecha = input("Ingrese la fecha del reclamo: ")
    direccion = input("Ingrese la dirección de la propiedad: ")
    propietario = input("Ingrese el nombre del propietario: ")
    gremio = input("Ingrese el  gremio: ")
    empleado = input("Ingrese el empleado: ")
    estado = input("Ingrese el estado del reclamo: ")
    
    cursor.execute('''INSERT INTO reclamos (fecha, direccion_propiedad, propietario, gremio, empleado, estado_reclamo)
                      VALUES (?, ?, ?, ?, ?, ?)''', (fecha, direccion, propietario, gremio, empleado, estado))
    conn.commit()
    print("Reclamo agregado correctamente.")

# Función para eliminar un reclamo
def eliminar_reclamo():
    direccion = input("Ingrese la dirección del reclamo que desea eliminar: ")
    cursor.execute("SELECT * FROM reclamos WHERE direccion_propiedad=?", (direccion,))
    reclamos = cursor.fetchall()
    if reclamos:
        print("Se encontraron múltiples reclamos con la misma dirección:")
        for idx, reclamo in enumerate(reclamos, start=1):
            print(f"{idx}. {reclamo}")
        
        while True:
            seleccion = input("Ingrese el número del reclamo que desea eliminar: ")
            if seleccion.isdigit():
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(reclamos):
                    confirmacion = input("¿Está seguro que desea eliminar este reclamo? (s/n): ")
                    if confirmacion.lower() == 's':
                        cursor.execute("DELETE FROM reclamos WHERE id_reclamo=?", (reclamos[seleccion-1][0],))
                        conn.commit()
                        print("Reclamo eliminado correctamente.")
                    else:
                        print("Operación de eliminación cancelada.")
                    break
                else:
                    print("Número de selección no válido.")
            else:
                print("Por favor, ingrese un número válido.")
    else:
        print("La dirección de la propiedad ingresada no existe.")

# Función para modificar un reclamo
def modificar_reclamo():
    direccion = input("Ingrese la dirección: ")
    cursor.execute("SELECT * FROM reclamos WHERE direccion_propiedad=?", (direccion,))
    reclamos = cursor.fetchall()
    if reclamos:
        print("Se encontraron múltiples reclamos con la misma dirección:")
        for idx, reclamo in enumerate(reclamos, start=1):
            print(f"{idx}. {reclamo}")
        
        while True:
            seleccion = input("Ingrese el número del reclamo que desea modificar: ")
            if seleccion.isdigit():
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(reclamos):
                    nuevo_estado = input("Ingrese el nuevo estado del reclamo: ")
                    cursor.execute("UPDATE reclamos SET estado_reclamo=? WHERE id_reclamo=?", (nuevo_estado, reclamos[seleccion-1][0]))
                    conn.commit()
                    print("Reclamo modificado correctamente.")
                    break
                else:
                    print("Número de selección no válido.")
            else:
                print("Por favor, ingrese un número válido.")
    else:
        print("La dirección de la propiedad ingresada no existe.")

# Función para ver todos los reclamos
def ver_reclamos():
    cursor.execute("SELECT * FROM reclamos")
    reclamos = cursor.fetchall()
    for reclamo in reclamos:
        print(reclamo)

# Función para buscar reclamos
def buscar_reclamos():
    direccion = input("Ingrese la dirección del reclamo que desea buscar: ")
    cursor.execute("SELECT * FROM reclamos WHERE direccion_propiedad=?", (direccion,))
    reclamos = cursor.fetchall()
    if reclamos:
        for reclamo in reclamos:
            print(reclamo)
    else:
        print("No se encontraron reclamos para esa direccion.")



# Menú principal
while True:
    print("\nMenú:")
    print("1. Agregar reclamo")
    print("2. Eliminar reclamo")
    print("3. Modificar reclamo")
    print("4. Ver reclamos")
    print("5. Buscar reclamos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_reclamo()
    elif opcion == "2":
        eliminar_reclamo()
    elif opcion == "3":
        modificar_reclamo()
    elif opcion == "4":
        ver_reclamos()
    elif opcion == "5":
        buscar_reclamos()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
# Cerrar la conexión a la base de datos
conn.close()