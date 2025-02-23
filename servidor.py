from flask import Flask, render_template_string, request, redirect, url_for
import views
import utils

app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note_route(note_id):
    views.delete_note(note_id)
    return redirect(url_for('index'))

@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note_route(note_id):
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        detalhes = request.form.get('detalhes')
        views.edit_note(note_id, titulo, detalhes)
        return redirect(url_for('index'))
    else:
        return render_template_string(views.edit_note_form(note_id))

@app.errorhandler(404)
def page_not_found(e):
    return render_template_string(utils.load_template('404.html')), 404

if __name__ == '__main__':
    app.run(debug=True)