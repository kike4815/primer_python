"""
Proyecto pyhton y MySQL:
-abrir asistente
-Login o Registro
-Si elegimos registro creará un usuario en la bbdd
-Si elegimos login identificará al usuario y nos preguntará
-crear notas,mostrar, borrarlas

"""

from usuarios import acciones
print("""
Acciones disponibles:
    - Registro
    - Login
""")

hazEl = acciones.Acciones()

accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
