# 📊 Estadísticas de Uso de ChatGPT

Este script genera un análisis visual de tus interacciones con ChatGPT a lo largo del año, mostrando un **mapa de calor** y estadísticas sobre la frecuencia de uso.

---

## 🚀 Cómo usar este script

### 1️⃣ Exporta tus conversaciones de ChatGPT
Desde tu cuenta de ChatGPT:
- Ve a **Configuración** → **Controles de datos** → **Exportar datos**.
- Descarga y descomprime el archivo exportado.
- Localiza la carpeta donde están los datos (generalmente `export_chatgpt`).

### 2️⃣ Configura tu entorno
#### 📌 Requisitos
Asegúrate de tener **Python 3.x** instalado y luego instala las dependencias ejecutando:
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecuta el script
Abre una terminal en la carpeta del script y ejecuta:
```bash
python estadisticas_chatgpt.py
```

### 4️⃣ Introduce la información necesaria
Al ejecutar el script, se te pedirá que introduzcas:
- **Tu zona horaria** (si no se detecta automáticamente).
- **El año** que quieres analizar (por ejemplo, 2025).

### 5️⃣ Visualiza los resultados
El script generará:
- Un **mapa de calor** con la frecuencia de uso diario.
- Estadísticas en la terminal, incluyendo:
  - Total de interacciones en el año.
  - Media de interacciones por día.
  - Día con más interacciones.

---

## 🛠 Solución de problemas
### ❌ Error de permisos al instalar dependencias
Si ves un error como:
```
ERROR: Could not install packages due to an OSError: [WinError 5] Acceso denegado...
```
Prueba con:
```bash
pip install --user -r requirements.txt
```
O ejecuta el terminal como **Administrador** y vuelve a intentarlo.

### ❌ No se encuentra el archivo `conversations.json`
Asegúrate de que el archivo exportado de ChatGPT está en la carpeta correcta y que `convo_folder` en el script apunta al directorio correcto.

---

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. ¡Úsalo, modifícalo y comparte libremente! 😊

---

## ⭐ ¡Dale una estrella al repositorio!
Si este proyecto te ha sido útil, considera darle una ⭐ en GitHub para apoyar su desarrollo. ¡Gracias por tu apoyo! 🚀

