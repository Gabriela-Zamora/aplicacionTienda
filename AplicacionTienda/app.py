from re import U
from flask import Flask, render_template, request
from clases.operacionesMatematicas import *
from Procesos import *


app = Flask(__name__)

titulosTablaUsuarios=("Documento","Nombre","Telefono","Valor")

operacionesM=OperacionesMatematicas()
misProcesos=Procesos()
misProcesos.llenarLista()

@app.route("/")
def index():
    return render_template('inicio.html')

@app.route("/inicio")
def inicio():
    return render_template('inicio.html', user=Procesos.usuarioGlobal)

@app.route("/pago")
def pago_empleados():
    return render_template('pagoEmpleados.html', user=Procesos.usuarioGlobal)

@app.route("/registrar")
def registro():
    return render_template('registro.html', user=Procesos.usuarioGlobal)


@app.route("/gestionar_empleados")
def gestion_usuario():
    return render_template('gestionar_empleados.html',user=Procesos.usuarioGlobal)

@app.route("/pagoTotal", methods=['GET', 'POST'])
def pagoTotal():
    resultado=None
    if request.method == 'POST':
        num1=int(request.form['salario'])
        num2=int(request.form['abono'])
        num3=int(request.form['deuda'])
        cliente=(request.form['cliente'])

        resultado=operacionesM.sumar(num1,num2,num3)

        res={
            "num1":num1,
            "num2":num2,
            "num3":num3,
            "resultado":resultado,
            "empleado":cliente
            }
        print(resultado)
        
    return render_template('pagoEmpleados.html', data=res)

@app.route("/valida_usuarios", methods=['GET', 'POST'])
def valida_usuarios():
    informacion=misProcesos.obtenerLista()
    global datos
    resultado=""
    if request.method == 'POST':

            usuario=None
            datos=None
            documento=request.form['documento']
            nombre=request.form['nombre']
            telefono=request.form['telefono']
            valor=request.form['valor']

            if ('buscar' in request.form):
                usuario=misProcesos.consultar(documento)
                if(usuario==None):
                    resultado="El Empleado no se encuentra registrado!"

            elif('registrar' in request.form):
                print("Registrar")
                usuario=misProcesos.consultar(documento)
                if usuario==None:
                    usuario=Usuario(documento,nombre,telefono,valor)
                    misProcesos.registrar(usuario)
                    resultado=misProcesos.registrar(usuario)
                else:
                    resultado=f"El documento ya se encuentra registrado y corresponde a {usuario.nombre}"
            elif('actualizar' in request.form):
                print("actualizar")
                usuario=Usuario(documento,nombre,telefono,valor)
                resultado=misProcesos.actualizar(usuario)
            elif('eliminar' in request.form):
                print("eliminar")
                usuario=Usuario(documento,nombre,telefono,valor)
                resultado=misProcesos.eliminar(documento)

            print("**********************")
            print("VALOR DE EMPLEADO",usuario)
            if(usuario!=None):
                datos={
                    "documento":usuario.documento,
                    "nombre":usuario.nombre,
                    "telefono":usuario.telefono,
                    "valor":usuario.valor,
                    "resultado":resultado
                    }

            
    return render_template('gestionar_empleados.html',titulos_tabla=titulosTablaUsuarios,data=informacion,usuario=datos,user=Procesos.usuarioGlobal)



@app.route("/registro_usuario", methods=['GET', 'POST'])
def registrarEmpleado():
    resultado=None
    documento,nombre,telefono,email,tipo="","","","",""

    if request.method == 'POST':
        usuario=None
        documento=request.form['documento']
        nombre=request.form['nombre']
        telefono=request.form['Telefono']
        valor=request.form['valor']

        print("Registrar")
            
        usuario=misProcesos.consultar(documento)
        if usuario==None:
            usuario=Usuario(documento,nombre,telefono,valor)
            misProcesos.registrar(usuario)
            resultado=misProcesos.registrar(usuario)
        else:
            resultado=f"El documento ya se encuentra registrado y corresponde a {usuario.nombre}"       
      

        datos={
            "resultado":resultado
        }

    return render_template('registro.html',data=datos)

if (__name__ == '__main__'): 
    app.run(debug=True,port=8080)