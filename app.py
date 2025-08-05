from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        imagem = request.files['image']
        pedido = request.form['pedido']
        add_phone = request.form['addPhone']
        telefone = request.form.get('telefone', '')

        filename_base = pedido.strip().replace(' ', '_')
        if add_phone == 'sim' and telefone.strip():
            telefone = telefone.strip().replace(' ', '').replace('-', '')
            filename_base += f'_({telefone})'

        ext = os.path.splitext(imagem.filename)[1]
        filename = secure_filename(filename_base + ext)
        imagem.save(os.path.join(UPLOAD_FOLDER, filename))

        return render_template('index.html', sucesso=filename)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)