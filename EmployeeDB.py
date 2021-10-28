import sqlite3  
  
con = sqlite3.connect("employee.db")  
print("BASE DE DATOS CREADA CON EXITO")  
  
con.execute("create table Employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, contraseña TEXT NOT NULL, address TEXT NOT NULL, tipo_usuario TEXT NOT NULL)")  

print("TABLA EMPLEADO CREADA SATISFACTORIAMENTE!!")  
  
con.execute("create table Bebidas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, descripcion TEXT NOT NULL, valoracion INTEGER)")

print("Tabla bebidas creada con exito")

con.close()  