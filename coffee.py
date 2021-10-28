import sqlite3
from flask import Flask,redirect,url_for,render_template,request,form
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

@app.route("/registro", methods = ["POST","GET"])
def registro(): 
    return render_template('registro.html')


@app.route("/pedidos")
def pedidos():
    return render_template('pedidos.html')

@app.route("/menu")
def menu():
    conbl = sqlite3.connect("employee.db")  
    conbl.row_factory = sqlite3.Row  
    cur = conbl.cursor()  
    cur.execute("select * from Bebidas")  
    rows = cur.fetchall()  
    return render_template("menu.html",rows = rows) 

@app.route("/bebida")
def detallebebida():
    conbb = sqlite3.connect("employee.db")  
    conbb.row_factory = sqlite3.Row  
    cur = conbb.cursor()  
    cur.execute("select * from Bebidas")  
    rows = cur.fetchall()  
    return render_template("bebida.html",rows = rows) 

@app.route("/usuarios")
def usuarios():
    conv = sqlite3.connect("employee.db")  
    conv.row_factory = sqlite3.Row  
    cur = conv.cursor()  
    cur.execute("select * from Employees")  
    rows = cur.fetchall()  
    return render_template("usuarios.html",rows = rows) 

@app.route("/busqueda")
def busqueda():
    return render_template('busqueda.html')

@app.route("/gestionbebidas")
def gestionbebidas():
    return render_template('gestionbebidas.html')

@app.route("/miperfil")
def miperfil():
    return render_template('miperfil.html')

@app.route("/agregarbebidas")
def agregarbebidas():
    return render_template('agregarbebidas.html')

@app.route("/listadebebidas")
def listadebebidas():
    conbls = sqlite3.connect("employee.db")  
    conbls.row_factory = sqlite3.Row  
    cur = conbls.cursor()  
    cur.execute("select * from Bebidas")  
    rows = cur.fetchall()  
    return render_template("listadebebidas.html",rows = rows)

@app.route("/listadedeseos")
def listadedeseos():
    return render_template('listadedeseos.html')

@app.route("/eliminarb")
def eliminarb():
    return render_template('eliminarbebidas.html')

@app.route("/eliminaru")
def eliminaru():
    return render_template('borrarcliente.html')










# @app.route("/")  
# def index():  
#     return render_template("index.html");  
 
# @app.route("/add")  
# def add():  
#     return render_template("add.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            contraseña = request.form["contraseña"]  
            address = request.form["address"]
            tipo_usuario = "administrador"  
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (name, contraseña, address, tipo_usuario) values (?,?,?,?)",(name,contraseña,address,tipo_usuario))  
                con.commit()  
                # msg = "Employee successfully Added"
            return redirect('/menu')
                
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"
            return redirect('/registro')
        finally:  
            # return render_template("success.html",msg = msg)
            con.close()  
    else:
        return "No es post"


# PARA GUARDAR LAS BEBIDAS
@app.route("/guardarbebidas",methods = ["POST","GET"])  
def guardarbebidas():  
    msg = "msg"  
    if request.method == "POST":  
        try:
            nombre = request.form["nombre"] 
            url = request.form["url"] 
            descripcion = request.form["descripcion"]  
            valoracion = 0
            with sqlite3.connect("employee.db") as conb:  
                cur = conb.cursor()  
                cur.execute("INSERT into Bebidas (nombre, url, descripcion, valoracion) values (?,?,?,?)",(nombre,url,descripcion,valoracion))  
                conb.commit()  
                # msg = "Employee successfully Added"
            return redirect('/menu')
                
        except:  
            conb.rollback()  
            msg = "We can not add the drink to the list"
            return redirect('/agregarbebidas')
        finally:  
            # return render_template("success.html",msg = msg)
            conb.close()  
    else:
        return "No es post"


#PARA ELIMINAR USUARIOS
@app.route("/eliminarusuario",methods = ["POST"])  
def eliminarusuario():    
    id = request.form["id"]
    with sqlite3.connect("employee.db") as cond:
        try:
            cur= cond.cursor()
            cur.execute("delete from Employees where id=?",(id,))
            msg = "record successfully deleted"
        except:
            print(sqlite3.Error.mensaje)
            msg= "cant be deleted"
        finally:
            return redirect('/usuarios')


#PARA ELIMINAR BEBIDAS
@app.route("/eliminarbebidas",methods = ["POST"])  
def eliminarbebidas():    
    id = request.form["id"]
    with sqlite3.connect("employee.db") as conn:
        try:
            cur= conn.cursor()
            cur.execute("delete from Bebidas where id=?",(id,))
            msg = "record successfully deleted"
        except:
            print(sqlite3.Error.mensaje)
            msg= "cant be deleted"
        finally:
            return redirect('/listadebebidas')

 
# @app.route("/view")  
# def view():  
#     conv = sqlite3.connect("employee.db")  
#     conv.row_factory = sqlite3.Row  
#     cur = conv.cursor()  
#     cur.execute("select * from Employees")  
#     rows = cur.fetchall()  
#     return render_template("usuarios.html",rows = rows)  
 
 
# @app.route("/delete")  
# def delete():  
#     return render_template("delete.html")  
 
# @app.route("/deleterecord",methods = ["POST"])  
# def deleterecord():  
#     id = request.form["id"]  
#     with sqlite3.connect("employee.db") as con:  
#         try:  
#             cur = con.cursor()  
#             cur.execute("delete from Employees where id=?",(id,))  
#             msg = "record successfully deleted"  
#         except:  
#             print(sqlite3.Error.mensaje)
#             msg = "can't be deleted"
              
#         finally:  
#             return render_template("delete_record.html",msg = msg)  
  
# if __name__ == "__main__":  
#     app.run(debug = True)  






# @app.route("/api/peliculas",methods=['GET'])
# def api_pelicula():
#     if 'id' in request.args:
#         id=int(request.args['id'])
#     else:
#         return "Error: No ingreso ninguna id."


    
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)