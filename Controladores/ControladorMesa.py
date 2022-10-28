from Modelos.Mesa import Mesa

class ControladorMesa():


    def __init__(self):
        print("Creando controlador   mesa")


    def index(self):
        print("Listar  todas las  mesas")
        unaMesa =[
            {
                "Numero": 1,
                "Cantidad_inscritos": "100",
            },
            {
                "Numero": 2,
                "Cantidad_inscritos": "50",
            },
            {
                "Numero": 3,
                "Cantidad_inscritos": "60",
            }
        ]
        return [unaMesa]




    def create(self,infoMesa):
        print("Crear una mesa")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def show(self, numero):
        print("Mostrando una mesa")
        laMesa = {
            "numero": numero,
            "cantida_inscritos": "123"
              }
        return laMesa


    def update(self, numero, infoDelaMesa):
        print("Actualizando mesa con id ", numero)
        laMesa = Mesa(infoDelaMesa)
        return laMesa.__dict__


    def delete(self, numero):
        print("Eliminando mesa con numero ", numero)
        return {"deleted_count":1}