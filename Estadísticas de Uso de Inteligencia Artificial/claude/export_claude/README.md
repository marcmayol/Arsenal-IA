# 📊 Herramienta de Visualización de Uso de Claude 🚀

## 📊 Descripción ✨

Esta herramienta permite analizar y visualizar la actividad de interacciones con Claude en un calendario de calor anual. 📅🔥 Genera un heatmap basado en los datos de conversaciones almacenados en un archivo JSON exportado desde Claude.

## 🔥 Características 📌

- **Carga de datos**: Importa conversaciones desde un archivo JSON con timestamps en formato ISO.
- **Conversión de zona horaria**: Ajusta las marcas de tiempo de UTC a la zona horaria local del usuario.
- **Análisis por año**: Permite al usuario seleccionar el año que desea analizar.
- **Visualización en Heatmap**: Muestra un calendario de calor con la frecuencia de interacciones por día. 📅
- **Estadísticas**: Presenta el total de interacciones, media diaria y el día con más actividad.

## 📜 Requisitos ⚙️

- Python 3.x
- Instala las dependencias desde el archivo `requirements.txt` con el siguiente comando:
  ```sh
  pip install -r requirements.txt
  ```

## 🚀 Uso 🛠️

1. Exporta las conversaciones de Claude en formato JSON y guárdalas en la carpeta `export_claude`.
2. Ejecuta el script:
   ```sh
   python estadsiticas_claude.py
   ```
3. Introduce tu zona horaria cuando se te solicite (ejemplo: `Europe/Madrid`).
4. Introduce el año que deseas analizar (ejemplo: `2025`).
5. Se generará un heatmap con los datos y se mostrarán estadísticas en pantalla. 📊

## 📈 Ejemplo de Salida 🔍

- Un heatmap mostrando la actividad por día.
- Estadísticas detalladas sobre el uso de Claude en el año seleccionado.

## 🤝 Contribuciones ✨

Si deseas mejorar esta herramienta, puedes realizar un fork del repositorio y enviar un pull request con tus cambios. 🛠️

## 📝 Licencia 📜

Esta herramienta es de código abierto bajo la licencia MIT. 📄

Si te gusta esta herramienta, considera darle una estrella al repositorio ⭐🚀✨.