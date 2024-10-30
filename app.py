from flask import Flask, render_template

app = Flask(__name__)

class Pelicula:
    def __init__(self, nombre, año, protagonista):
        self.nombre = nombre
        self.año = año
        self.protagonista = protagonista

@app.route('/')

def hola():
    return "Hola Mundo!!"

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/estructura')
def estructura():
    peliculas = [
        "Orgullo y prejuicio",
        "Harry Potter",
        "Star Wars 1",
        "Interestelar"
    ]
    
    interestelar = {
        "Nombre": "Interestelar",
        "Año": 2014,
        "Protagonista": "Matthew McConaughey"
    }
    
    start = Pelicula(
        "Start Wars 1",
        1999,
        "Ewan McGregor"
        )
    return render_template(
        "estructura.html", 
        peliculas = peliculas, 
        destacada=interestelar,
        favorita=start)

@app.route('/variables')
def variables():
    return render_template(
        "variables.html", 
        nombre = "Susana",
        curso = "Python"
    )
    
@app.route('/expresiones')
def expresiones():
    kwargs = {
        "nombre": "Susana",
        "apellido": "Piñero",
        "base": 5,
        "altura": 10
    }
    return render_template("expresiones.html", **kwargs)

if __name__ == '__main__':
    app.run(debug=True)
