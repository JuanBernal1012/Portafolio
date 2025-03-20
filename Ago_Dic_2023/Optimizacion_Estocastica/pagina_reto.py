import flet as ft
import numpy as np
import pandas as pd
from numpy.linalg import eig, inv

# # global cliente_material 
# cliente_material = {1234: ["A", "B", "C", "D"],0:"Error"}
# import os
# directorio_actual = os.path.dirname("pagina_reto.py")  # __file__ representa el archivo actual
# # print(directorio_actual)
# ruta_relativa = os.path.join('Tec','Optimización /','Reto', 'Markov_Chains', 'tec_estocasticos.parquet')
# ruta_completa = os.path.abspath(os.path.join(directorio_actual, ruta_relativa))
# ruta_completa
# df = pd.read_parquet(r"f:\Users\Admin\Documents\Programas\Tec\Quinto\Optimización estócastica\Reto\Markov_Chains\tec_estocasticos.parquet")
# df_filtered = df
# df_filtered['periodo'] = pd.to_datetime(df_filtered['periodo'])
# df_filtered.dropna(subset=['cliente_id'], inplace=True)

def recomendacion(cliente):
    if cliente not in cliente_material:
        cliente_material[cliente]=[]
        
        # Ordenar el DataFrame por la columna 'Date'
        df_sorted = df_filtered.sort_values(by='periodo')

        materiales = df_sorted[df_sorted["cliente_id"]==cliente]['material_id'].unique()
        for material_id in materiales:
            filtered_df = df_sorted[df_sorted['material_id'] == material_id]

            # Obtener las fechas únicas y clientes únicos para el material filtrado
            fechas_unicas = filtered_df['periodo'].unique()
            clientes_unicos = filtered_df['cliente_id'].unique()

            nuevas_filas = []

            # Crear todas las combinaciones posibles para el material filtrado
            for fecha in fechas_unicas:
                # for cliente in clientes_unicos:
                comprado = "comprado" if ((filtered_df['periodo'] == fecha) & (filtered_df['cliente_id'] == cliente)).any() else "no comprado"
                nuevas_filas.append({'periodo': fecha, 'cliente_id': cliente, 'material_id': material_id, 'comprado': comprado})

            # Crear un nuevo DataFrame con las combinaciones
            nuevo_df = pd.DataFrame(nuevas_filas)

            # Ordena primero por cliente_id, luego por material_id y finalmente por periodo.
            df = nuevo_df.sort_values(by=['cliente_id', 'material_id', 'periodo'])

            # Si quieres restablecer los índices del DataFrame después de ordenarlo.
            df = df.reset_index(drop=True)

            rating_categories = ['comprado','no comprado']

            # Crear una nueva columna que represente la categoría de rating siguiente
            df['nextcomprado'] = df['comprado'].shift(-1)

            # Calcular la matriz de transición  
            P = pd.crosstab(df['comprado'], df['nextcomprado'], normalize='index')
            client_data = df[df['cliente_id'] == cliente]
            last_comprado_value = client_data['comprado'].iloc[-1]
            if client_data['comprado'].iloc[:-1].all():
                if last_comprado_value == "comprado":
                    res = np.array([[1.0, 0.0]])
                else:
                    res = np.array([[0.0, 1.0]])
            else:
                Lambda, Q = eig(P)
                Q_1 = inv(Q)
                Lambda_20 = Lambda**2000000
                P_20 = np.matmul(np.matmul(Q, Lambda_20), Q_1)
                res = P_20.round(decimals = 4)
            if res[0][0] > res[0][1]:
                cliente_material[cliente].append(material_id)
    return cliente_material[cliente], len(cliente_material[cliente])

def my_app(page: ft.Page):
    page.title = "Recomendador de materiales"

    def search():
        t.value = "Buscando..."
        page.update()
        cliente = int(material_field.value)
        materiales, cantidad_recomendaciones = recomendacion(cliente)
        t.value = "{} recomendaciones encontradas\nMateriales recomendados para el cliente {}:\n{}".format(cantidad_recomendaciones ,cliente,materiales)
        page.update()

    def button_click(e):
        search()
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key=="Enter":
            search()
    
    material_field = ft.TextField(label = "Cliente a buscar:",
                 hint_text="Escribe el código del cliente")
    page.on_keyboard_event = on_keyboard

    t = ft.Text()
    search_button = ft.ElevatedButton(text="Buscar", on_click=button_click)
    
    
    page.add(
        ft.Row([
            ft.Column([material_field,
                  search_button],alignment="center")]),
        ft.Row([ft.Column([t],alignment="center", width=page.window_width*0.8)]
        ))

ft.app(target = my_app)
