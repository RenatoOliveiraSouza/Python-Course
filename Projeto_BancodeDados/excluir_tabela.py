from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE emails')
        # DROP TABEL IF EXISTS emails
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')