from Modelos.Resultado import Resultado

class ControladorResultado():


    def __init__(self):
        print("Creando controlador   Resultado")


    def index(self):
        print("Listar  el Resultado")
        unResultado=[
            {
                "Id_Resultado": 5,
                "Numero de mesa": 1,
                "Id_partido":3333333
            },
            {
                "Id": 6,
                "Numero de mesa": 2,
                "Id_partido": 444444
            }

        ]
        return [unResultado]




    def create(self,infoResultado):
        print("Crear un Resultado")
        ElResultado= resultado(infoResultado)
        return ElResultado.__dict__

    def show(self, id_Resultado):
        print("Mostrando un Resultado: ", id_Resultado)
        ElResultado = {
            "Id_Resultado": 5,
            "Numero de mesa": 1,
            "Id_partido": 3333333
              }
        return ElResultado


    def update(self, id_Resultado, Resultado):
        print("Actualizando mesa con id_Resultado ", id_Resultado)
        ElResultado = resultado(Resultado)
        return ElResultado.__dict__


    def delete(self, id_Resultado):
        print("Eliminando Resultado ", id_Resultado)
        return {"deleted_count":id_Resultado}