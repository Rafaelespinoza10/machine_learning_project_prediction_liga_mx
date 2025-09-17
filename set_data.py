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
    return res.get("response", [])

def get_stats(fixture_id):
    """Trae estadísticas de un partido específico."""
    url = "https://v3.football.api-sports.io/fixtures/statistics"
    params = {"fixture": fixture_id}
    res = requests.get(url, headers=headers, params=params).json()
    return res.get("response", [])

# 🔹 Temporadas 2012–2025
for season in range(2021, 2024):
    print(f"\n📅 Descargando temporada {season}...")
    fixtures = get_fixtures(season)
    season_data = []

    for i, match in enumerate(fixtures, start=1):
        fixture_id = match["fixture"]["id"]
        home_team = match["teams"]["home"]["name"]
        away_team = match["teams"]["away"]["name"]
        date = match["fixture"]["date"]
        goals_home = match["goals"]["home"]
        goals_away = match["goals"]["away"]

        # Esperar un poco para no saturar la API (FREE → 100 requests/día)
        time.sleep(1)

        stats = get_stats(fixture_id)

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

        season_data.append(stats_dict)

        if i % 20 == 0:
            print(f"   → Procesados {i}/{len(fixtures)} partidos")

    # Guardar temporada
    df = pd.DataFrame(season_data)
    df.to_csv(f"liga_mx_{season}.csv", index=False)
    print(f"✅ Temporada {season} guardada con {len(df)} partidos en liga_mx_{season}.csv")
