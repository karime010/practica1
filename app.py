from flask import Flask, redirect, render_template, request, session
from gestor_tareas import GestorTareas

app = Flask(__name__) 
app.secret_key = "mimecita2.0" #La puse para proteger la sesion

gestor = GestorTareas()




from flask import Flask, render_template, request, redirect, url_for

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("formulario.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)