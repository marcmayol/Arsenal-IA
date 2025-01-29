from typing import Dict, Union
from huggingface_hub import get_safetensors_metadata
import argparse
import sys

# Mapeo de tipos de datos a su tamaño en bytes
bytes_per_dtype = {"int4": 0.5, "int8": 1, "float8": 1, "float16": 2, "float32": 4}

def calculate_gpu_memory(parameters: float, bytes: float) -> float:
    # Calcula la memoria requerida en GPU en función de los parámetros y el tipo de dato
    return round((parameters * 4) / (32 / (bytes * 8)) * 1.18, 2)

def get_model_size(model_id: str, dtype: str = "float16") -> Union[float, None]:
    # Obtiene el tamaño estimado del modelo en GPU a partir de su ID en Hugging Face
    try:
        if dtype not in bytes_per_dtype:
            raise ValueError("Unsupported dtype")
        metadata = get_safetensors_metadata(model_id)
        if not metadata or not metadata.parameter_count:
            raise ValueError(f"Could not fetch metadata for model: {model_id}")
        model_parameters = int(list(metadata.parameter_count.values())[0]) / 1_000_000_000
        return calculate_gpu_memory(model_parameters, bytes_per_dtype[dtype])
    except Exception as e:
        print(f"Error estimating model size: {str(e)}", file=sys.stderr)
        return None

def main():
    # Ejecuta el cálculo de memoria a partir de los argumentos de línea de comandos
    parser = argparse.ArgumentParser()
    parser.add_argument("model_id", help="Hugging Face model ID (e.g., OwenArli/ArliAI-Llama-3-8B-Instruct-Dolfin-v0.1)")
    parser.add_argument("--dtype", default="float16", choices=bytes_per_dtype.keys(), help="Data type for model loading")
    args = parser.parse_args()
    size = get_model_size(args.model_id, args.dtype)
    print(f"Estimated GPU memory requirement for {args.model_id}: {size:.2f} GB ({args.dtype})")
    
    
if __name__ == "__main__":
    main()

# ⭐ en GitHUB!!
    print("\n🔗 Entra en https://github.com/marcmayol/Arsenal-IA y dale una ⭐!")
