from colorama import Cursor
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome,tel) VALUES (%s,%s)'
args = ('Lucas', '98607-4321')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Error:  {e.msg}')
    else:
        print('1 registro incluído, ID:', cursor.lastrowid)