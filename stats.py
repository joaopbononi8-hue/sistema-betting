def calc_prob(est):
    # Calcula probabilidades fictícias para cada jogo
    total_chutes = sum(s["chutes_no_gol"] for s in est)
    total_esc = sum(s["escanteios"] for s in est)
    if total_chutes + total_esc == 0:
        return {"casa": 0.5, "fora": 0.5}
    return {
        "casa": total_chutes / (total_chutes + total_esc),
        "fora": total_esc / (total_chutes + total_esc)
    }

def calcular_odds(est):
    prob = calc_prob(est)
    # Odds = 1/probabilidade
    return {
        "casa": round(1 / max(prob["casa"], 0.01), 2),
        "fora": round(1 / max(prob["fora"], 0.01), 2)
    }
