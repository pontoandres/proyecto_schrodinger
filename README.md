# 🌌 Simulación 1D de la Ecuación de Schrödinger para el Átomo de Hidrógeno

Este proyecto resuelve numéricamente la ecuación de Schrödinger independiente del tiempo en 1D para el potencial de Coulomb, modelando los primeros estados ligados del electrón en el átomo de hidrógeno.

Se utiliza el **método de diferencias finitas** y el **método de bisección** para encontrar los valores propios de energía \(E_n\) y graficar las funciones de onda \( \psi_n(x) \).

---

## 📁 Estructura del Proyecto
proyecto_schrodinger/
│
├── shrodinger.py           # Código principal del simulador
├── graficos/               # Carpeta donde se guardan las gráficas generadas
├── env/                    # Entorno virtual (excluido por .gitignore)
├── .gitignore              # Ignora el entorno virtual y otros archivos temporales
└── README.md               # Documentación del proyecto

## ⚙️ Requisitos

Python 3.10 o superior.

### 📦 Librerías necesarias

- `numpy`
- `matplotlib`
- `scipy`

Puedes instalar todo con:

```bash
pip install -r requirements.txt
```
## Cómo Ejecutar el Proyecto

### 🖥️ Opción 1: Desde la terminal

1. Clona el repositorio (si aún no lo has hecho):

   ```bash
   git clone https://github.com/pontoandres/proyecto_schrodinger.git
   cd proyecto_schrodinger
   ```

2. Crea un entorno virtual (si no existe):

   ```bash
   python -m venv env
   ```

3. Activa el entorno virtual:

   En Windows:
   ```bash
   .\env\Scripts\activate
   ```

   En Mac/Linux:
   ```bash
   source env/bin/activate
   ```

4. Instala las dependencias necesarias:

   Si tienes un archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   O bien, instala las librerías manualmente:
   ```bash
   pip install numpy matplotlib scipy
   ```

5. Ejecuta el simulador:

   ```bash
   python shrodinger.py
   ```

6. Las gráficas se abrirán en pantalla y también se guardarán automáticamente en la carpeta `graficos/`.

---

### 💻 Opción 2: Desde Visual Studio Code (VS Code)

1. Abre la carpeta del proyecto en VS Code:  
   `Archivo > Abrir carpeta...` y selecciona `proyecto_schrodinger`.

2. Crea un entorno virtual (si no existe) desde la terminal integrada:

   ```bash
   python -m venv env
   ```

3. Activa el entorno virtual:

   En Windows:
   ```bash
   .\env\Scripts\activate
   ```

   En Mac/Linux:
   ```bash
   source env/bin/activate
   ```

4. Asegúrate de que VS Code esté usando el entorno virtual:  
   Presiona `Ctrl + Shift + P`, selecciona `Python: Select Interpreter`, y elige el que esté dentro de la carpeta `env`.

5. Instala las dependencias necesarias:

   Si tienes un archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   O bien, instala las librerías manualmente:
   ```bash
   pip install numpy matplotlib scipy
   ```

6. Ejecuta el archivo `shrodinger.py`:  
   Haz clic en el botón ▶️ en la esquina superior derecha o haz clic derecho sobre el archivo y selecciona **"Run Python File in Terminal"**.

7. Las gráficas se abrirán en pantalla y también se guardarán automáticamente en la carpeta `graficos/`.
