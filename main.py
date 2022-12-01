from tkinter import *
from tkinter import ttk
import pandas as pd
import csv

def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal = Tk()
    ventana_principal.geometry("550x550")  # DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login")  # TITULO DE LA VENTANA
    
    Label(text="Escoja una opción", bg=pestas_color, width="300", height="2",
          font=("Calibri", 13)).pack()  # ETIQUETA CON TEXTO

    Label(text="").pack()
    Button(text="Acceder", height="2", width="60", bg=pestas_color, command=login_u).pack()  # BOTÓN "Acceder"
    
    Label(text="").pack()
    Button(text="Acceso ventas", height="2", width="60", bg=pestas_color, command=login_v).pack()  # BOTÓN "Acceder"
    
    Label(text="").pack()
    Button(text="Registrarse como usuario", height="2", width="60", bg=pestas_color, command=registro_u).pack()  # BOTÓN "Registrarse".
    
    Label(text="").pack()
    Button(text="Registrarse como vendedor", height="2", width="60", bg=pestas_color, command=registro_v).pack()  # BOTÓN "Registrarse".
    
    Label(text="").pack()
    Label(text="Grupo 1, App Limos", width="300", height="2", font=("Calibri", 11)).pack()
    ventana_principal.mainloop()

def registro_u():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("550x550")

    global entrada_nombre
    global entrada_apellido
    global entrada_telefono
    global entrada_correo
    global entrada_clave
    
    nombre_usuario = StringVar()
    apellido_usuario = StringVar()
    telefono = IntVar()
    correo = StringVar()
    clave = StringVar()
    
    Label(ventana_registro, text="Introduzca datos", bg="DarkGrey", width="300", height="2").pack()
    Label(ventana_registro, text="").pack()
    
    etiqueta_nombre = Label(ventana_registro, text="Nombre")
    etiqueta_nombre.pack()
    
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario)  # ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    
    etiqueta_apellido = Label(ventana_registro, text="Apellido")
    etiqueta_apellido.pack()
    
    entrada_apellido = Entry(ventana_registro, textvariable=apellido_usuario)  # ESPACIO PARA INTRODUCIR EL APELLIDO.
    entrada_apellido.pack()
    
    etiqueta_telefono = Label(ventana_registro, text="Telefono")
    etiqueta_telefono.pack()
    
    entrada_telefono = Entry(ventana_registro, textvariable=telefono)  # ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_telefono.pack()
    
    etiqueta_correo = Label(ventana_registro, text="Correo Electronico")
    etiqueta_correo.pack()
    
    entrada_correo = Entry(ventana_registro, textvariable=correo)  # ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_correo.pack()
    
    etiqueta_clave = Label(ventana_registro, text="Contraseña")
    etiqueta_clave.pack()
    
    entrada_clave = Entry(ventana_registro, textvariable=clave)  # ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=50, height=1, bg="DarkGrey", command=registro_usuario_u).pack()

def registro_usuario_u():

    usuario_info = entrada_nombre.get()
    apellido_info = entrada_apellido.get()
    telefono_info = entrada_telefono.get()
    correo_info = entrada_correo.get()
    clave_info = entrada_clave.get()
    
    columnas = ["Nombre", "Apellido", "Telefono", "Correo", "Clave"]
    datos = [usuario_info, apellido_info, telefono_info, correo_info, clave_info]
 
    filename = "usuarios.csv"
    usuarios = pd.read_csv(filename, header = 0)
    usuarios_act = usuarios.append(pd.Series(datos, index = usuarios.columns), ignore_index = True)
    usuarios_act.to_csv("usuarios.csv", index = False)
    
    Label(ventana_registro, text="Registro completado con éxito", fg="DarkGrey", font=("calibri", 11)).pack()
    
def registro_v():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro vendedores")
    ventana_registro.geometry("550x550")

    global entrada_nombre_negocio
    global entrada_correo_negocio
    global entrada_telefono_negocio
    global entrada_latitud_negocio
    global entrada_longitud_negocio
    global entrada_clave_negocio
    
    nombre_negocio = StringVar()
    correo_negocio = StringVar()
    telefono_negocio = IntVar()
    latitud = IntVar()
    longitud = IntVar()
    clave_negocio = StringVar()

    Label(ventana_registro, text="Introduzca datos", bg="DarkGrey", width="300", height="2").pack()
    Label(ventana_registro, text="").pack()
    
    etiqueta_nombre = Label(ventana_registro, text="Nombre del negocio")
    etiqueta_nombre.pack()
    
    entrada_nombre_negocio = Entry(ventana_registro, textvariable=nombre_negocio)
    entrada_nombre_negocio.pack()
    
    etiqueta_correo = Label(ventana_registro, text="Correo")
    etiqueta_correo.pack()
    
    entrada_correo_negocio = Entry(ventana_registro, textvariable=correo_negocio)
    entrada_correo_negocio.pack()
    
    etiqueta_telefono = Label(ventana_registro, text="Telefono")
    etiqueta_telefono.pack()
    
    entrada_telefono_negocio = Entry(ventana_registro, textvariable=telefono_negocio)
    entrada_telefono_negocio.pack()
    
    etiqueta_latitud = Label(ventana_registro, text="Latitud")
    etiqueta_latitud.pack()
    
    entrada_latitud_negocio = Entry(ventana_registro, textvariable=latitud)
    entrada_latitud_negocio.pack()
    
    etiqueta_longitud = Label(ventana_registro, text="Longitud")
    etiqueta_longitud.pack()
    
    entrada_longitud_negocio = Entry(ventana_registro, textvariable=longitud)
    entrada_longitud_negocio.pack()
    
    etiqueta_clave_negocio = Label(ventana_registro, text="Clave")
    etiqueta_clave_negocio.pack()
    
    entrada_clave_negocio = Entry(ventana_registro, textvariable=clave_negocio)
    entrada_clave_negocio.pack()
    
    Label(ventana_registro, text="para conocer las coordenadas, visite https://www.coordenadas-gps.com/").pack()
    Label(ventana_registro, text="").pack()
    
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=50, height=1, fg="DarkGrey", command=registro_usuario_v).pack()

def registro_usuario_v():

    nombre_negocio_info = entrada_nombre_negocio.get()
    correo_negocio_info = entrada_correo_negocio.get()
    telefono_negocio_info = entrada_telefono_negocio.get()
    latitud_info = entrada_latitud_negocio.get()
    longitud_info = entrada_longitud_negocio.get()
    clave_negocio_info = entrada_clave_negocio.get()

    identificador = format(id(nombre_negocio_info), "x")

    columnas = ["Identificador", "Nombre", "Correo", "Telefono", "Latitud", "Longitud", "Clave"]
    datos = [identificador, nombre_negocio_info, correo_negocio_info, telefono_negocio_info, latitud_info, longitud_info, clave_negocio_info]
    
    filename = "vendedores.csv"
    vendedores = pd.read_csv(filename, header = 0)
    vendedores_act = vendedores.append(pd.Series(datos, index = vendedores.columns), ignore_index = True)
    vendedores_act.to_csv("vendedores.csv", index = False)
    
    Label(ventana_registro, text="Registro completado con éxito", fg="DarkGrey", font=("calibri", 11)).pack()

def login_u():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("550x550")
    
    Label(ventana_login, text="Introduzca nombre del usuario y contraseña", width="100", height="2", bg="DarkGrey").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave_usuario
 
    verifica_usuario = StringVar()
    verifica_clave_usuario = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave_usuario
 
    Label(ventana_login, text="Nombre usuario").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    
    Label(ventana_login, text="Contraseña").pack()
    entrada_login_clave_usuario = Entry(ventana_login, textvariable=verifica_clave_usuario, show = "*")
    entrada_login_clave_usuario.pack()
    
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login_u).pack()

def login_v():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("550x550")
    
    Label(ventana_login, text="Introduzca nombre del negocio y contraseña", width="100", height="2", bg="DarkGrey").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_negocio
    global verifica_clave_negocio
 
    verifica_negocio = StringVar()
    verifica_clave_negocio = StringVar()
 
    global entrada_login_negocio
    global entrada_login_clave_negocio
 
    Label(ventana_login, text="Nombre negocio").pack()
    entrada_login_negocio = Entry(ventana_login, textvariable=verifica_negocio)
    entrada_login_negocio.pack()
    
    Label(ventana_login, text="Contraseña").pack()
    entrada_login_clave_negocio = Entry(ventana_login, textvariable=verifica_clave_negocio, show= '*')
    entrada_login_clave_negocio.pack()
    
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login_v).pack()

def verifica_login_u():
    usuario_1 = verifica_usuario.get()
    clave_1 = verifica_clave_usuario.get()
    
    entrada_login_usuario.delete(0, END)
    entrada_login_clave_usuario.delete(0, END)
    
    filename = "usuarios.csv"
    leer_usuarios = pd.read_csv(filename, header = 0)
    
    filtro = leer_usuarios.loc[(leer_usuarios["Nombre"] == usuario_1) & (leer_usuarios["Clave"] == clave_1)]
    filtro_existe = filtro.empty
    
    if filtro_existe is False:
        exito_login_u()
    else:
        no_login()
    
def verifica_login_v():
    
    global filtro
    global filtro_existe
    global id_vendedor
    
    negocio_1 = verifica_negocio.get()
    clave_1 = verifica_clave_negocio.get()
    
    entrada_login_negocio.delete(0, END)
    entrada_login_clave_negocio.delete(0, END)
    
    filename = "vendedores.csv"
    leer_vendedores = pd.read_csv(filename, header = 0)
    
    filtro = leer_vendedores.loc[(leer_vendedores["Nombre"] == negocio_1) & (leer_vendedores["Clave"] == clave_1)]
    filtro_existe = filtro.empty
    
    id_vendedor = filtro["Identificador"]
    
    if filtro_existe is False:
        exito_login_v()
    else:
        no_login()

def no_login():
    global ventana_no_login
    ventana_no_login = Toplevel(ventana_login)
    ventana_no_login.title("ERROR")
    ventana_no_login.geometry("500x100")
    Label(ventana_no_login, text="Contraseña incorrecta o el usuario no esta en nuestra base de datos").pack()

def exito_login_u():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()

def exito_login_v():
    
    def Seleccion_Combobox(event):
        categoria_producto.set("")
        categoria_producto.config(values = valores[entrada_comida_o_producto.get()])
    
    global ventana_publicar_productos
    ventana_publicar_productos = Toplevel(ventana_principal)
    ventana_publicar_productos.title("Publicar productos")
    ventana_publicar_productos.geometry("550x550")
    
    global entrada_alimento
    global descripcion_alimento
    global entrada_comida_o_producto
    global categoria_producto
    global entrada_fecha_caducidad
    global entrada_precio
    
    entrada_alimento = StringVar()
    descripcion_alimento = StringVar()
    entrada_precio = IntVar()
    
    valores = {
        "Comida": ("Asiatica", "Cafeteria", "Comida Rapida", "Saludables", "Casero"),
        "Productos": ("Lacteos", "Carnes", "Pescados", "Bebestibles", "Frutas", "Verduras", "Conservas", "Granos")
        }
    
    Label(ventana_publicar_productos, text="Introduzca datos", bg="DarkGrey", width="100", height="2").pack()
    Label(ventana_publicar_productos, text="Tu Id es :", bg="DarkGrey", width="100", height="2").pack()
    Label(ventana_publicar_productos, text=id_vendedor, bg="DarkGrey", width="100", height="2").pack()
    Label(ventana_publicar_productos, text="").pack()

    etiqueta_alimento = Label(ventana_publicar_productos, text = "Nombre del producto").pack()
    entrada_tk_alimento = Entry(ventana_publicar_productos, textvariable = entrada_alimento)
    entrada_tk_alimento.pack()
    
    etiqueta_descripcion = Label(ventana_publicar_productos, text = "Descripcion del producto").pack()
    entrada_tk_descripcion = Entry(ventana_publicar_productos, textvariable = descripcion_alimento)
    entrada_tk_descripcion.pack()
    
    etiqueta_alimento_o_produccion = Label(ventana_publicar_productos, text = "Alimento o Producto").pack()
    entrada_comida_o_producto = ttk.Combobox(ventana_publicar_productos, values = tuple(valores.keys()), state = "readonly")
    entrada_comida_o_producto.bind("<<ComboboxSelected>>", Seleccion_Combobox)
    entrada_comida_o_producto.pack()
    
    etiqueta_categoria = Label(ventana_publicar_productos, text = "Categoria").pack()
    categoria_producto = ttk.Combobox(ventana_publicar_productos, state = "readonly")
    categoria_producto.pack()
    
    etiqueta_precio = Label(ventana_publicar_productos, text = "Precio").pack()
    entrada_tk_precio = Entry(ventana_publicar_productos, textvariable = entrada_precio)
    entrada_tk_precio.pack()
    
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Publicar Producto", width=10, height=1, command = añadir_registro).pack()

def añadir_registro():
    nombre_1

ventana_inicio()



