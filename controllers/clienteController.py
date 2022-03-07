import services.database as db
import models.Cliente as cliente

def incluir(cliente):
    # Sample insert query
    count = db.cursor.execute("""
    INSERT INTO dbo.Clientes (Nome, Idade, profissao) 
    VALUES (?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM Clientes")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))

    return costumerList
