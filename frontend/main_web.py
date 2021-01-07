from flask import Flask, render_template, request, redirect
import sys
sys.path.append('.')
from backend.log import save_log
from backend.marketplace import list_mkplaces, save_mkplace
from backend.product import list_products, save_product

app = Flask(__name__)

    
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html', titulo='Marketplace Olist')


@app.route('/form-mkp')
def form_mkp():
    return render_template('form-mkp.html', titulo='Marketplace')


@app.route('/form-product')
def form_product():
    return render_template('form-product.html', titulo='Produto')


@app.route('/save-mkp')
def save_mkp():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    data = f'{nome};{desc}'
    save_mkplace(data)
    save_log('Save Marketplace')
    return redirect('/list-mkp')


@app.route('/save-product')
def save_prod():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    data = f'{nome};{desc};{preco}'
    save_product(data)
    save_log('Save Product')
    return redirect('/list-product')


@app.route('/list-mkp')
def list_mkp():
    final_list = list_mkplaces()
    save_log('Listed Marketplace')
    return render_template('list_mkp.html', list=final_list)


@app.route('/list-product')
def list_product():
    final_list = list_products()
    save_log('Listed Product')
    return render_template('list_product.html', list=final_list)

app.debug = True

app.run()