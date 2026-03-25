# importo las librerias
import numpy as np
import matplotlib.pyplot as plt


# defino mi funcion 

def mi_funcion_sen(amplitud = 1, offset = 0, f0 = 1, fase = 0, N = 1000, fs = 1000):
    """
    - amplitud: es la amplitud maxima. [amplitud] = [V]
    - offset: es mi amplitud media. [offset] = [V]
    - f0: es la frecuencia fundamental de la señal. [f0] = [Hz]S
    - fase: es la fase inicial. [fase] = [rad]
    - N: es la cantidad de muestras a generar
    - fs: es la frecuencia de muestreo --> cantidad de muestras que se toman cada 1 segundo. [fs] = [Hz]
    """

    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * f0 * tt + fase) + offset

    return tt, xx

# Defino mis variables
N = 1000
amplitud = 2
offset = 1
f0 = 5
fase = np.pi/4
fs = 1000

# Llamo a mi funcion
tt, xx = mi_funcion_sen(amplitud, offset, f0, fase, N, fs)

# Grafico la señal
plt.title("Señal Senoidal Generada")
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, linestyle = '-', color = 'r' ) # Genero el grafico de la señal con linea 'continua' de color 'rojo'
plt.show()

"""
--------------------------------------- EJERCICIO BONUS ---------------------------------------
--------------------------------------- ITEM 1 ---------------------------------------
"""

# Genero otra ventana para los graficos
plt.figure(figsize=(10, 6))  # Tamaño de la figura (ancho, alto)

# Señal 500 Hz, es Nyquist
plt.subplot(2, 2, 1)
tt, xx = mi_funcion_sen(1, 0, 500, 0, 1000, 50000)
plt.plot(tt, xx, '-', color='blue')
plt.title("Señal Senoidal con 500 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.grid(True)

# Señal 999 Hz
plt.subplot(2, 2, 2)
tt, xx = mi_funcion_sen(1, 0, 999, 0, 1000, 100000)
plt.plot(tt, xx, '-', color='green')
plt.title("Señal Senoidal con 999 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.grid(True)

# Señal 1001 Hz
plt.subplot(2, 2, 3)
tt, xx = mi_funcion_sen(1, 0, 1001, 0, 1000, 100000)
plt.plot(tt, xx, '-', color='orange')
plt.title("Señal Senoidal con 1001 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.grid(True)

# Señal 2001 Hz
plt.subplot(2, 2, 4)
tt, xx = mi_funcion_sen(1, 0, 2001, 0, 1000, 100000)
plt.plot(tt, xx, '-', color='grey')
plt.title("Señal Senoidal con 2001 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.grid(True)

plt.tight_layout()

plt.show()

"""
--------------------------------------- ITEM 2 -----------------------------------------------------------
--------------------------------------- Grafico una señal cuadrada ---------------------------------------
"""
from scipy import signal

def mi_funcion_cuadrada (f0, fs, N, offset, fase):
    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    ttc = np.arange(start = 0, stop= N*Ts, step = Ts)

    xxc = signal.square(2 * np.pi * f0 * ttc + fase) + offset

    return ttc, xxc

# Defino mis variables
N = 100
offset = 0
f0 = 4
fase = 0
fs = 100

# Llamo a mi funcion
ttc, xxc = mi_funcion_cuadrada(f0, fs, N, offset, fase)

# Grafico la señal cuadrada generada
plt.figure(figsize=(10, 4))
plt.plot(ttc, xxc, label='Señal Cuadrada')
plt.title('Generación de Señal Cuadrada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()

