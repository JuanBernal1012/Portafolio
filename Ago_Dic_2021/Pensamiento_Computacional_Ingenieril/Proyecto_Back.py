#Importación de las librerías para lectura de archivos y creación de gráficas.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Función que contiene el menú de inicio con las 6 preguntas detonantes.
def menu():
    print("-----------------------MENU----------------------------")
    print("1 -- Productos más vendidos") 
    print("2 -- Número de importes por establecimiento")
    print("3 -- Tipo de pago frecuente")
    print("4 -- Ventas promedio por día")
    print("5 -- Marca más vendida")
    print("6 -- Hora pico")
    print("7 -- Salir del menú")

#Función que despliega una gráfica con el número de ventas por producto    
def producto():
    tabla = pd.read_excel("superzarci2.xlsx")
    graf=tabla.groupby("DESCRIPCION", as_index=False).agg({"CANTIDAD": "sum"})
    produc=graf["DESCRIPCION"]
    ventas=graf["CANTIDAD"]
    productos = []
    cantidades = []
    for i in range(0,len(ventas)):
        if ventas[i]> np.mean(ventas):
            productos.append(produc[i])
            cantidades.append(ventas[i])
    barlist=plt.bar(productos, cantidades, color='red')
    plt.xlabel("Producto")
    plt.ylabel("Ventas")
    plt.title("Ventas por producto")
    plt.xticks(rotation=90)
    plt.show()
    print()
    print(f"La cantidad de ventas de los productos menos vendidos es {np.min(cantidades)} cada uno")

#Función que despliega una gráfica con el número de importes por comercio.
def importes():
    tabla = pd.read_excel("superzarci2.xlsx")
    pro=tabla.groupby("NOMBRE_COMERCIO", as_index=False).agg({"IMPORTE_TOTAL": "sum"})
    comercio=pro["NOMBRE_COMERCIO"]
    importe=pro["IMPORTE_TOTAL"]
    comer = []
    impor = []
    for i in range(0,len(importe)):
        if importe[i]> np.mean(importe):
            comer.append(comercio[i])
            impor.append(importe[i])
    barlist=plt.bar(comercio, importe, color='pink')
    plt.xlabel("Establecimiento")
    plt.ylabel("Importes totales")
    plt.title("Importes por establecimiento")
    plt.xticks(rotation=85)
    plt.show()
    print()
    print(f"La ganancia de ventas de Super S Mitras es ${np.max(impor)}")

#Función que despliega una gráfica de pastel de los tipos de pago.    
def tipo_pago():
    tabla = pd.read_excel("superzarci2.xlsx")
    resultado=tabla.groupby(["FORMA_PAGO"])["CANTIDAD"].count().reset_index()
    forma_pago= resultado["FORMA_PAGO"]
    cantidad=resultado["CANTIDAD"]
    fig, x=plt.subplots()
    x.pie(cantidad, labels=forma_pago, autopct='%1.1f%%', shadow=True, startangle=90)
    x.axis('equal')
    plt.title("Forma de pago más frecuente")
    plt.show()

#Función que despliega una gráfica de puntos de las ventas por día.
def ventas_dia():
    tabla = pd.read_excel("superzarci2.xlsx")
    resultado=tabla.groupby('DIA_SEMANA', as_index=False).agg({"IMPORTE_TOTAL": "sum"})
    dia=resultado["DIA_SEMANA"]
    ventas = resultado["IMPORTE_TOTAL"]
    dias = []
    vent = []
    for i in range(0,len(ventas)):
        if ventas[i]> np.mean(ventas):
            dias.append(dia[i])
            vent.append(ventas[i])
    plt.plot(dia, ventas, color="red", linestyle="--", marker="o")
    plt.title("Dia de la semana que se gana menos")
    plt.xlabel("Días")
    plt.ylabel("Ganancias")
    plt.xticks(rotation=45)
    plt.legend(['Ganancias por día'])
    plt.show()
    print()
    print(f"La ganancia aproximada de productos vendidos los martes es ${np.min(ventas)}")

#Función que despliega una gráfica de barras que representa las marcas más vendidas.
def marcas():
    tabla = pd.read_excel("superzarci2.xlsx")
    resultado=tabla.groupby(["MARCA"])["CANTIDAD"].count().reset_index()
    marca=resultado["MARCA"]
    cantidad=resultado["CANTIDAD"]
    marcas_mas_vendidos = []
    cantidades_mas_vendidas = []
    for i in range(0,len(cantidad)):
        if cantidad[i]> np.mean(cantidad):
            marcas_mas_vendidos.append(marca[i])
            cantidades_mas_vendidas.append(cantidad[i])
    barlist=plt.bar(marcas_mas_vendidos, cantidades_mas_vendidas, color="blue", edgecolor='black')
    plt.grid(color='gray', linestyle='--', linewidth=2, axis='y', alpha=0.2)
    plt.title("Ventas por marca")
    plt.xlabel("Marcas")
    plt.ylabel("Ventas")
    plt.xticks(rotation=45)
    plt.show()
    print()
    print(f"La cantidad de productos vendidos de la marca Coca Cola es {np.max(cantidades_mas_vendidas)}")
    
#Función que despliega una gráfica de líneas de las ventas por hora.
def graficaLinea():
    tabla = pd.read_excel("superzarci2.xlsx")
    resultado=tabla.groupby('HORA', as_index=False).agg({"CANTIDAD": "count"})
    horas=resultado["HORA"]
    cantidad= resultado["CANTIDAD"]
    plt.plot(horas, cantidad, color="blue", linestyle="--", marker="o")
    plt.title("Horas frecuentadas")
    plt.xlabel("Hora")
    plt.ylabel("Cantidad de ventas")
    plt.xticks(rotation=20)
    plt.legend(['Cantidad de ventas por hora'])
    plt.show()
    print("La hora pico es a las 14:00 y la hora menos concurrida es a las 7:00")

#Llamado de la función menú.
menu()

#Entrada del usuario para desplegar alguna opción del menú.
opc=int(input("Teclee la opción: "))

#Ciclo "while" para que el menú se despliegue después de mostrar alguna opción del menú.
while opc!=7:
    if opc==1:
        producto()
    elif opc==2:
        importes()
    elif opc==3:
        tipo_pago()
    elif opc==4:
        ventas_dia()
    elif opc==5:
        marcas()
    elif opc==6:
        graficaLinea()
    #Si el usuario elige una opción que no es valida y no es 7, se despliega un mensaje de error.
    else:
        print("Opción incorrecta")
    #Cada ciclo del While, se volverá a desplegar el menú para elegir alguna otra opción.
    menu()
    opc=int(input("Teclee la opción: "))
print("Adiós!!")