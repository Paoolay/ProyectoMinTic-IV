from Modelos.Partido import Partido

class ControladorPartido():


    def __init__(self):
        print("Creando controlador   Partido")


    def index(self):
        print("Listar  todas las  Partido")
        ElPartido =[
            {
                "Id_partido": 3333333,
                "Nombre": "Azul",
                "Lema":"La fuerza que decide"

            },
            {
                "Id_partido": 444444,
                "Nombre": "Rojo",
                "Lema":"Porque la Comunidad funcina"
            }

        ]
        return [ElPartido]




    def create(self,Id_partido,Nombre,Lema):
        print("Crear un Partido")
        Elpartido = Partido(Id_partido,Nombre,Lema)
        return Elpartido.__dict__

    def show(self, Id_partido):
        print("Mostrando un Partido",Id_partido)
        Elpartido = {
            Id_partido: 1,
            "Nombre": "Azul",
            "Lema": "La fuerza que decide"
              }
        return Elpartido


    def update(self,Id_partido, Nombre,Lema):
        print("Actualizando Partido: ", Id_partido)
        Elpartido = Partido(Nombre,Lema)
        return Elpartido.__dict__


    def delete(self, Id_partido):
        print("Eliminando mesa un partido con id: ", Id_partido)
        return {"deleted_count:", Id_partido}
