from database import get_connection

def atualizar():
    # Aqui você faria o update dos dados da API ou CSV
    # Por enquanto vamos simular 5 registros importados
    conn = get_connection()
    c = conn.cursor()

    # Exemplo de atualização dummy
    c.execute("INSERT INTO times (nome) VALUES (?)", ("Time A",))
    c.execute("INSERT INTO times (nome) VALUES (?)", ("Time B",))
    conn.commit()
    conn.close()

    return 5  # número de registros importados
