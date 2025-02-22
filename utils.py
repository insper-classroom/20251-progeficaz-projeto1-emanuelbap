
def load_template(template_name: str) -> str: ### essa seta significa que a função deve retornar uma string 
    # Define o caminho completo para o template
    file_path = f'static/templates/{template_name}'

    # Lê o conteúdo do arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return content
    
