from utils import load_data, load_template
from flask import request, redirect, url_for
from utils import add_note_to_json
# import sqlite3
def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)


def submit(titulo: str, detalhes: str):
    add_note_to_json(titulo, detalhes)
