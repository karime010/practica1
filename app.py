from flask import Flask, redirect, render_template, request, session #Session recordar al usuario entre paginas
from practica1 import GestorTareas #Ve a practica1 y trae la clase GestorTareas

app = Flask(__name__) 
app.secret_key = "mimecita2.0" #La puse para proteger la sesion

gestor = GestorTareas()

#Muestra el formulario de registro
@app.route("/")
def inicio():
    return render_template("formulario.html")


@app.route("/registro", methods=["POST"])
def registro():
    nombre = request.form["nombre"]
    email = request.form["email"]


    gestor.crear_usuario(nombre, email)

    return render_template("login.html")

@app.route("/login")
def login_plantilla():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]

    usuario = gestor.usuarios.find_one({"email": email})

    if usuario: #Encontre un usuario con ese email
        session["usuario_id"] = str(usuario["_id"])
        return redirect("/tareas") #Existe y te manda a la pagina de tareas + le pasa informacion y permite conectar con mongodb
    else:
        return "Usuario no encontrado" #No existe un usuario con ese email



if __name__ == "__main__":
    app.run(debug=True)