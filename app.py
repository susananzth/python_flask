from flask import Flask, render_template, request

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
    # Se utiliza el import "render_template"
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

@app.route('/condicionales')
def condicionales():
    return render_template("condicionales.html", equipo="Barcelona")

@app.route('/bucles')
def bucles():
    dependencias = [
        "Archipiélago Los Monjes",
        "Isla la Tortuga y Cayos adyacentes",
        "Isla La Sola",
        "Islas Los Testigos",
        "Islas los Frailes",
        "Isla de Patos",
        "Archipiélago Los Roques",
        "Isla La Blanquilla",
        "Islas Los Hermanos",
        "Isla La Orchila",
        "Archipiélago Las Aves",
        "Isla de Aves"
    ]
    
    superficies = {
        "Archipiélago Los Monjes": 0.20,
        "Isla la Tortuga y Cayos adyacentes": 156.6,
        "Isla La Sola": 0.0005,
        "Islas Los Testigos": 6.53,
        "Islas los Frailes": 1.92,
        "Isla de Patos": 0.60,
        "Archipiélago Los Roques": 40.61,
        "Isla La Blanquilla": 64.53,
        "Islas Los Hermanos": 2.14,
        "Isla La Orchila": 40,
        "Archipiélago Las Aves": 3.35,
        "Isla de Aves": 0.045
    }
    return render_template(
        "bucles.html", 
        islas = dependencias, 
        superficies = superficies
    )

@app.route('/form', methods = ["GET", "POST"])
def form():
    # Se utiliza el import "request"
    
    info_formulario = ""
    # Si se recibe el metodo post...
    if request.method == "POST":
        info_formulario = request.form.get("nombre")
        
        # Aquí muestra este mensaje en la consola una vez que envía el texto desde el formulario
        print(f"Hola, {info_formulario}")
        
    return render_template("form.html", nombre = info_formulario)

if __name__ == '__main__':
    app.run(debug=True)
