from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve



app = Flask(__name__)
cors = CORS(app)
'''Inicio de rutas controladoras de modelo mesa'''
from Controladores.ControladorMesa import ControladorMesa
miControladorMesa=ControladorMesa()

@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(numero):
    json=miControladorMesa.show(numero)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(numero):
    data = request.get_json()
    json=miControladorMesa.update(numero,data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(numero):
    json=miControladorMesa.delete(numero)
    return jsonify(json)
'''Aqui finaliza las rutas controladoras del modelo mesa'''



'''Inicio de rutas controladoras de modelo Candidato'''
from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato=ControladorCandidato()

@app.route("/candidato",methods=['GET'])
def getCandidato():
    json=miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidato/<string:cedula>",methods=['GET'])
def getCandidato(cedula):
    json=miControladorCandidato.show(cedula)
    return jsonify(json)

@app.route("/candidato/<string:cedula>",methods=['PUT'])
def modificarCandidato(cedula):
    data = request.get_json()
    json=miControladorCandidato.update(cedula,data)
    return jsonify(json)

@app.route("/candidato/<string:cedula>",methods=['DELETE'])
def eliminarCandidato(cedula):
    json=miControladorCandidato.delete(cedula)
    return jsonify(json)



'''Inicio de rutas controladoras de modelo Partido'''
from Controladores.ControladorPartido import ControladorPartido
miControladorPartido=ControladorPartido()

@app.route("/partido",methods=['GET'])
def getPartido():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partido/<string:Id_partido>",methods=['GET'])
def getPartido(Id_partido):
    json=miControladorPartido.show(Id_partido)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarPartido(Id_partido):
    data = request.get_json()
    json=miControladorPartido.update(Id_partido,data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarPartido(Id_partido):
    json=miControladorPartido.delete(Id_partido)
    return jsonify(json)
'''Aqui finaliza las rutas controladoras del modelo Partido'''


'''Inicio de rutas controladoras de modelo Resultado'''
from Controladores.ControladorResultado import ControladorResultado
miControladorResultado=ControladorResultado()

@app.route("/resultado",methods=['GET'])
def getResultado():
    json=miControladorResultado.index()
    return jsonify(json)

@app.route("/resultado",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=miControladorResultado.create(data)
    return jsonify(json)

@app.route("/mesas/<string:Id_Resultado>",methods=['GET'])
def getResultado(Id_Resultado):
    json=miControladorResultado.show(Id_Resultado)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarResultado(Id_Resultado):
    data = request.get_json()
    json=miControladorResultado.update(Id_Resultado,data)
    return jsonify(json)

@app.route("/mesas/<string:Id_Resultado>",methods=['DELETE'])
def eliminarResultado(Id_Resultado):
    json=miControladorResultado.delete(Id_Resultado)
    return jsonify(json)
'''Aqui finaliza las rutas controladoras del modelo mesa'''










'''@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)'''

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Corriendo Servidor en : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])