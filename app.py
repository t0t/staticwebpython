from flask import Flask, render_template, request
app = Flask(__name__) #la instancia de Flask

numeros = []

@app.route("/") #decorador para crear rutas
def home():
    nombre="Sergio"
    num = 12
    lista = [1,2,3,4,5,6,7,8]
    return render_template("home.html", prueba="pruebaaaa",nombre=nombre, num=num, lista=lista)

@app.route("/contacto", methods=["POST"])
def contacto():
    camponombre = request.form.get("camponombre")
    numeros.append(f"{camponombre}")
    return render_template("contacto.html", camponombre=camponombre, numeros=numeros)

@app.route("/about")
def about():
    return render_template("about.html", title="titulo")

@app.route("/hola/<string:nombre>")
def hola(nombre):
    return f"<h1>Holaaaa: {nombre}</h1>"

if __name__ == "__main__":
    freezer.run(debug=True)