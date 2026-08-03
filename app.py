import math
import tkinter as tk
from tkinter import messagebox


def truncar_decimales(numero: float) -> str:
    partes = f"{numero:.8f}".split(".")
    enteros = partes[0]
    decimales = partes[1][:2]
    return f"{enteros}.{decimales}"


def calcular():
    txt_distancia = entry_distancia.get().strip()
    txt_frecuencia = entry_frecuencia.get().strip()

    # Reemplazar comas por puntos para aceptar ambos formatos
    txt_distancia = txt_distancia.replace(",", ".")
    txt_frecuencia = txt_frecuencia.replace(",", ".")

    # Validaciones de entrada
    try:
        distancia = float(txt_distancia)
        frecuencia = float(txt_frecuencia)
    except ValueError:
        messagebox.showerror(
            "Error de Ingreso",
            "Por favor, ingrese números válidos para la distancia y la frecuencia.",
        )
        return

    if distancia <= 0 or frecuencia <= 0:
        messagebox.showwarning(
            "Valores inválidos",
            "La distancia y la frecuencia deben ser valores mayores a cero.",
        )
        return

    # Cálculo según la fórmula: F1 = 8.656 * sqrt(D / f)
    resultado = 8.656 * math.sqrt(distancia / frecuencia)

    # Truncado a 2 decimales
    resultado_truncado = truncar_decimales(resultado)

    # Mostrar resultado en pantalla
    lbl_resultado.config(text=f"{resultado_truncado} m", fg="#1e7e34")


def limpiar():
    entry_distancia.delete(0, tk.END)
    entry_frecuencia.delete(0, tk.END)
    lbl_resultado.config(text="-", fg="#333333")


# --- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA ---
root = tk.Tk()
root.title("Calculadora de Zona de Fresnel")
root.geometry("420x460")
root.resizable(False, False)
root.configure(bg="#f4f6f9")

# Estilos básicos
FUEN_TEXTO = ("Helvetica", 10)
FUEN_RESULTADO = ("Helvetica", 18, "bold")

# Encabezado / Créditos 
frame_header = tk.Frame(root, bg="#1a252f", pady=12)
frame_header.pack(fill="x")

lbl_titulo = tk.Label(
    frame_header,
    text="Calculadora - Primera Zona de Fresnel",
    font=("Helvetica", 11, "bold"),
    fg="white",
    bg="#1a252f",
)
lbl_titulo.pack()

lbl_autor = tk.Label(
    frame_header,
    text="Desarrollado por: Carla Nadalig",
    font=("Helvetica", 9, "italic"),
    fg="#3498db",
    bg="#1a252f",
)
lbl_autor.pack(pady=(2, 0))

# Contenedor Principal
frame_body = tk.Frame(root, bg="#f4f6f9", padx=25, pady=20)
frame_body.pack(fill="both", expand=True)

# Campo: Distancia
lbl_d = tk.Label(
    frame_body,
    text="Distancia total del enlace (D) [km]:",
    font=FUEN_TEXTO,
    bg="#f4f6f9",
    anchor="w",
)
lbl_d.pack(fill="x", pady=(5, 2))

entry_distancia = tk.Entry(frame_body, font=FUEN_TEXTO, justify="center", bd=2)
entry_distancia.pack(fill="x", ipady=5, pady=(0, 10))

# Campo: Frecuencia
lbl_f = tk.Label(
    frame_body,
    text="Frecuencia de trabajo (f) [GHz]:",
    font=FUEN_TEXTO,
    bg="#f4f6f9",
    anchor="w",
)
lbl_f.pack(fill="x", pady=(5, 2))

entry_frecuencia = tk.Entry(
    frame_body, font=FUEN_TEXTO, justify="center", bd=2
)
entry_frecuencia.pack(fill="x", ipady=5, pady=(0, 15))

# Botones
btn_calcular = tk.Button(
    frame_body,
    text="CALCULAR",
    font=("Helvetica", 10, "bold"),
    bg="#27ae60",
    fg="white",
    activebackground="#219150",
    activeforeground="white",
    cursor="hand2",
    command=calcular,
)
btn_calcular.pack(fill="x", ipady=6, pady=(0, 5))

btn_limpiar = tk.Button(
    frame_body,
    text="Borrar campos",
    font=FUEN_TEXTO,
    bg="#e74c3c",
    fg="white",
    activebackground="#c0392b",
    activeforeground="white",
    cursor="hand2",
    command=limpiar,
)
btn_limpiar.pack(fill="x", ipady=3, pady=(0, 15))

# Separador
tk.Frame(frame_body, height=2, bg="#dcdde1").pack(fill="x", pady=10)

# Cuadro de Resultado
lbl_res_titulo = tk.Label(
    frame_body,
    text="Radio de la 1ª Zona de Fresnel (F₁):",
    font=FUEN_TEXTO,
    bg="#f4f6f9",
)
lbl_res_titulo.pack()

lbl_resultado = tk.Label(
    frame_body, text="-", font=FUEN_RESULTADO, fg="#333333", bg="#f4f6f9"
)
lbl_resultado.pack(pady=5)

root.mainloop()