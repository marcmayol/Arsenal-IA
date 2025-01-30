# 🖥️ Estimador de Memoria GPU para IA

Este script permite estimar el consumo de memoria GPU necesario para cargar un modelo de inteligencia artificial desde Hugging Face, considerando distintos formatos de datos.

## 🚀 Características
✅ Calcula la memoria necesaria en GB según el número de parámetros del modelo.  
✅ Compatible con distintos formatos de precisión: `int4`, `int8`, `float8`, `float16`, `float32`.  
✅ Usa metadatos de Hugging Face para obtener información del modelo.  
✅ Fácil de usar desde la línea de comandos.  

## 📥 Instalación
Para utilizar este estimador, instala las dependencias necesarias:
```bash
pip install huggingface_hub
```

## ⚙️ Uso
Ejecuta el script con el ID del modelo en Hugging Face:
```bash
python estimador_gpu.py <model_id>
```
Por ejemplo:
```bash
python estimador_gpu.py meta-llama/Llama-2-7b
```
Opcionalmente, puedes especificar el tipo de dato:
```bash
python estimador_gpu.py meta-llama/Llama-2-7b --dtype float16
```

## 📌 Notas
- El cálculo de memoria se basa en una estimación y puede variar según la implementación del modelo y optimizaciones específicas.
- Si el modelo no tiene metadatos disponibles en Hugging Face, el script mostrará un error.

## ⭐ ¡Apoya el proyecto!
Si este proyecto te resulta útil, **dale una estrella ⭐ en GitHub!**  
🔗 [GitHub Repo](https://github.com/marcmayol/Arsenal-IA)
