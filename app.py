from flask import Flask, jsonify
from database import init_db, get_connection
from updater import atualizar
from stats import calc_prob, calcular_odds

app = Flask(__name__)

@app.route('/api/update', methods=['POST'])
def update_data():
    # Atualiza os dados e retorna quantos registros foram importados
    return jsonify({'imported': atualizar()})

@app.route('/api/matches')
def matches():
    conn = get_connection()
    c = conn.cursor()

    # Busca os últimos 50 jogos com nomes dos times
    c.execute("""
        SELECT j.*, t1.nome AS home, t2.nome AS away
        FROM jogos j
        JOIN times t1 ON j.time_casa_id = t1.id
        JOIN times t2 ON j.time_fora_id = t2.id
        ORDER BY j.data_jogo DESC
        LIMIT 50
    """)

    jogos = c.fetchall()
    out = []

    for j in jogos:
        c.execute("SELECT * FROM estatisticas WHERE jogo_id=?", (j["id"],))
        st = c.fetchall()
        if not st:
            continue

        m = {
            "id": j["id"],
            "data": j["data_jogo"],
            "home": j["home"],
            "away": j["away"],
            "esc": sum(s["escanteios"] for s in st) / 2,
            "chutes": sum(s["chutes_no_gol"] for s in st) / 2,
            "cartoes": sum(s["amarelos"] for s in st) / 2,
            "probabilidades": calc_prob(st),
            "odds": calcular_odds(st)
        }
        out.append(m)

    conn.close()
    return jsonify(out)

if __name__ == "__main__":
    init_db()  # inicializa o banco se necessário
    app.run(host="0.0.0.0", port=5000, debug=True)
