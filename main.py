#FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
#SECCIÓN DEL CURSO: 0-L-38
#PROFESOR DE TEORÍA: LUCIANO HIDALGO - JAVIER SALAZAR - LINDA MUÑOZ
#GRUPO: 1
#INTEGRANTES:
#1.CRISTIAN ALVARADO 21.309.006-2
#2. SARAHY ASTETE 21.243.827-8
#3. NICOLÁS CUEVAS 20.794.067-4
#4. YELNNIE GARRIDO 21.496.814-2
#5. ANAHIS GONZÁLEZ 21.326.120-7
#6. TOMÁS PAINEPI 21.573.280-0
#7. ANTONIO VALDIVIA 21.549.091-2
#DESCRIPCIÓN DEL PROGRAMA: EN ESTA PARTE DEL CÓDIGO SE MUESTRA LA ENTRADA DE DATOS, DONDE EL USUARIO PODRÁ CREAR SU CUENTA
#RESPECTO A SUS DATOS O SU NEGOCIO.

#IMPORTACIÓN DE MÓDULOS

from tkinter import *
from tkinter import ttk
import webbrowser
import pandas as pd
import csv

#BLOQUE PRINCIPAL

#BLOQUE DE DEFINICIONES

#INFORMACIÓN EN LA PANTALLA DE INICIO

def ventana_inicio():
    
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal = Tk()
    ventana_principal.geometry("550x550") # DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login") # TITULO DE LA VENTANA
    
    Label(text="Escoja una opción", bg=pestas_color, width="300", height="2",
          font=("Calibri", 13)).pack() # ETIQUETA CON TEXTO

    Label(text="").pack()
    Button(text="Acceder", height="2", width="60", bg=pestas_color, command=login_u).pack()  # BOTÓN "Acceder"
    
    Label(text="").pack()
    Button(text="Acceso ventas", height="2", width="60", bg=pestas_color, command=login_v).pack()  # BOTÓN "Acceder"
    
    Label(text="").pack()
    Button(text="Registrarse como usuario", height="2", width="60", bg=pestas_color, command=registro_u).pack()  # BOTÓN "Registrarse".
    
    Label(text="").pack()
    Button(text="Registrarse como vendedor", height="2", width="60", bg=pestas_color, command=registro_v).pack()  # BOTÓN "Registrarse".
    
    Label(text="").pack()
    Label(text="Grupo 1, App Limos", width="300", height="2", font=("Calibri", 11)).pack() #TIPO DE TIPOGRAFIA Y DIMENSIÓN DEL TÍTULO
    ventana_principal.mainloop()

#GUARDAR LA VARIABLE DE VENTANA

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
    
    # TIPO DE VARIABLES Y SU ALAMCENAMIENTO
    
    nombre_usuario = StringVar()
    apellido_usuario = StringVar()
    telefono = IntVar()
    correo = StringVar()
    clave = StringVar()
    
    Label(ventana_registro, text="Introduzca datos", bg="DarkGrey", width="300", height="2").pack()
    Label(ventana_registro, text="").pack() # INTRODUCIR DATOS PERSONALES DEL USUARIO
    
    etiqueta_nombre = Label(ventana_registro, text="Nombre")
    etiqueta_nombre.pack()
    
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) # ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    
    etiqueta_apellido = Label(ventana_registro, text="Apellido")
    etiqueta_apellido.pack()
    
    entrada_apellido = Entry(ventana_registro, textvariable=apellido_usuario) # ESPACIO PARA INTRODUCIR EL APELLIDO.
    entrada_apellido.pack()
    
    etiqueta_telefono = Label(ventana_registro, text="Telefono")
    etiqueta_telefono.pack()
    
    entrada_telefono = Entry(ventana_registro, textvariable=telefono) # ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_telefono.pack()
    
    etiqueta_correo = Label(ventana_registro, text="Correo Electronico")
    etiqueta_correo.pack()
    
    entrada_correo = Entry(ventana_registro, textvariable=correo) # ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_correo.pack()
    
    etiqueta_clave = Label(ventana_registro, text="Contraseña")
    etiqueta_clave.pack()
    
    entrada_clave = Entry(ventana_registro, textvariable=clave) # ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=50, height=1, bg="DarkGrey", command=registro_usuario_u).pack() # BOTON REGISTRO

def registro_usuario_u():

    usuario_info = entrada_nombre.get()
    apellido_info = entrada_apellido.get()
    telefono_info = entrada_telefono.get()
    correo_info = entrada_correo.get()
    clave_info = entrada_clave.get()
    
    # ESTRUCTURA APPEND
    
    columnas = ["Nombre", "Apellido", "Telefono", "Correo", "Clave"]
    datos = [usuario_info, apellido_info, telefono_info, correo_info, clave_info]

    # CREACIÓN, ALMACENAJE Y DESCARGA DEL CSV DE USUARIOS
    
    filename = "usuarios.csv"
    usuarios = pd.read_csv(filename, header = 0)
    usuarios_act = usuarios.append(pd.Series(datos, index = usuarios.columns), ignore_index = True)
    usuarios_act.to_csv("usuarios.csv", index = False)
    
    Label(ventana_registro, text="Registro completado con éxito", fg="DarkGrey", font=("calibri", 11)).pack() # MENSAJE VERIFICACIÓN DEL REGISTRO

# VENTANA DEL REGISTRO DE VENDEDORES      

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

    Label(ventana_registro, text="Introduzca datos", bg="DarkGrey", width="300", height="2").pack() # INTRODUCIR DATOS PERSONALES
    Label(ventana_registro, text="").pack()
    
    etiqueta_nombre = Label(ventana_registro, text="Nombre del negocio") # LABEL INDICACIÓN TITULO
    etiqueta_nombre.pack()
    
    entrada_nombre_negocio = Entry(ventana_registro, textvariable=nombre_negocio)#ESPACIO PARA INTRODUCIR NOMBRE DEL NEGOCIO
    entrada_nombre_negocio.pack()
    
    etiqueta_correo = Label(ventana_registro, text="Correo")#ESPACIO PARA INTRODUCIR CORREO
    etiqueta_correo.pack()
    
    entrada_correo_negocio = Entry(ventana_registro, textvariable=correo_negocio)
    entrada_correo_negocio.pack()
    
    etiqueta_telefono = Label(ventana_registro, text="Telefono") #ESPACIO PARA INTRODUCIR EL TELEFONO

    etiqueta_telefono.pack()
    
    entrada_telefono_negocio = Entry(ventana_registro, textvariable=telefono_negocio)
    entrada_telefono_negocio.pack()
    
    # SE DEBE CONOCER LA UBICACIÓN DEL VENDEDOR PARA QUE SE PUEDA POSTERIORMENTE ABRIR SU UBICACION
    
    etiqueta_latitud = Label(ventana_registro, text="Latitud")
    etiqueta_latitud.pack()
    
    entrada_latitud_negocio = Entry(ventana_registro, textvariable=latitud) # ESPACIO PARA INTRODUCIR UBICACIÓN(LATITUD)
    entrada_latitud_negocio.pack()
    
    etiqueta_longitud = Label(ventana_registro, text="Longitud")
    etiqueta_longitud.pack()
    
    entrada_longitud_negocio = Entry(ventana_registro, textvariable=longitud) # ESPACIO PARA INTRODUCIR UBICACIÓN(LONGITUD)
    entrada_longitud_negocio.pack()
    
    etiqueta_clave_negocio = Label(ventana_registro, text="Clave")
    etiqueta_clave_negocio.pack()
    
    entrada_clave_negocio = Entry(ventana_registro, textvariable=clave_negocio) # ESPACIO PARA LA CLAVE DEL NEGOCIO
    entrada_clave_negocio.pack()
    
    Label(ventana_registro, text="").pack()
    
    Label_Link = ttk.Label(ventana_registro, text="para conocer las coordenadas, visite aqui", foreground="DodgerBlue3")
    Label_Link.pack()
    Label_Link.bind("<Button-1>", LinkCoordenada)
    Label(ventana_registro, text="").pack()
    
    Button(ventana_registro, text="Registrarse", width=50, height=1, fg="DarkGrey", command=registro_usuario_v).pack()

def LinkCoordenada(ev):
    
    webbrowser.open_new("https://www.coordenadas-gps.com/") # AYUDA PARA DEFINIR LAS COORDENADAS DEL VENDEDOR

def registro_usuario_v():
    
    # OBTENCIÓN DE DATOS
    
    nombre_negocio_info = entrada_nombre_negocio.get()
    correo_negocio_info = entrada_correo_negocio.get()
    telefono_negocio_info = entrada_telefono_negocio.get()
    latitud_info = entrada_latitud_negocio.get()
    longitud_info = entrada_longitud_negocio.get()
    clave_negocio_info = entrada_clave_negocio.get()

    identificador = format(id(nombre_negocio_info), "x")

    columnas = ["Identificador", "Nombre", "Correo", "Telefono", "Latitud", "Longitud", "Clave"]
    datos = [identificador, nombre_negocio_info, correo_negocio_info, telefono_negocio_info, latitud_info, longitud_info, clave_negocio_info]

    # CREAR ARCHIVO CSV DE VENDEDORES
    
    filename = "vendedores.csv"
    vendedores = pd.read_csv(filename, header = 0)
    vendedores_act = vendedores.append(pd.Series(datos, index = vendedores.columns), ignore_index = True)
    vendedores_act.to_csv("vendedores.csv", index = False)
    
    # INICIO DE SESIÓN USUARIO
    
    Label(ventana_registro, text="Registro completado con éxito", fg="DarkGrey", font=("calibri", 11)).pack()

def login_u():
    
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("550x550")
    
    # ACCESO A LA CUENTA CREADA
    
    Label(ventana_login, text="Introduzca nombre del usuario y contraseña", width="100", height="2", bg="DarkGrey").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave_usuario
 
    verifica_usuario = StringVar()
    verifica_clave_usuario = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave_usuario
    
    # DATOS A RELLENAR SEGÚN CORRESPONDA
    
    Label(ventana_login, text="Nombre usuario").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    
    Label(ventana_login, text="Contraseña").pack()
    entrada_login_clave_usuario = Entry(ventana_login, textvariable=verifica_clave_usuario, show = "*")
    entrada_login_clave_usuario.pack()
    
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login_u).pack() # TERMINAR EL INICIO DE SESIÓN
    
#INICIO DE SESIÓN DEL VENDEDOR
    
def login_v():
    
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("550x550")
    
    # ACCESO A LA CUENTA DEL NEGOCIO DEL VENDEDOR
     
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

# VERIFICACIÓN DEL INICIO DE LOS USUARIOS

def verifica_login_u():
    
    usuario_1 = verifica_usuario.get()
    clave_1 = verifica_clave_usuario.get()
    
    entrada_login_usuario.delete(0, END)
    entrada_login_clave_usuario.delete(0, END)
    
    # CREAR ARCHIVO CSV DE LOS USUARIOS
    
    filename = "usuarios.csv"
    leer_usuarios = pd.read_csv(filename, header = 0)

    # LECTURA DE LOS DATOS DEL USUARIO
    
    filtro = leer_usuarios.loc[(leer_usuarios["Nombre"] == usuario_1) & (leer_usuarios["Clave"] == clave_1)]
    filtro_existe = filtro.empty

    # CORROBORACIÓN DE SI EXISTE O NO LOS DATOS ENTREGADOS POR EL USUARIO
    
    if filtro_existe is False:
        exito_login_u()
    else:
        no_login()

def verifica_login_v():
    
    global id_vendedor
    global filtro
    
    # VERIFICACIÓN DEL NEGOCIO Y SU CLAVE DE INGRESO
    
    negocio_1 = verifica_negocio.get()
    clave_1 = verifica_clave_negocio.get()
    
    entrada_login_negocio.delete(0, END)
    entrada_login_clave_negocio.delete(0, END)
    
    # CREAR ARCHIVO CSV DE LOS VENDEDORES
    
    filename = "vendedores.csv"
    leer_vendedores = pd.read_csv(filename, header = 0)
    
    # LEER LOS DATOS ENTREGADOS POR LOS VENDEDORES
    
    filtro = leer_vendedores.loc[(leer_vendedores["Nombre"] == negocio_1) & (leer_vendedores["Clave"] == clave_1)]
    filtro = filtro.reset_index()
    filtro_existe = filtro.empty
    
    id_vendedor = filtro.loc[0]["Identificador"]
    
    # VERIFICAR SI EXISTEN LOS DATOS EN EL SISTEMA ENTREGADOS POR EL VENDEDOR
    
    if filtro_existe is False:
        exito_login_v()
    else:
        no_login()

# CASO DE INICIACIÓN DE SESIÓN CON ERROR

def no_login():
    
    global ventana_no_login
    ventana_no_login = Toplevel(ventana_login)
    ventana_no_login.title("ERROR") # SE SEÑALARÁ QUE LA APLICACIÓN DETECTA UN ERROR
    ventana_no_login.geometry("550x100")
    Label(ventana_no_login, text="Contraseña incorrecta o el usuario no esta en nuestra base de datos").pack() # MENSAJE DE AVISO

# CASO DE INICIACION DE SESIÓN DEL USUARIO EXITOSA

def exito_login_u():
    
    global ventana_productos
    global leer_vendedores
    global filtro_vendedor
    global index_buscar
    
    ventana_productos = Toplevel(ventana_principal)
    ventana_productos.title("Ver productos")
    ventana_productos.geometry("550x550")
    
    filename = "vendedores.csv"
    leer_vendedores = pd.read_csv(filename, header = 0)
    
    valores = leer_vendedores["Nombre"]
    valores_lista = valores.tolist()
    
    Label(ventana_productos, text = "").pack()
    Label(ventana_productos, text = "Busque el nombre del negocio").pack()
    index_buscar = ttk.Combobox(ventana_productos, values = valores_lista, state = "readonly")
    index_buscar.pack()
    
    def mostrar_producto():
        
    # MUESTRA PRODUCTO POR PANTALLA
    
        global filtro_vendedor
        global nombre_vendedor
        global correo_vendedor
        global telefono_vendedor
        global direccion_vendedor
        global identificador_vendedor
        
        global latitud_vendedor
        global longitud_vendedor
        
        ventana_productos_mostrar = Toplevel(ventana_principal)
        ventana_productos_mostrar.title("Ver productos")
        ventana_productos_mostrar.geometry("550x750")
        
        nombre_negocio_sel = index_buscar.get()
        
        filename = "vendedores.csv"
        lectura_vendedores = pd.read_csv(filename, header = 0)
        
        filtro_vendedor = lectura_vendedores.loc[lectura_vendedores["Nombre"] == nombre_negocio_sel]
        filtro_vendedor.reset_index(drop=True, inplace=True)
        
        latitud_vendedor = filtro_vendedor.loc[0]["Latitud"]
        longitud_vendedor = filtro_vendedor.loc[0]["Longitud"]
        
        nombre_vendedor = filtro_vendedor.loc[0]["Nombre"]
        correo_vendedor = filtro_vendedor.loc[0]["Correo"]
        telefono_vendedor = filtro_vendedor.loc[0]["Telefono"]
        direccion_vendedor = vinculo_maps
        identificador_vendedor = filtro_vendedor.loc[0]["Identificador"]
        
    # DATOS DE LA VENTANA 
    
        Label(ventana_productos_mostrar, text = "").pack()
        Label(ventana_productos_mostrar, text = "Nombre: ").pack()
        Label(ventana_productos_mostrar, text = nombre_vendedor).pack()
        Label(ventana_productos_mostrar, text = "").pack()
        Label(ventana_productos_mostrar, text = "Correo: ").pack()
        Label(ventana_productos_mostrar, text = correo_vendedor).pack()
        Label(ventana_productos_mostrar, text = "").pack()
        Label(ventana_productos_mostrar, text = "Telefono: ").pack()
        Label(ventana_productos_mostrar, text = telefono_vendedor).pack()
        Label(ventana_productos_mostrar, text = "").pack()
        Label(ventana_productos_mostrar, text = "Direccion: ").pack()
        
        LabelDir = ttk.Label(ventana_productos_mostrar, text = "Direccion en Maps", foreground="DodgerBlue3")
        LabelDir.pack()

        LabelDir.bind("<Button-1>", vinculo_maps)
        
        frame1 = ttk.LabelFrame(ventana_productos_mostrar, text="Productos Disponibles")
        frame1.place(height=300, width=500, x=25, y=400)

        tv1 = ttk.Treeview(frame1)
        tv1.place(relheight=1, relwidth=1)
        
    # ORIENTACIÓN
    
        treescrolly = ttk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
        treescrollx = ttk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")
        
        def Act_DB():
            
            file_path = "productos_vendedor.csv"
            
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)

            clear_data()
            tv1["column"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)

            df_rows = df.to_numpy().tolist()
            for row in df_rows:
                tv1.insert("", "end", values=row)
            return None

        def clear_data():
            tv1.delete(*tv1.get_children())
            return None
        
        base_vendedor()
        vinculo_maps()
        Act_DB()
        
    Label(ventana_productos, text = "").pack()
    Button(ventana_productos, text="Buscar productos", width=20, height=1, command = mostrar_producto).pack()
    
    def base_vendedor():
        
    # AL INGRESAR NOMBRE DE VENDEDOR APARECEN TODOS LOS PRODUCTOS DE ÉL
    
        global identificador_base
        global productos_venta_id
    
        identificador_base = identificador_vendedor   
        
        filename = "productos.csv"
        productos_venta = pd.read_csv(filename, header = 0)
        productos_venta_id = productos_venta[productos_venta["Identificador"] == identificador_base]
        productos_venta_id.to_csv("Productos_vendedor.csv", index = False)
    
def vinculo_maps():
    
# LOCALIZACIÓN DEL NEGOCIO

    global latitud_link
    global longitud_link
    global vinculo_dir

    latitud_link = str(latitud_vendedor)
    longitud_link = str(longitud_vendedor)
    
    vinculo_dir = "https://maps.google.com/?q=" + latitud_link + "," + longitud_link
    webbrowser.open_new(vinculo_dir)

def exito_login_v():
    
    # CASO DE INICIACIÓN DE SESIÓN DEL VENDEDOR EXITOSO
    
    def Seleccion_Combobox(event):
        categoria_producto.set("")
        categoria_producto.config(values = valores[entrada_comida_o_producto.get()])#CATEGORIAS DE LOS PRODUCTOS
    
    global ventana_publicar_productos#VENTANA ESPECIFICA PARA QUE EL VENDEDOR PUBLIQUE SUS ALIMENTOS
    ventana_publicar_productos = Toplevel(ventana_principal)
    ventana_publicar_productos.title("Publicar productos")
    ventana_publicar_productos.geometry("550x550")
    
    # VARIABLES QUE CAMBIAN SEGUN LA INDICACIÓN DEL VENDEDOR
    
    global entrada_alimento
    global descripcion_alimento
    global entrada_comida_o_producto
    global categoria_producto
    global entrada_fecha
    global entrada_precio
    global entrada_cantidad
    
    entrada_alimento = StringVar()
    descripcion_alimento = StringVar()
    entrada_precio = IntVar()
    entrada_cantidad = IntVar()
    entrada_fecha = StringVar()
    
    valores = {
        "Comida": ("Asiatica", "Cafeteria", "Comida Rapida", "Saludables", "Casero"),
        "Productos": ("Lacteos", "Carnes", "Pescados", "Bebestibles", "Frutas", "Verduras", "Conservas", "Granos")
        }
    
    #CATEGORIAS DE LOS ALIMENTOS
    
    Label(ventana_publicar_productos, text="Introduzca datos", bg="DarkGrey", width="100", height="2").pack()
    Label(ventana_publicar_productos, text="Tu Id es :", bg="DarkGrey", width="100", height="2").pack()
    Label(ventana_publicar_productos, text=id_vendedor, bg="DarkGrey", width="100", height="2").pack()
    Label(ventana_publicar_productos, text="").pack()
    
    # ESPACIOS A RELLENAR SEGÚN LA INFORMACIÓN QUE BRINDE EL VENDEDOR
    
    etiqueta_alimento = Label(ventana_publicar_productos, text = "Nombre del producto").pack()
    entrada_tk_alimento = Entry(ventana_publicar_productos, textvariable = entrada_alimento, width = 60)
    entrada_tk_alimento.pack()
    
    # ESPECIFICACIÓN DE ALIMENTO O PRODUCTO QUE DESPLEGA UNA LISTA
    
    etiqueta_descripcion = Label(ventana_publicar_productos, text = "Descripcion del producto").pack()
    entrada_tk_descripcion = Entry(ventana_publicar_productos, textvariable = descripcion_alimento, width = 60)
    entrada_tk_descripcion.pack()
    
    etiqueta_alimento_o_produccion = Label(ventana_publicar_productos, text = "Alimento o Producto").pack()
    entrada_comida_o_producto = ttk.Combobox(ventana_publicar_productos, values = tuple(valores.keys()), state = "readonly", width = 60)
    entrada_comida_o_producto.bind("<<ComboboxSelected>>", Seleccion_Combobox)
    entrada_comida_o_producto.pack()
    
    # ESPECIFICACION DE LA CATEGORIA DEL ALIMENTO O PRODUCTO
    
    etiqueta_categoria = Label(ventana_publicar_productos, text = "Categoria").pack()
    categoria_producto = ttk.Combobox(ventana_publicar_productos, state = "readonly", width = 60)
    categoria_producto.pack()
    
    # VALOR DEL PRODUCTO GENERAL
    
    etiqueta_precio = Label(ventana_publicar_productos, text = "Precio").pack()
    entrada_tk_precio = Entry(ventana_publicar_productos, textvariable = entrada_precio, width = 60)
    entrada_tk_precio.pack()
    
    # VALOR DE LA CANTIDAD
    
    etiqueta_cantidad = Label(ventana_publicar_productos, text = "Cantidad").pack()
    entrada_tk_cantidad = Entry(ventana_publicar_productos, textvariable = entrada_cantidad, width = 60)
    entrada_tk_cantidad.pack()
    
    # ESPECIFICACION  CADUCIDAD
    
    etiqueta_fecha = Label(ventana_publicar_productos, text = "Fecha Vencimiento (dd/mm/aaaa)").pack()
    entrada_tk_fecha = Entry(ventana_publicar_productos, textvariable = entrada_fecha, width = 60)
    entrada_tk_fecha.pack()
    
    # PROCESO DE PUBLICACIÓN DEL PRODUCTO
    
    Label(ventana_publicar_productos, text="").pack()
    Button(ventana_publicar_productos, text="Publicar Producto", width=30, height=1, command = añadir_registro).pack()

    # PROCESO DE VER EL PRODUCTO
    
    Label(ventana_publicar_productos, text="").pack()
    Button(ventana_publicar_productos, text="Ver Alimentos", width=30, height=1, command = base_producto).pack()
    
def añadir_registro():
    
    # OBTENCIÓN DE DATOS
    
    global productos_act
    global categoria_info
    
    entrada_alimento_info = entrada_alimento.get()
    descripcion_alimento_info = descripcion_alimento.get()
    alimento_o_producto_info = entrada_comida_o_producto.get()
    categoria_info = categoria_producto.get()
    entrada_precio_info = entrada_precio.get()
    entrada_cantidad_info = entrada_cantidad.get()
    entrada_fecha_info = entrada_fecha.get()
    
    identificador_producto_info = format(id(entrada_alimento_info), "x")
    
    # CARACTERÍSTICAS DE LOS PRODUCTOS
    
    columnas = ["Identificador", "Identificador Producto", "Nombre", "Descripcion", "Tipo de Producto", "Categoria", "Precio", "Cantidad", "Fecha"]
    datos = [id_vendedor, identificador_producto_info, entrada_alimento_info, descripcion_alimento_info, alimento_o_producto_info, categoria_info, entrada_precio_info, entrada_cantidad_info, entrada_fecha_info]
    
    # LEER ARCHIVO CSV DE LOS PRODUCTOS 
    
    filename = "productos.csv"
    productos = pd.read_csv(filename, header = 0)
    productos_act = productos.append(pd.Series(datos, index = productos.columns), ignore_index = True)
    productos_act.to_csv("productos.csv", index = False)
    
    # VERIFICACIÓN DEL PROCESO COMPLETO DEL PRODUCTO
    
    Label(ventana_publicar_productos, text="Producto completado con éxito", fg="DarkGrey", font=("calibri", 11)).pack()

# INFORMACIÓN ESPECIFICA SOBRE LOS PRODUCTOS DE UNA FORMA MÁS VISUAL

def base_producto():
    
    # FUNCION PARA BORRAR PRODUCTOS
    
    def Eliminar_producto():
        
        # FUNCION PARA ELIMINAR TODO DEL PRODUCTO
        
        global ventana_eliminar
        global Index_dato
        global valores_lista
        global Dato_eliminar
        global valores
        
        ventana_eliminar = Toplevel(ventana_login)
        ventana_eliminar.title("Eliminar productos")
        ventana_eliminar.geometry("250x250")
        
        valores = productos_filtro_id["Identificador Producto"]
        valores_lista = valores.tolist()
        
        Label(ventana_eliminar, text="").pack()
        Label(ventana_eliminar, text="Introduzca el id producto a eliminar").pack()
        Label(ventana_eliminar, text="").pack()
        Dato_eliminar = ttk.Combobox(ventana_eliminar, values = valores_lista, state = "readonly")
        Dato_eliminar.pack()
        Label(ventana_eliminar, text="").pack()
        button_e = ttk.Button(ventana_eliminar, text = "Eliminar", command = Eliminar_base).pack()
    
    #FUNCION PARA ELIMINAR TODO DEL PRODUCTO DESDE ARCHIVO CSV
    def Eliminar_base():
        
        global Index_dato
        global Index_borrar
        
        global productos_delete
        global productos_delete_borrar
        
        Index_dato = Dato_eliminar.get()
        
        filename = "productos.csv"
        productos_delete = pd.read_csv(filename, header = 0)
        
        Index_borrar = productos_delete[productos_delete["Identificador Producto"] == Index_dato].index
        productos_delete_borrar = productos_delete.drop(Index_borrar, axis = 0)
        productos_delete_borrar.to_csv("productos.csv", index = False)
        
        # FUNCION DE FILTROS 
        
    def Act_DB():
        
        file_path = "productos_filtro.csv"
        
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)

        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tv1.insert("", "end", values=row)
        return None

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None

    global ventana_base
    global productos_filtro_id
    
    filename = "productos.csv"
    productos_filtro = pd.read_csv(filename, header = 0)
    productos_filtro_id = productos_filtro[productos_filtro["Identificador"] == id_vendedor]
    productos_filtro_id.to_csv("Productos_filtro.csv", index = False)
    
    ventana_base = Toplevel(ventana_login)
    ventana_base.geometry("550x550")
    ventana_base.title("Base de Productos")
    
    # MOSTRAR LOS PRODUCTOS DISPONIBLES
    
    frame1 = ttk.LabelFrame(ventana_base, text="Productos Disponibles")
    frame1.place(height=450, width=550)

    file_frame = ttk.LabelFrame(ventana_base)
    file_frame.place(height=100, width=550, rely=0.8, relx=0)
    
    # DATOS DEL PRODUCTO

    button = ttk.Button(file_frame, text="Ver Datos", command = lambda:Act_DB())
    button.place(rely=0.65, relx=0.50)
    
    button = ttk.Button(file_frame, text="Eliminar", command = Eliminar_producto)
    button.place(rely=0.65, relx=0.30)

    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1)
    
    # ORIENTACIÓN
    
    treescrolly = ttk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
    treescrollx = ttk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")


# PROCESAMIENTO
    
ventana_inicio()