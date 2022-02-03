from flask import render_template, request, redirect, session,flash
from dojo_app import app
from dojo_app.modelos import modelo_dojo



@app.route( '/', methods=['GET'] )
def despliegadojos():
    return redirect('/dojos')

@app.route('/dojos', methods=['GET'])
def dojos():
    dojos = modelo_dojo.Dojo.mostrarNinjas()
    return render_template("index.html", dojos = dojos)

@app.route('/dojos/<int:id>', methods=['GET'])
def dojo_ninjas(id):
    data = {
        "dojoId": id
    }

    dojo = modelo_dojo.Dojo.mostrarDojosYNinjas(data)
    return render_template("listaDojo.html", dojo = dojo)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form["name"],
    }

    modelo_dojo.Dojo.guardar(data)
    return redirect('/dojos')