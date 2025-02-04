# 📊 Herramientas de Visualización de Uso de IA 🚀

## 📌 Descripción ✨

Este repositorio contiene dos herramientas para analizar y visualizar la actividad de interacciones con modelos de IA en un calendario de calor anual:

- **[ChatGPT](https://github.com/marcmayol/Arsenal-IA/tree/main/Estad%C3%ADsticas%20de%20Uso%20de%20Inteligencia%20Artificial/chatgpt)**: Herramienta para analizar el uso de ChatGPT a partir de sus datos de exportación.
- **[Claude](https://github.com/marcmayol/Arsenal-IA/tree/main/Estad%C3%ADsticas%20de%20Uso%20de%20Inteligencia%20Artificial/claude/export_claude)**: Herramienta para analizar el uso de Claude a partir de sus datos de exportación.

Ambas herramientas generan un heatmap basado en los datos de conversaciones almacenados en archivos JSON exportados desde cada plataforma.

## 🔥 Características 📌

- **Carga de datos**: Importa conversaciones desde archivos JSON con timestamps en formato específico de cada IA.
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

### Para ChatGPT 📢

1. Exporta las conversaciones de ChatGPT en formato JSON y guárdalas en la carpeta `export_chatgpt`.
2. Ejecuta el script:
   ```sh
   python estadisticas_chatgpt.py
   ```
3. Introduce tu zona horaria cuando se te solicite (ejemplo: `Europe/Madrid`).
4. Introduce el año que deseas analizar (ejemplo: `2025`).
5. Se generará un heatmap con los datos y se mostrarán estadísticas en pantalla. 📊

### Para Claude 🤖

1. Exporta las conversaciones de Claude en formato JSON y guárdalas en la carpeta `export_claude`.
2. Ejecuta el script:
   ```sh
   python estadisticas_claude.py
   ```
3. Introduce tu zona horaria cuando se te solicite (ejemplo: `Europe/Madrid`).
4. Introduce el año que deseas analizar (ejemplo: `2025`).
5. Se generará un heatmap con los datos y se mostrarán estadísticas en pantalla. 📊

## 📈 Ejemplo de Salida 🔍

- Un heatmap mostrando la actividad por día.
- Estadísticas detalladas sobre el uso de cada IA en el año seleccionado.

## 🤝 Contribuciones ✨

Si deseas mejorar estas herramientas, puedes realizar un fork del repositorio y enviar un pull request con tus cambios. 🛠️

## 📝 Licencia 📜

Estas herramientas son de código abierto bajo la licencia MIT. 📄

Si te gustan estas herramientas, considera darle una estrella al repositorio ⭐🚀✨.

