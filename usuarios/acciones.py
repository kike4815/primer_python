import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nOK! Vamos a registrarte en el sistema...")

        nombre = input("introduce tu nombre: ")
        apellidos = input("introduce tus apellidos: ")
        email = input("introduce tu email: ")
        password = input("introduce tu password: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"\nperfecto!! {registro[1].nombre} te has registrado con el mail {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nidentificate en el sistema....")
        try:
            email = input("introduce tu email: ")
            password = input("introduce tu password: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()

            if(email == login[3]):
                print(
                    f"\n Bienvenido {login[1]}, te has registrado el dia {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto, vuelvalo a intentar")

    def proximasAcciones(self, usuario):
        print("""
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input("Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if(accion == "crear"):
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif(accion == "mostrar"):
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif(accion == "eliminar"):
            hazEl.eliminar(usuario)
            self.proximasAcciones(usuario)
        elif(accion == "salir"):
            exit()
