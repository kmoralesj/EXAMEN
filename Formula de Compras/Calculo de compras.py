from flask import Flask, render_template, request

app = Flask(__name__)

# Página de inicio con dos botones
@app.route('/')
def index():
    return render_template('index.html')

# Página para el Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        # Calcular total sin descuento
        total_sin_descuento = cantidad_tarros * 9000

        # Calcular descuento
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        # Calcular total con descuento
        total_con_descuento = total_sin_descuento - descuento

        return render_template('resultado_ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, total_con_descuento=total_con_descuento)

    return render_template('formulario_ejercicio1.html')

# Página para el Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']

        # Verificar usuario y contraseña
        if (nombre == 'juan' and password == 'admin'):
            mensaje = 'Bienvenido administrador juan'
        elif (nombre == 'pepe' and password == 'user'):
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('resultado_ejercicio2.html', mensaje=mensaje)

    return render_template('formulario_ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
