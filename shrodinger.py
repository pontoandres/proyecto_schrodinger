import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
import os

# --- Constantes físicas ---
e = 1.602e-19         # Carga del electrón (C)
epsilon_0 = 8.854e-12 # Permitividad del vacío (C²/(N·m²))
hbar = 1.055e-34      # Constante reducida de Planck (J·s)
m = 9.109e-31         # Masa del electrón (kg)

# --- Parámetros del potencial ---
D = e**2 / (4 * np.pi * epsilon_0)  # Constante del potencial de Coulomb
C = 2 * m / hbar**2                 # Constante de la ecuación

# --- Rango espacial ---
x_min = 1e-11  # evitamos división por cero
x_max = 2e-9
dx = 1e-11
x_vals = np.arange(x_min, x_max, dx)

# --- Método numérico para resolver la ecuación de Schrödinger ---
def resolver_schrodinger(E_J):
    psi = np.zeros_like(x_vals)
    psi[0] = 0                    # Condición inicial
    psi[1] = dx * 0.5             # Derivada inicial aproximada

    for i in range(1, len(x_vals) - 1):
        x = x_vals[i]
        V = -D / x
        psi[i + 1] = (2 * psi[i] - psi[i - 1] + dx**2 * C * (V - E_J) * psi[i])

    return psi

# --- Función objetivo: valor de ψ al final del dominio ---
def objetivo(E_eV):
    E_J = E_eV * e
    psi = resolver_schrodinger(E_J)
    return psi[-1]  # Queremos que esto sea ≈ 0 para un valor propio de E

# --- Encuentra el valor propio de energía usando el método de bisección ---
def encontrar_energia_prop(n, E_min_eV, E_max_eV):
    E_n = bisect(objetivo, E_min_eV, E_max_eV, xtol=1e-4)
    return E_n

# --- Script principal ---
if __name__ == "__main__":
    os.makedirs("graficos", exist_ok=True)

    # Intervalos de búsqueda de energía (eV) para los 4 primeros estados
    niveles = [
    #(1, -14, -13.6),
    (2, -40.5, -3.3),
    (3, -1.7, -1.3),
    #(4, -1.1, -0.75)
    ]


    # 🔍 Diagnóstico: inspeccionar extremos del intervalo
    print("==== Diagnóstico de extremos ====")
    for i, (n, emin, emax) in enumerate(niveles):
        #n = i + 1
        print(f"\nEstado n = {n}")
        print(f"ψ(x_max) con E = {emin} eV → {objetivo(emin)}")
        print(f"ψ(x_max) con E = {emax} eV → {objetivo(emax)}")

    # 🚀 Bucle principal
    for n, emin, emax in niveles:
        E_n_eV = encontrar_energia_prop(n, emin, emax)
        E_n_J = E_n_eV * e
        psi_n = resolver_schrodinger(E_n_J)

        norm = np.trapz(psi_n**2, x_vals)
        psi_n /= np.sqrt(norm)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals * 1e9, psi_n, label=f"E = {E_n_eV:.4f} eV")
        plt.title(f"ψ{n}(x) — Estado n = {n}")
        plt.xlabel("x (nm)")
        plt.ylabel(f"ψ{n}(x)")
        plt.grid()
        plt.legend()
        plt.savefig(f"graficos/psi_{n}.png")
    plt.show()


    print("✅ ¡Listo! Se generaron los gráficos en la carpeta 'graficos/'.")
