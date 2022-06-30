from colorama import Cursor
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome,tel) VALUES (%s,%s)'
args = (
        ('Ana', '98687-4321'),
        ('Lara', '91677-1321'),
        ('Gabi', '94667-4321'),
        ('Lici', '95657-4321'),
        ('Bull', '93647-4321'),
        ('Bobe', '99637-4321'),
        ('Rafo', '97627-4321'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Error:  {e.msg}')
    else:
        print(f'{cursor.rowcount} rgistro incluidos')