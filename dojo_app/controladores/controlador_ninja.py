from flask import render_template, request, redirect, session
from dojo_app import app
from dojo_app.modelos import modelo_dojo, modelo_ninjas

@app.route( '/ninjas', methods=["GET"] )
def desplegar():

    dojos = modelo_dojo.Dojo.mostrarNinjas()
    return render_template("ninjas.html", dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        "dojo": request.form["dojo"],
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "age": request.form["age"]
    }

    ninja = modelo_ninjas.Ninja.guardar(data)

    if ninja:
        return redirect(f'/dojos/{request.form["dojo"]}')
    else:
        return redirect('/dojos')