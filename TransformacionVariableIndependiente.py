import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Señal x(t), versiones x(t-2) y x(t+3)
# -----------------------------
def x1(t):
    # x(t) = t+1 para -1 < t < 0, x(t) = 1 para 0 <= t < 2, x(t) = 3-t para 2 <= t < 3, 0 en el resto
    return np.piecewise(t,
        [t < -1, (t >= -1) & (t < 0), (t >= 0) & (t < 2), (t >= 2) & (t < 3), t >= 3],
        [0, lambda t: t+1, 1, lambda t: 3-t, 0])

tr = np.linspace(-2, 4, 1000)  # rango ajustado para ver bien la señal
plt.figure(figsize=(10, 6))
plt.subplot(3,1,1)
plt.plot(tr, x1(tr), label='x(t)')
plt.title('Punto 1: x(t)')
plt.grid(True)
plt.legend()

plt.subplot(3,1,2)
plt.plot(tr, x1(tr-2), label='x(t-2)')
plt.title('Punto 1: x(t-2)')
plt.grid(True)
plt.legend()

plt.subplot(3,1,3)
plt.plot(tr, x1(tr+3), label='x(t+3)')
plt.title('Punto 1: x(t+3)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# -----------------------------
# 2. Dibujar x(-t) y x(3-t) para la función x(t) del punto 2
# -----------------------------
def x2(t):
    # x(t) = t+1 para -1 <= t <= 0, x(t) = 1 para 0 < t <= 2, 0 en el resto
    return np.piecewise(t,
        [t < -1, ((t >= -1) & (t <= 0)), ((t > 0) & (t <= 2)), t > 2],
        [0, lambda t: t+1, 1, 0])

plt.figure(figsize=(10, 8))
plt.subplot(3,1,1)
plt.plot(tr, x2(tr), label='x(t)')
plt.title('Punto 2: x(t)')
plt.grid(True)
plt.legend()

plt.subplot(3,1,2)
plt.plot(tr, x2(-tr), label='x(-t)')
plt.title('Punto 2: x(-t)')
plt.grid(True)
plt.legend()

plt.subplot(3,1,3)
plt.plot(tr, x2(3-tr), label='x(3-t)')
plt.title('Punto 2: x(3-t)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# -----------------------------
# 3. Representación de x(t) desplazada y comprimida: x(3t-6)
# -----------------------------
plt.figure(figsize=(8,4))
plt.plot(tr, x1(3*tr-6), label='x(3t-6)')
plt.title('Punto 3: x(3t-6)')
plt.grid(True)
plt.legend()
plt.show()

# -----------------------------
# 4. Señal x(t) = sin(2πt), dibujar x(-t) y x(4t)
# -----------------------------
def x4(t):
    return np.sin(2*np.pi*t)

plt.figure(figsize=(10,6))
plt.subplot(3,1,1)
plt.plot(tr, x4(tr), label='x(t) = sin(2πt)')
plt.legend()
plt.grid(True)
plt.title('Punto 4: x(t)')

plt.subplot(3,1,2)
plt.plot(tr, x4(-tr), label='x(-t)')
plt.legend()
plt.grid(True)
plt.title('Punto 4: x(-t)')

plt.subplot(3,1,3)
plt.plot(tr, x4(4*tr), label='x(4t)')
plt.legend()
plt.grid(True)
plt.title('Punto 4: x(4t)')

plt.tight_layout()
plt.show()

# -----------------------------
# 5. Señal x(t) = 10e^{2t}e^{jπt}, discretizar y graficar parte real e imaginaria
# -----------------------------
N = 10
t5 = np.arange(0, 11) * (1/N)
x5 = 10 * np.exp(2*t5) * np.exp(1j * np.pi * t5)

plt.figure(figsize=(10,4))
plt.stem(t5, np.real(x5), linefmt='b-', markerfmt='bo', basefmt='k-', label='Re{x(t)}')
plt.stem(t5, np.imag(x5), linefmt='r-', markerfmt='ro', basefmt='k-', label='Im{x(t)}')
plt.title('Punto 5: x(t) = 10e^{2t}e^{jπt} (N=10)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# 6. Señal x(t) = e^{t} [u(t+2) - u(t-2)] y versiones transformadas
# -----------------------------
def u(t):
    return np.where(t >= 0, 1, 0)

def x6(t):
    return np.exp(t) * (u(t+2) - u(t-2))

plt.figure(figsize=(10,8))
plt.subplot(3,1,1)
plt.plot(tr, x6(tr+2), label='x(t+2)')
plt.title('Punto 6a: x(t+2)')
plt.grid(True)
plt.legend()

plt.subplot(3,1,2)
plt.plot(tr, x6(-2*tr), label='x(-2t)')
plt.title('Punto 6b: x(-2t)')
plt.grid(True)
plt.legend()

plt.subplot(3,1,3)
plt.plot(tr, x6((tr/2)+2), label='x(t/2 + 2)')
plt.title('Punto 6c: x(t/2 + 2)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
