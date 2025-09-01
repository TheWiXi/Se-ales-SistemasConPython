import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Punto 1: Señal x(t) = 10*sin(t)
# -----------------------------
T1 = 2 * np.pi  # Intervalo de integración

def potencia_promedio_continua_x1():
    # Potencia promedio normalizada (integral de |x(t)|^2 / T)
    from scipy.integrate import quad
    integrando = lambda t: (10 * np.sin(t)) ** 2
    potencia, _ = quad(integrando, 0, T1)
    return potencia / T1

potencia1 = potencia_promedio_continua_x1()
print(f"Punto 1: Potencia promedio normalizada (continua) de x(t)=10sin(t) en [0,2pi]: {potencia1:.2f}")

# -----------------------------
# Punto 2: Discretización de x(t) = 10*sin(t)
# -----------------------------
fs = 100  # Frecuencia de muestreo (Hz)
t2 = np.linspace(0, T1, int(fs * T1))
x2 = 10 * np.sin(t2)

# Potencia promedio normalizada discreta
potencia2 = np.sum(x2 ** 2) / len(x2)
print(f"Punto 2: Potencia promedio normalizada (discreta) de x[n]=10sin(n) en [0,2pi]: {potencia2:.2f}")

plt.figure(figsize=(8, 3))
plt.stem(t2, x2)
plt.title('Punto 2: Señal Discreta x[n]=10sin(n)')
plt.xlabel('t')
plt.ylabel('x[n]')
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# Punto 3: Señal x(t) = e^t [μ(t+2)μ(-t+2)]
# -----------------------------
def x3(t):
    # μ(t+2) = 1 para t >= -2, μ(-t+2) = 1 para t <= 2
    return np.exp(t) * ((t >= -2) & (t <= 2))

# Potencia promedio normalizada continua
T3 = 4  # Intervalo de t donde x(t)>0: t in [-2,2]
def potencia_promedio_continua_x3():
    from scipy.integrate import quad
    integrando = lambda t: (np.exp(t)) ** 2
    potencia, _ = quad(integrando, -2, 2)
    return potencia / T3

potencia3 = potencia_promedio_continua_x3()
print(f"Punto 3: Potencia promedio normalizada (continua) de x(t)=e^t[μ(t+2)μ(-t+2)] en [-2,2]: {potencia3:.2f}")

# -----------------------------
# Punto 4: Discretización de x(t) = e^t [μ(t+2)μ(-t+2)]
# -----------------------------
fs3 = 100  # Frecuencia de muestreo (Hz)
t4 = np.linspace(-2, 2, int(fs3 * T3))
x4 = np.exp(t4)

potencia4 = np.sum(x4 ** 2) / len(x4)
print(f"Punto 4: Potencia promedio normalizada (discreta) de x[n]=e^n en [-2,2]: {potencia4:.2f}")

plt.figure(figsize=(8, 3))
plt.stem(t4, x4)
plt.title('Punto 4: Señal Discreta x[n]=e^n')
plt.xlabel('t')
plt.ylabel('x[n]')
plt.grid(True)
plt.tight_layout()
plt.show()

# Fin del archivo. Cada bloque está comentado según el punto correspondiente.
