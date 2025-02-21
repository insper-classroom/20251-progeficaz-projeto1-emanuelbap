import json
import os


def load_data(nome):
    #preciso achar o caminho do arquivo com o nome fornecido:
    # Com o "os.path.json([...])" --> eu consigo criar o caminho completo para o arquivo que eu quero buscar
    file_path = os.path.join('static', 'data', nome)
    #Agora, preciso abrir a pasta e transformar esse unico arquivo em um objeto python
    # 'r' seria para abrir o arquivo em modo padrão (tem varios outros modos)
    # tipo o modo 'a' que abre o arquivo para escrita no final. Tipo como se fosse um append 
    with open(file_path, 'r', encoding='utf-8') as file:
        arquivo = json.load(file)
    return arquivo

def load_template(template_name: str) -> str: ### essa seta significa que a função deve retornar uma string 
    # Define o caminho completo para o template
    file_path = f'static/templates/{template_name}'

    # Lê o conteúdo do arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return content

def add_note_to_json(titulo: str, detalhes: str):
    file_path = 'static/data/notes.json'
    
    # Lê o conteúdo atual do arquivo JSON
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    
    # Adiciona a nova anotação à lista
    new_note = {'titulo': titulo, 'detalhes': detalhes}
    notes.append(new_note)
    
    # Escreve a lista atualizada de volta no arquivo JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)
    
