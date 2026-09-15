import tkinter as tk

# ==========================================
# 1. FUNCIONES (Se completarán más adelante)
# ==========================================
def borrar_valores():
    print("Botón presionado: Borrar valores")
    # aca limpiamos los Entry anashe

def calcular_cramer():
    print("Botón presionado: Calcular")
    # Aca tenemos que usar bloques try-except para validar datos y calcular x

def calcular_determinante():
    print("Botón presionado: Calcular det.")
    # calculamos el determinante de la dimensión seleccionada

def actualizar_dimension():
    dim = dimension_var.get()
    print(f"Dimensión cambiada a: {dim}x{dim}")
    #  habilitamos/deshabilitamos campos según la dimensión

# ==========================================
# 2. CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ==========================================
ventana = tk.Tk()
ventana.title("Resolución de sistemas de ecuaciones lineales mediante el método de Cramer")
ventana.geometry("450x350")
#la resolucion la tenemos que ver, no se ve muy bien

# ==========================================
# 3. VARIABLES DE CONTROL
# ==========================================
dimension_var = tk.IntVar(value=3) # Por defecto arranca en 3x3 xd

# ==========================================
# 4. CREACIÓN DE WIDGETS (INTERFAZ)
# ==========================================

# --- lado Izquierdo: Dimensión ---
frame_dim = tk.LabelFrame(ventana, text="Dimensión")
frame_dim.grid(row=0, column=0, padx=10, pady=10, sticky="n")# chat gpeteado, preguntale al chat

tk.Radiobutton(frame_dim, text="2 x 2", variable=dimension_var, value=2, command=actualizar_dimension).pack(anchor="w")
tk.Radiobutton(frame_dim, text="3 x 3", variable=dimension_var, value=3, command=actualizar_dimension).pack(anchor="w")
tk.Radiobutton(frame_dim, text="4 x 4", variable=dimension_var, value=4, command=actualizar_dimension).pack(anchor="w")

# --- lado Derecho: Matrices y Vectores ---
frame_matrices = tk.Frame(ventana)
frame_matrices.grid(row=0, column=1, padx=10, pady=10)

# Títulos de las columnas (A, b, x)
tk.Label(frame_matrices, text="A", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=4)
tk.Label(frame_matrices, text="b", font=("Arial", 10, "bold")).grid(row=0, column=5)
tk.Label(frame_matrices, text="x", font=("Arial", 10, "bold")).grid(row=0, column=6)

# Listas para guardar las referencias a los cuadros de texto 
entradas_A = []
entradas_b = []
entradas_x = []

# Bucle for para crear la grilla 4x4 de la Matriz A y los vectores b y x
for i in range(4):
    fila_A = []
    # Matriz A
    for j in range(4):
        entry_A = tk.Entry(frame_matrices, width=5)
        entry_A.grid(row=i+1, column=j, padx=2, pady=2)
        fila_A.append(entry_A)
    entradas_A.append(fila_A)
    
    # Separador visual vacío
    tk.Label(frame_matrices, text="   ").grid(row=i+1, column=4)
    
    # Vector b
    entry_b = tk.Entry(frame_matrices, width=5)
    entry_b.grid(row=i+1, column=5, padx=2, pady=2)
    entradas_b.append(entry_b)
    
    # Vector x (creo que va a serde solo lectura, pero lo creamos normal por ahora)
    entry_x = tk.Entry(frame_matrices, width=5, state="readonly")
    entry_x.grid(row=i+1, column=6, padx=2, pady=2)
    entradas_x.append(entry_x)

# --- parte de abajo: Botones y Textos ---
frame_inferior = tk.Frame(ventana)
frame_inferior.grid(row=1, column=0, columnspan=2, pady=10)

texto_ayuda = "Ayuda: el sistema de ecuaciones permite calcular A.x = b\nSe deben cargar los valores de A y b y luego,\nal calcular, se obtienen los valores de x"#aca solo puse el texto de ayuda, no se ve muy bien, hay que ver como ponerlo en varias lineas
tk.Label(frame_inferior, text=texto_ayuda, justify="center").grid(row=0, column=0, columnspan=3, pady=10)# esto es para que el texto de ayuda se vea centrado y en varias lineas

tk.Button(frame_inferior, text="Borrar valores", command=borrar_valores).grid(row=1, column=0, padx=5)# aca le puse el boton de borrar valores, que va a limpiar todos los entrys de la matriz A y el vector b
tk.Button(frame_inferior, text="Calcular", command=calcular_cramer).grid(row=1, column=1, padx=5)#  le puse el boton de calcular, que va a calcular los valores de x usando el metodo de cramer

tk.Label(frame_inferior, text="Determinante:").grid(row=2, column=0, sticky="e", pady=10)
entry_det = tk.Entry(frame_inferior, width=10, state="readonly")
entry_det.grid(row=2, column=1, sticky="w")
tk.Button(frame_inferior, text="Calcular det.", command=calcular_determinante).grid(row=2, column=2, padx=5)

# Bucle principal de la aplicación
ventana.mainloop()
#IMPORTANTE: No se puede usar el metodo de cramer si el determinante es 0, hay que poner un mensaje de error en ese caso
# tambien hayq ue verificar el valor de la entrada de la matriz A y el vector b, si no son numeros hay que poner un mensaje de error
#tyambien necesitamos un mensaje de error si el sistema no tiene solucion o tiene infinitas soluciones, eso se puede verificar con el determinante y el rango de la matriz A y la matriz aumentada [A|b]
#Todavia no se implemento la parte de calcular el determinante, eso se puede hacer con numpy o con una funcion recursiva que calcule el determinante de una matriz, SUERTE JAVOOOOOOOO