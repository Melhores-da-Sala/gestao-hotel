from dao import connection
from datetime import date

# ──────────────────────────────────────────
# HÓSPEDES
# ──────────────────────────────────────────


def consulta_hospedes():
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hospedes")
    retorno = cursor.fetchall()

    cursor.close()
    conn.close()

    return retorno


def consulta_hospede_id(id):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hospedes WHERE id = %s", (id,))
    retorno = cursor.fetchone()

    cursor.close()
    conn.close()

    return retorno


def add_hospede(nome, email, telefone, cpf):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        INSERT INTO hospedes (nome, email, telefone, cpf)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (nome, email, telefone, cpf))
    conn.commit()

    cursor.close()
    conn.close()


def update_hospede(id, nome, email, telefone, cpf):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        UPDATE hospedes
        SET nome     = %s,
            email    = %s,
            telefone = %s,
            cpf      = %s
        WHERE id = %s
    """

    cursor.execute(query, (nome, email, telefone, cpf, id))
    conn.commit()

    cursor.close()
    conn.close()


def delete_hospede(id):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("DELETE FROM hospedes WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()


# ──────────────────────────────────────────
# QUARTOS
# ──────────────────────────────────────────


def consulta_quartos():
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM quartos")
    retorno = cursor.fetchall()

    cursor.close()
    conn.close()

    return retorno


def consulta_quarto_id(id):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM quartos WHERE id = %s", (id,))
    retorno = cursor.fetchone()

    cursor.close()
    conn.close()

    return retorno


def add_quarto(numero, tipo, valor_diaria, status):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        INSERT INTO quartos (numero, tipo, valor_diaria, status)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (numero, tipo, valor_diaria, status))
    conn.commit()

    cursor.close()
    conn.close()


def update_quarto(id, numero, tipo, valor_diaria, status):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        UPDATE quartos
        SET numero       = %s,
            tipo         = %s,
            valor_diaria = %s,
            status       = %s
        WHERE id = %s
    """

    cursor.execute(query, (numero, tipo, valor_diaria, status, id))
    conn.commit()

    cursor.close()
    conn.close()


def delete_quarto(id):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("DELETE FROM quartos WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()


# ──────────────────────────────────────────
# RESERVAS
# ──────────────────────────────────────────


def consulta_reservas_ativas():
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT r.*,
               h.nome   AS nome_hospede,
               q.numero AS numero_quarto
        FROM reservas r
        JOIN hospedes h ON r.hospede_id = h.id
        JOIN quartos  q ON r.quarto_id  = q.id
        WHERE r.data_saida >= CURDATE()
    """

    cursor.execute(query)
    retorno = cursor.fetchall()

    cursor.close()
    conn.close()

    return retorno


def consulta_reservas_ativas():
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT r.*,
               h.nome   AS nome_hospede,
               q.numero AS numero_quarto
        FROM reservas r
        JOIN hospedes h ON r.hospede_id = h.id
        JOIN quartos  q ON r.quarto_id  = q.id
        WHERE r.data_saida >= CURDATE()
    """

    cursor.execute(query)
    retorno = cursor.fetchall()

    cursor.close()
    conn.close()

    return retorno


def consulta_reserva_id(id):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT r.*,
               h.nome   AS nome_hospede,
               q.numero AS numero_quarto
        FROM reservas r
        JOIN hospedes h ON r.hospede_id = h.id
        JOIN quartos  q ON r.quarto_id  = q.id
        WHERE r.id = %s
    """

    cursor.execute(query, (id,))
    retorno = cursor.fetchone()

    cursor.close()
    conn.close()

    return retorno


def add_reserva(hospede_id, quarto_id, data_entrada, data_saida):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        INSERT INTO reservas (hospede_id, quarto_id, data_entrada, data_saida)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (hospede_id, quarto_id, data_entrada, data_saida))
    conn.commit()

    cursor.close()
    conn.close()


def update_reserva(id, hospede_id, quarto_id, data_entrada, data_saida):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        UPDATE reservas
        SET hospede_id   = %s,
            quarto_id    = %s,
            data_entrada = %s,
            data_saida   = %s
        WHERE id = %s
    """

    cursor.execute(query, (hospede_id, quarto_id, data_entrada, data_saida, id))
    conn.commit()

    cursor.close()
    conn.close()


def delete_reserva(id):
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("DELETE FROM reservas WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

def consulta_todas_reservas():
    """Retorna TODAS as reservas (incluindo passadas) para a listagem e calendário."""
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT r.*,
               h.nome   AS nome_hospede,
               q.numero AS numero_quarto
        FROM reservas r
        JOIN hospedes h ON r.hospede_id = h.id
        JOIN quartos q ON r.quarto_id = q.id
        ORDER BY r.data_entrada
    """

    cursor.execute(query)
    retorno = cursor.fetchall()

    cursor.close()
    conn.close()

    # Converter datas para string (JSON serializable e compatível com as tabelas)
    for r in retorno:
        if hasattr(r.get('data_entrada'), 'isoformat'):
            r['data_entrada'] = r['data_entrada'].isoformat()
        
        if hasattr(r.get('data_saida'), 'isoformat'):
            r['data_saida'] = r['data_saida'].isoformat()

    return retorno


def obter_detalhes_reserva(reserva_id: int):
    """Retorna os detalhes de uma reserva específica gerenciando sua própria conexão."""
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT 
            r.id,
            r.hospede_id,
            r.quarto_id,
            r.data_entrada,
            r.data_saida,
            h.nome AS nome_hospede,
            h.cpf AS cpf_hospede,
            h.email AS email_hospede,
            h.telefone AS telefone_hospede,
            q.numero AS numero_quarto,
            q.tipo AS tipo_quarto,
            q.valor_diaria,
            DATEDIFF(r.data_saida, r.data_entrada) AS total_dias
        FROM reservas r
        INNER JOIN hospedes h ON r.hospede_id = h.id
        INNER JOIN quartos q ON r.quarto_id = q.id
        WHERE r.id = %s
    """
    
    cursor.execute(query, (reserva_id,))
    reserva = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    # Se a reserva existir, aplicamos as regras de negócio de cálculo
    if reserva:
        # Garante pelo menos 1 diária se o check-in/out for no mesmo dia
        if reserva["total_dias"] <= 0:
            reserva["total_dias"] = 1
            
        # Calcula o valor total estimado da estadia
        reserva["valor_total_estimado"] = reserva["total_dias"] * float(reserva["valor_diaria"])
        
        # Converte as datas para string no formato YYYY-MM-DD para o <input type="date"> reconhecer no form
        if hasattr(reserva.get('data_entrada'), 'isoformat'):
            reserva['data_entrada'] = reserva['data_entrada'].isoformat()
        if hasattr(reserva.get('data_saida'), 'isoformat'):
            reserva['data_saida'] = reserva['data_saida'].isoformat()
        
    return reserva