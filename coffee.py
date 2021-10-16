from flask import Flask,redirect,url_for,render_template,request
from werkzeug.utils import html

app=Flask(__name__)

@app.route('/')
def redireccion():
    return redirect('/login')


@app.route('/login',methods=['GET','POST'])
def login():
    if 'iniciar' in request.args:
       iniciar=str(request.args['iniciar'])
       if(iniciar=='Inicia Sesion'):
           return redirect('/menu')
    else:
        return render_template('login.html')

@app.route("/registro")
def registro(): 
    if 'iniciar' in request.args:
       iniciar=str(request.args['iniciar'])
       if(iniciar=='Registrate'):
           return redirect('/menu')
    else:
        return render_template('registro.html')


@app.route("/pedidos")
def pedidos():
    return render_template('pedidos.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/bebida")
def detallebebida():
    return render_template('bebida.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html')

@app.route("/busqueda")
def busqueda():
    return render_template('busqueda.html')

@app.route("/gestionbebidas")
def gestionbebidas():
    return render_template('gestionbebidas.html')






# @app.route("/api/peliculas",methods=['GET'])
# def api_pelicula():
#     if 'id' in request.args:
#         id=int(request.args['id'])
#     else:
#         return "Error: No ingreso ninguna id."


    
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)