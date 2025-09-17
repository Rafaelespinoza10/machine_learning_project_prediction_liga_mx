import requests
import pandas as pd
import time

API_KEY = "9a1a0af60ec9dc87792c38e7a8da5a9d"
headers = {"x-apisports-key": API_KEY}

def get_fixtures(season):
    """Trae todos los partidos de una temporada de Liga MX."""
    url = "https://v3.football.api-sports.io/fixtures"
    params = {"league": 262, "season": season}  # 262 = Liga MX
    res = requests.get(url, headers=headers, params=params).json()
    return res["response"]

def get_stats(fixture_id):
    """Trae estadísticas de un partido específico."""
    url = "https://v3.football.api-sports.io/fixtures/statistics"
    params = {"fixture": fixture_id}
    res = requests.get(url, headers=headers, params=params).json()
    return res["response"]

all_data = []

# 🔹 Rango de temporadas 2012–2025
for season in range(2012, 2026):
    print(f"Descargando temporada {season}...")
    fixtures = get_fixtures(season)

    for match in fixtures:
        fixture_id = match["fixture"]["id"]
        home_team = match["teams"]["home"]["name"]
        away_team = match["teams"]["away"]["name"]
        date = match["fixture"]["date"]
        goals_home = match["goals"]["home"]
        goals_away = match["goals"]["away"]

        # Esperar para no saturar la API (ajusta si tienes plan PRO)
        time.sleep(1)
        stats = get_stats(fixture_id)

        # Crear diccionario base
        stats_dict = {
            "fixture_id": fixture_id,
            "season": season,
            "date": date,
            "home_team": home_team,
            "away_team": away_team,
            "goals_home": goals_home,
            "goals_away": goals_away,
        }

        # Añadir estadísticas por equipo
        for team_stats in stats:
            team = team_stats["team"]["name"]
            for s in team_stats["statistics"]:
                key = s["type"].lower().replace(" ", "_")
                stats_dict[f"{team}_{key}"] = s["value"]

        all_data.append(stats_dict)

# Convertir todo a DataFrame
df = pd.DataFrame(all_data)

# Guardar en CSV
df.to_csv("liga_mx_stats_2012_2025.csv", index=False)
print("Guardado en liga_mx_stats_2012_2025.csv con", len(df), "partidos.")
