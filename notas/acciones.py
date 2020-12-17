import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"\nOK! {usuario[1]},vamos a crear una nota nueva")

        titulo = input('Introduce el titulo: ')
        descripcion = input("Mete el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        save = nota.guardar()

        if save[0] >= 1:
            print(f"perfecto!! has guardado la nota: {nota.titulo}")
        else:
            print(f'lo siento {usuario[1]} no se ha guardado')

    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}, aquí tienes tus notas: ")

        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for listNotas in notas:
            print("\n***********************")
            print(listNotas[2])
            print(listNotas[3])
            print("***********************")

    def eliminar(self, usuario):
        print(f"\nVale {usuario[1]}, vamos a eliminar la nota: ")

        titulo = input("Introduce el titulo de la nota: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No hemos borrado la nota, lo siento")
