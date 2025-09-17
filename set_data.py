import pandas as pd
import numpy as np

# Definir columnas igual que tu dataset histórico
columns = [
    "id", "referee", "timezone", "date", "venue_id", "venue_name", "venue_city",
    "season", "round", "home_team", "away_team",
    "home_goals", "away_goals", "home_goals_half_time", "away_goals_half_time",
    "home_goals_fulltime", "away_goals_fulltime",
    "home_goals_extra_time", "away_goals_extratime", "home_goals_penalty", "away_goals_penalty",
    "home_avg_goals_last5", "away_avg_goals_last5",
    "home_win_rate_last5", "away_win_rate_last5",
    "home_result", "home_winrate_all", "away_result", "away_winrate_all",
    "home_win_streak3", "h2h_goals_diff_last_5", "away_win_streak3",
    "Class"
]

# Crear lista vacía
data = []

# Jornadas 1 a 8 (ejemplo con Jornada 1, rellenas lo demás con los resultados de tus capturas)
jornada_1 = [
    {"season": 2025, "round": "Apertura - 1", "home_team": "Puebla", "away_team": "Atlas", "home_goals": 2, "away_goals": 3},
    {"season": 2025, "round": "Apertura - 1", "home_team": "Juárez", "away_team": "América", "home_goals": 1, "away_goals": 1},
    {"season": 2025, "round": "Apertura - 1", "home_team": "Tijuana", "away_team": "Querétaro", "home_goals": 1, "away_goals": 0},
    {"season": 2025, "round": "Apertura - 1", "home_team": "Toluca", "away_team": "Necaxa", "home_goals": 3, "away_goals": 1},
    {"season": 2025, "round": "Apertura - 1", "home_team": "Santos", "away_team": "Pumas", "home_goals": 3, "away_goals": 0},
    {"season": 2025, "round": "Apertura - 1", "home_team": "Cruz Azul", "away_team": "Mazatlán", "home_goals": 0, "away_goals": 0},
    {"season": 2025, "round": "Apertura - 1", "home_team": "Pachuca", "away_team": "Monterrey", "home_goals": 3, "away_goals": 0},
    {"season": 2025, "round": "Apertura - 1", "home_team": "León", "away_team": "Atl. San Luis", "home_goals": 0, "away_goals": 1},
]

for match in jornada_1:
    row = {col: np.nan for col in columns}  # Inicializamos con NaN
    row.update(match)                       # Metemos datos de ese partido
    # Definir la clase del resultado
    if pd.notna(row["home_goals"]) and pd.notna(row["away_goals"]):
        if row["home_goals"] > row["away_goals"]:
            row["Class"] = 1
        elif row["home_goals"] < row["away_goals"]:
            row["Class"] = -1
        else:
            row["Class"] = 0
    data.append(row)

# Jornada 9 (sin goles, para predecir)
jornada_9 = [
    {"season": 2025, "round": "Apertura - 9", "home_team": "Club América", "away_team": "Guadalajara Chivas"},
    {"season": 2025, "round": "Apertura - 9", "home_team": "Cruz Azul", "away_team": "Monterrey"},
    # ... completa con los demás partidos de la jornada 9
]

for match in jornada_9:
    row = {col: np.nan for col in columns}
    row.update(match)
    data.append(row)

# Convertir a DataFrame
df = pd.DataFrame(data, columns=columns)

# Exportar
df.to_csv("apertura_2025_j1_j9.csv", index=False, encoding="utf-8")
print("CSV generado: apertura_2025_j1_j9.csv")
