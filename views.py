from utils import load_template
from flask import redirect, url_for
import sqlite3

# Devo crir uma conecção com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('notes.db')
    # "row_factory" permite que as informações do banco de dados possam ser acessadas, tipo um dicionario
    # no futuro eu precisarei disso
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Criar a tabela notes --> caso ela não exista 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            detalhes TEXT NOT NULL
        )
    ''')
    # Salvar tudo e fechar o banco de dados 
    conn.commit()
    conn.close()

# Execute esta função uma vez para criar a tabela
create_table()

def index():
    note_template = load_template('components/note.html')

    # estabelecer uma conecção com o banco de dados 
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fazer uma consulta para pegar todos os titulos e detalhes das notas na tabela notes
    cursor.execute('SELECT id, titulo, detalhes FROM notes')
    
    # criar uma lista de notas formatadas usando o template html
    notes_li = [
        note_template.format(id=row['id'], title=row['titulo'], details=row['detalhes'])
        for row in cursor.fetchall()
    ]

    # Fechar a conecção com o banco de dados
    conn.close()

    # Juntar todas as notas em uma string que vai seprar pela quebra de linhas 
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo: str, detalhes: str):
    # Estabelecer a conecção novamente
    conn = get_db_connection()
    cursor = conn.cursor()
    # Inserir uma nova nota com o titulo e o detalhe fornecidos 
    cursor.execute('INSERT INTO notes (titulo, detalhes) VALUES (?, ?)', (titulo, detalhes))

    #Salvar as informações e fechar a conecção 
    conn.commit()
    conn.close()

    # Redirecionar o usuário 
    return redirect(url_for('index'))

def delete_note(note_id: int):
    # Estabelece a conecção
    conn = get_db_connection()
    cursor = conn.cursor()

    # Criar um comando SQLite para deletar a nota correspondente ao id 
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))

    #salvar tudo e fechar o banco de dados 
    conn.commit()
    conn.close()

def edit_note_form(note_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT titulo, detalhes FROM notes WHERE id = ?', (note_id,))
    note = cursor.fetchone()
    conn.close()
    return load_template('edit_note.html').format(id=note_id, title=note['titulo'], details=note['detalhes'])

def edit_note(note_id: int, titulo: str, detalhes: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE notes SET titulo = ?, detalhes = ? WHERE id = ?', (titulo, detalhes, note_id))
    conn.commit()
    conn.close()

