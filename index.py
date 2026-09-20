# Laboratio N°4 - Informatica II
# Eberle Javier - Iñiguez Agustin 
# https://github.com/GlobHD/Labo4.git
# NOTA: Este programa requiere la librería externa Numpy. 
# Para instalarla ejecute en consola: pip install numpy
# Falta completar la parte de calcular el determinante y el metodo de cramer

import numpy as np 
import tkinter as tk
from tkinter import messagebox


def borrar_valores():
    # 1. Limpiar todos los campos de la Matriz A
    for fila in entradas_A:
        for entry in fila:
            entry.delete(0, tk.END)
            
    # 2. Limpiar todos los campos del vector b
    for entry in entradas_b:
        entry.delete(0, tk.END)
        
    # 3. Limpiar los campos del vector x
    for entry in entradas_x:
        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
        entry.config(state="readonly")
        
    # 4. Limpiar el campo del determinante
    entry_det.config(state=tk.NORMAL)
    entry_det.delete(0, tk.END)
    entry_det.config(state="readonly")

def calcular_cramer():
    print("Botón presionado: Calcular")
    dim = dimension_var.get()
    
    try:
        matriz_A = np.zeros((dim, dim))
        vector_b = np.zeros(dim)
        
        # 1. Leer Matriz A y Vector b
        for i in range(dim):
            vector_b[i] = float(entradas_b[i].get())
            for j in range(dim):
                matriz_A[i, j] = float(entradas_A[i][j].get())
                
        # 2. Calcular determinante principal y mostrarlo
        det_A = np.linalg.det(matriz_A)
        entry_det.config(state=tk.NORMAL)
        entry_det.delete(0, tk.END)
        entry_det.insert(0, f"{det_A:.2f}")
        entry_det.config(state="readonly")
        
        if abs(det_A) < 1e-9:
            messagebox.showerror("Error", "El determinante es 0. El sistema no tiene solución única.")
            return
            
        # 3. Aplicar Regla de Cramer
        for j in range(dim):
            matriz_Ai = matriz_A.copy()
            matriz_Ai[:, j] = vector_b  # Reemplaza la columna por el vector b
            
            det_Ai = np.linalg.det(matriz_Ai)#aca calculamos el determinante de la matriz Ai, que es la matriz A con la columna j reemplazada por el vector b
            xi = det_Ai / det_A
            
            entradas_x[j].config(state=tk.NORMAL)#  ponemos el entry de x en modo normal para poder escribir en el
            entradas_x[j].delete(0, tk.END)#  borramos el contenido del entry de x
            entradas_x[j].insert(0, f"{xi:.2f}")#  insertamos el valor de xi en el entry de x, dejando 2 decimales
            entradas_x[j].config(state="readonly")# ponemos el entry de x en modo readonly para que no se pueda modificar
            
    except ValueError:
        messagebox.showerror("Error de datos", "Asegúrese de ingresar números válidos en A y b.")# mensaje de error si hay algun valor invalido en la matriz A o el vector b
def calcular_determinante():
    dim = dimension_var.get()
    matriz_A = []
    
    try:
        # Extraemos únicamente las filas y columnas según la dimensión elegida
        for i in range(dim):
            fila = []
            for j in range(dim):
                # float() convierte el texto a número. Si hay texto inválido o vacío, salta al except.
                valor = float(entradas_A[i][j].get())
                fila.append(valor)
            matriz_A.append(fila)
            
        # Si el bucle termina sin errores, tenemos la matriz limpia.
        print("Matriz lista para calcular:", matriz_A)
        
        # Si el bucle termina sin errores, tenemos la matriz limpia.
        print("Matriz lista para calcular:", matriz_A)
        
        # --- LÓGICA MATEMÁTICA DEL CÁLCULO ---
        matriz_np = np.array(matriz_A) # Convertimos tu lista a una matriz de Numpy
        det_A = np.linalg.det(matriz_np)
        
        entry_det.config(state=tk.NORMAL)
        entry_det.delete(0, tk.END)
        entry_det.insert(0, f"{det_A:.2f}") # Dejamos 2 decimales
        entry_det.config(state="readonly")

    except ValueError:
        # Atajamos el error de conversión y mostramos un pop-up visual
        messagebox.showerror("Error de datos", "Por favor, complete todos los campos habilitados únicamente con números.")

def actualizar_dimension():
    dim = dimension_var.get()
    print(f"Dimensión cambiada a: {dim}x{dim}")
    
    # Recorremos las 4 filas y columnas posibles
    for i in range(4):
        # Para los vectores b y x: mostramos solo las filas correspondientes a la dimensión
        if i < dim:
            entradas_b[i].grid()
            entradas_x[i].grid()
        else:
            entradas_b[i].grid_remove()
            entradas_x[i].grid_remove()
            
        # Para la matriz A: hacemos lo mismo iterando por cada columna (j)
        for j in range(4):
            if i < dim and j < dim:
                entradas_A[i][j].grid()
            else:
                entradas_A[i][j].grid_remove()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Resolución de sistemas de ecuaciones lineales mediante el método de Cramer")
ventana.geometry("400x350")
ventana.resizable(False, False)
#la resolucion la tenemos que ver, no se ve muy bien


dimension_var = tk.IntVar(value=3) 

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

# Bucle principal de la aplicaciónç
actualizar_dimension() #es para que aparezca la dimension correcta, lo iniciaba y empezaba mal
ventana.mainloop()