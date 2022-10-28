from Modelos.Candidato import Candidato

class ControladorCandidato():


    def __init__(self):
        print("Creando controlador  Candidato")


    def index(self):
        print("Listar  el Candidato ")
        unCandidato =[
            {
                "cedula": 1111111,
                "numero_resolucion": "11",
                "nombre": "Sebastian",
                "Apellido": "Palacios"
            },
            {
                "cedula": 2222222,
                "numero_resolucion": "22",
                "nombre": "Juan",
                "Apellido": "Ramirez"

            }

                    ]
        return [unCandidato]




    def create(self, cedula,numero_resolucion,nombre,apellido):
        print("Crear un Candidato")
        Elcandidato = Candidato(cedula,numero_resolucion,nombre,apellido)
        return Elcandidato.__dict__

    def show(self, cedula):
        print("Mostrando un candidato", cedula)
        Elcandidato = {
            "numero": cedula,
            "numero_resolucion": "11",
            "nombre": "Sebastian",
            "Apellido": "Palacios"
              }
        return Elcandidato


    def update(self, cedula, infocandidato):
        print("Actualizando candidato con cedula  ", cedula)
        Elcandidato = Candidato(infocandidato)
        return Elcandidato.__dict__


    def delete(self, cedula):
        print("Eliminando candidado con la cedula ", cedula)
        return {"deleted_count":cedula}