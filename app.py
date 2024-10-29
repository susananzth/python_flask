from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hola():
    return "Hola Mundo!!"

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

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
