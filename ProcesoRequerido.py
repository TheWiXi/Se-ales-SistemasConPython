import numpy as np
import matplotlib.pyplot as plt

# 1. Identidad de Euler para señales exponenciales complejas
# a) x(t) = 6e^{-j4πt}
#    x(t) = 6[cos(4πt) - j sin(4πt)]
def senal1(t):
    return 6 * np.exp(-1j * 4 * np.pi * t)
def senal1_cos(t):
    return 6 * np.cos(4 * np.pi * t)
def senal1_sin(t):
    return -6 * np.sin(4 * np.pi * t)

# b) x(t) = 10e^{j8πt-2π}
#    x(t) = 10e^{-2π} [cos(8πt) + j sin(8πt)]
def senal2(t):
    return 10 * np.exp(-2 * np.pi) * np.exp(1j * 8 * np.pi * t)
def senal2_cos(t):
    return 10 * np.exp(-2 * np.pi) * np.cos(8 * np.pi * t)
def senal2_sin(t):
    return 10 * np.exp(-2 * np.pi) * np.sin(8 * np.pi * t)

# 2. Parte real e imaginaria de 5e^{-j4π} y 20e^{j10π}
num1 = 5 * np.exp(-1j * 4 * np.pi)
num2 = 20 * np.exp(1j * 10 * np.pi)
parte_real1 = np.real(num1)
parte_imag1 = np.imag(num1)
parte_real2 = np.real(num2)
parte_imag2 = np.imag(num2)

# 3. Convertir señales continuas a versión exponencial compleja
# a) x(t) = 5 cos(200πt + π)
#    x(t) = 5 Re{e^{j(200πt + π)}}
def senal3(t):
    return 5 * np.cos(200 * np.pi * t + np.pi)
def senal3_exp(t):
    return 5 * np.exp(1j * (200 * np.pi * t + np.pi))
# b) x(t) = 5 sin(100πt + π)
#    x(t) = 5 Im{e^{j(100πt + π)}}
def senal4(t):
    return 5 * np.sin(100 * np.pi * t + np.pi)
def senal4_exp(t):
    return 5 * np.exp(1j * (100 * np.pi * t + np.pi))

# 4. Parte real e imaginaria de x(t) = 6e^{(-2+2πj)t}u(t)
def senal5(t):
    return 6 * np.exp((-2 + 2 * np.pi * 1j) * t) * (t >= 0)
def senal5_real(t):
    return np.real(senal5(t))
def senal5_imag(t):
    return np.imag(senal5(t))

# 5. Intervalos de la señal discreta x(n) = 2[μ(n) - μ(n-10)]
def x5(n):
    return 2 * ((n >= 0) & (n < 10))

# 6. Intervalos de la señal discreta x(n) = 2[μ(n)-μ(n+5)] + 10[μ(n-10)-μ(n-10)]
def x6(n):
    return 2 * ((n >= -5) & (n < 0)) + 10 * ((n >= 0) & (n < 10))

# Graficar señales continuas
t = np.linspace(-1, 1, 1000)
plt.figure(figsize=(12, 8))
plt.subplot(2,2,1)
plt.plot(t, senal1_cos(t), label='Parte real')
plt.plot(t, senal1_sin(t), label='Parte imaginaria')
plt.title('x(t) = 6e^{-j4πt}')
plt.legend()
plt.subplot(2,2,2)
plt.plot(t, senal2_cos(t), label='Parte real')
plt.plot(t, senal2_sin(t), label='Parte imaginaria')
plt.title('x(t) = 10e^{j8πt-2π}')
plt.legend()
plt.subplot(2,2,3)
plt.plot(t, np.real(senal3_exp(t)), label='coseno')
plt.title('x(t) = 5cos(200πt + π)')
plt.subplot(2,2,4)
plt.plot(t, np.imag(senal4_exp(t)), label='seno')
plt.title('x(t) = 5sin(100πt + π)')
plt.tight_layout()
plt.show()

# Graficar parte real e imaginaria de senal5
t2 = np.linspace(-1, 2, 1000)
plt.figure(figsize=(8,4))
plt.plot(t2, senal5_real(t2), label='Parte real')
plt.plot(t2, senal5_imag(t2), label='Parte imaginaria')
plt.title('x(t) = 6e^{(-2+2πj)t}u(t)')
plt.legend()
plt.show()

# Graficar señales discretas
n = np.arange(-10, 20)
plt.figure(figsize=(8,4))
plt.stem(n, x5(n), basefmt=" ")
plt.title('x(n) = 2[μ(n) - μ(n-10)]')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

plt.figure(figsize=(8,4))
plt.stem(n, x6(n), basefmt=" ")
plt.title('x(n) = 2[μ(n)-μ(n+5)] + 10[μ(n-10)-μ(n-10)]')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

# Mostrar resultados numéricos de la parte real e imaginaria del punto 2
print(f"Parte real de 5e^(-j4π): {parte_real1}")
print(f"Parte imaginaria de 5e^(-j4π): {parte_imag1}")
print(f"Parte real de 20e^(j10π): {parte_real2}")
print(f"Parte imaginaria de 20e^(j10π): {parte_imag2}")
