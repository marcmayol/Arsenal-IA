import json
import pytz
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime, timezone, timedelta
from collections import Counter

def get_local_timezone():
    try:
        return datetime.now().astimezone().tzinfo.zone
    except AttributeError:
        return input("Introduce tu zona horaria (ejemplo: Europe/Madrid): ")

def get_year_from_user():
    while True:
        try:
            year = int(input("Introduce el año para el análisis (ejemplo: 2025): "))
            if year > 2000 and year < 2100:
                return year
            else:
                print("Por favor, introduce un año válido entre 2000 y 2100.")
        except ValueError:
            print("Entrada no válida. Introduce un número de año válido.")

def create_year_heatmap(convo_times, year):
    # Convertir convo_times a fechas y filtrar para el año dado
    just_dates = [convo.date() for convo in convo_times if convo.year == year]

    date_counts = Counter(just_dates)

    # Crear un rango de fechas para todo el año
    start_date = datetime(year, 1, 1).date()
    end_date = datetime(year, 12, 31).date()

    total_days = (end_date - start_date).days + 1
    date_range = [start_date + timedelta(days=i) for i in range(total_days)]

    # Preparar datos para el heatmap
    data = []
    for date in date_range:
        week = ((date - start_date).days + start_date.weekday()) // 7
        day_of_week = date.weekday()
        count = date_counts.get(date, 0)
        data.append((week, day_of_week, count))

    weeks_in_year = (end_date - start_date).days // 7 + 1

    # Estadísticas
    total_interactions = sum(date_counts.values())
    avg_interactions_per_day = total_interactions / total_days

    # Crear el heatmap
    plt.figure(figsize=(15, 8))
    ax = plt.gca()
    ax.set_aspect('equal')

    max_count_date = max(date_counts, key=date_counts.get, default=None)
    max_count = date_counts[max_count_date] if max_count_date else 0
    p90_count = np.percentile(list(date_counts.values()), 90) if date_counts else 1

    for week, day_of_week, count in data:
        color = plt.cm.Greens((count + 1) / p90_count) if count > 0 else 'lightgray'
        rect = patches.Rectangle((week, day_of_week), 1, 1, linewidth=0.5, edgecolor='black', facecolor=color)
        ax.add_patch(rect)

    # Etiquetas de los meses
    month_starts = [start_date + timedelta(days=i) for i in range(total_days)
                    if (start_date + timedelta(days=i)).day == 1]
    for month_start in month_starts:
        week = (month_start - start_date).days // 7
        plt.text(week + 0.5, 7.75, month_start.strftime('%b'), ha='center', va='center', fontsize=10, rotation=0)

    # Ajustes visuales
    ax.set_xlim(-0.5, weeks_in_year + 0.5)
    ax.set_ylim(-0.5, 8.5)
    plt.title(
        f'Estadísticas de Uso de ChatGPT - {year}\n'
        f'Total de interacciones: {total_interactions}\n'
        f'Media de interacciones por día: {avg_interactions_per_day:.2f}\n'
        f'Día más activo: {max_count_date} con {max_count} interacciones.',
        fontsize=16
    )
    plt.xticks([])
    plt.yticks(range(7), ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'])
    plt.gca().invert_yaxis()
    plt.show()

    print(f"Total de interacciones en {year}: {total_interactions}")
    print(f"Media de interacciones por día: {avg_interactions_per_day:.2f}")
    print(f"Día más activo: {max_count_date} con {max_count} interacciones")

    return total_interactions, avg_interactions_per_day

# Cargar datos de conversaciones desde JSON
def load_conversations(file_path, local_tz):
    with open(file_path, 'r') as f:
        oai_convs = json.load(f)

    oai_convo_times = []
    for conv in oai_convs:
        unix_timestamp = conv['create_time']
        utc_datetime = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
        local_datetime = utc_datetime.astimezone(pytz.timezone(local_tz))
        oai_convo_times.append(local_datetime)
    
    return oai_convo_times

# Configuración del archivo y zona horaria
convo_folder = 'export_chatgpt'
local_tz = get_local_timezone()
year = get_year_from_user()
oai_convo_times = load_conversations(f'{convo_folder}/conversations.json', local_tz)

# Ejecutar la función con los datos cargados
total_interactions, avg_interactions_per_day = create_year_heatmap(oai_convo_times, year)
