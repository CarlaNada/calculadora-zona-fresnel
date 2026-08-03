# Calculadora de la Zona de Fresnel
Este software de escritorio fue desarrollado para realizar el cálculo del radio de la **Zona de Fresnel** de manera intuitiva, rápida y amigable.
---

## Información del Proyecto
* **Creadora:** Carla Nadalig
* **Materia:** Redes
* **Tecnología:** Python3 (Interfaz gráfica realizada con `tkinter`)
---

## Fórmula Utilizada
La aplicación utiliza la fórmula estándar para el radio de la primera zona de Fresnel ($F_1$ en metros), donde la distancia ($D$) está en kilómetros y la frecuencia ($f$) en gigahertz:

``` python
F1 = 8.656 * math.sqrt(distancia / frecuencia)
```

## Características Principales
Diseño intuitivo: Pensado para un uso sumamente fácil, con botones grandes, campos claros y una interfaz limpia.

Truncado a 2 decimales: El resultado se procesa estrictamente cortando a dos dígitos decimales sin redondear, garantizando el cumplimiento del requerimiento.

Validación inteligente de datos:
* Soporta ingreso tanto con punto (.) como con coma (,).
* Previene errores ante caracteres vacíos, letras o símbolos inválidos.
* Controla que los valores ingresados de distancia y frecuencia sean estrictamente mayores a cero.

## Cómo Ejecutar el Proyecto

Clonar o descargar el repositorio:
```Bash
git clone git@github.com:CarlaNada/calculadora-zona-fresnel.git
cd calculadora-zona-fresnel
```

Ejecutar la aplicación:
```Bash
python3 app.py
Si ejecutas la aplicación y hay un error sobre tkinter, instalar la librería ejecutando en tu terminal:
sudo apt install python3-tk
```

## Ejemplos de Prueba
| Caso de Uso | Distancia ($D$) | Frecuencia ($f$) | Resultado ($F_1$) | Detalle |
| :--- | :---: | :---: | :---: | :--- |
| **Estándar** | `10 km` | `5 GHz` | **`12.24 m`** | Valor redondeado real: 12.2414 |
| **Con coma** | `3,5 km` | `2,4 GHz` | **`10.45 m`** | Convierte `,` a `.` automáticamente |
| **Truncado** | `2 km` | `3 GHz` | **`7.06 m`** | Trunca en .06 (no redondea a .07) |
