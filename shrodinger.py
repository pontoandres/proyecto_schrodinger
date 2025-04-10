import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
import os

# --- Constantes físicas ---
e = 1.602e-19
epsilon_0 = 8.854e-12
hbar = 1.055e-34
m = 9.109e-31

# --- Parámetros del potencial ---
D = e**2 / (4 * np.pi * epsilon_0)
C = 2 * m / hbar**2

# --- Dominios espaciales específicos por estado n ---
dominios = {
    1: (1e-12, 5.8e-10, 1e-12),
    2: (1e-12, 1.4e-9, 1e-12),
    3: (1e-12, 2.05e-9, 1e-11),
    4: (1e-12, 2.6e-9, 1e-12)
}

# --- Método numérico para resolver la ecuación de Schrödinger ---
def resolver_schrodinger(E_J, x_vals, dx):
    psi = np.zeros_like(x_vals)
    psi[0] = 0
    psi[1] = dx * 0.5

    for i in range(1, len(x_vals) - 1):
        x = x_vals[i]
        V = -D / x
        psi[i + 1] = (2 * psi[i] - psi[i - 1] + dx**2 * C * (V - E_J) * psi[i])

    return psi

# --- Función objetivo que depende de x_vals y dx ---
def objetivo(E_eV, x_vals, dx):
    E_J = E_eV * e
    psi = resolver_schrodinger(E_J, x_vals, dx)
    return psi[-1]

# --- Encuentra la energía propia usando el dominio correspondiente a n ---
def encontrar_energia_prop(n, E_min_eV, E_max_eV, x_vals, dx):
    return bisect(lambda E: objetivo(E, x_vals, dx), E_min_eV, E_max_eV, xtol=1e-4)

# --- Script principal ---
if __name__ == "__main__":
    os.makedirs("graficos", exist_ok=True)

    # Intervalos de búsqueda
    niveles = [
        (1, -13.7, -9),
        (2, -5, -2),
        (3, -1.6, -1.3),
        (4, -2, -0.3)
    ]

    print("==== Diagnóstico de extremos ====")
    for n, emin, emax in niveles:
        x_min, x_max, dx = dominios[n]
        x_vals = np.arange(x_min, x_max, dx)

        print(f"\nEstado n = {n}")
        print(f"ψ(x_max) con E = {emin} eV → {objetivo(emin, x_vals, dx)}")
        print(f"ψ(x_max) con E = {emax} eV → {objetivo(emax, x_vals, dx)}")

    # --- Bucle principal ---
    for n, emin, emax in niveles:
        x_min, x_max, dx = dominios[n]
        x_vals = np.arange(x_min, x_max, dx)

        E_n_eV = encontrar_energia_prop(n, emin, emax, x_vals, dx)
        E_n_J = E_n_eV * e
        psi_n = resolver_schrodinger(E_n_J, x_vals, dx)

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
