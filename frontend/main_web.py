from flask import Flask, render_template, request
import sys
sys.path.append('.')
from backend.funcoes import write_file, log

# def create_app():
app = Flask(__name__)
    # Bootstrap(app)
    # return app
    
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html', titulo='Marketplace Olist')


@app.route('/cadastro')
def view_cadastro():
    opcao = request.args.get('opcao')
    if opcao == 'marketplace':
        return render_template('cadastro.html', titulo='Marketplace', op=opcao)
    elif opcao == 'produto':
        return render_template('cadastro.html', titulo='Produto', op=opcao)
    else:
        return render_template('index.html', titulo='Marketplace Olist')


@app.route('/gravar')
def gravar_dados():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    desc = str(desc).replace('*', '-').replace('%', '-')
    nome = str(nome).replace('*', '-').replace('%', '-')
    
    if preco is None:
        data = f'{nome};{desc}'
        write_file(0, data)
    else:
        data = f'{nome};{desc};{preco}'
        write_file(1, data)
    return render_template('index.html', titulo='Marketplace Olist')


app.debug = True

app.run()