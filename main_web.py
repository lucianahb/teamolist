from flask import Flask, render_template, request
from funcoes import escrever_arquivo

app = Flask(__name__)
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


    if preco is None:
        dado = f'{nome},{desc}'
        escrever_arquivo(dado, 0, 'a')
    else:
        dado = f'{nome},{desc},{preco}'
        escrever_arquivo(dado, 1, 'a')

    return render_template('index.html', titulo='Marketplace Olist')


app.run()
