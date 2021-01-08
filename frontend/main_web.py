from flask import Flask, render_template, request, redirect
import sys
sys.path.append('.')
from backend.log import save_log, list_logs
from backend.marketplace import list_mkplaces, save_mkplace
from backend.product import list_products, save_product
from backend.seller import list_sellers, save_seller
from backend.category import list_categories, save_category

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
    return render_template('form-product.html', titulo='Product')


@app.route('/form-seller')
def form_seller():
    return render_template('form-seller.html', titulo='Seller')


@app.route('/form-category')
def form_category():
    return render_template('form-category.html', titulo='Category')


@app.route('/save-mkp')
def save_mkp():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    data = f'{nome};{desc}'
    save_mkplace(data)
    save_log('Saved Marketplace')
    return redirect('/list-mkp')


@app.route('/save-product')
def save_prod():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    data = f'{nome};{desc};{preco}'
    save_product(data)
    save_log('Saved Product')
    return redirect('/list-product')


@app.route('/save-seller')
def save_sel():
    nome = request.args.get('nome')
    email = request.args.get('email')
    telefone = request.args.get('telefone')
    data = f'{nome};{email};{telefone}'
    save_seller(data)
    save_log('Saved Seller')
    return redirect('/list-seller')


@app.route('/save-category')
def save_cat():
    nome = request.args.get('nome')
    data = f'{nome}'
    save_category(data)
    save_log('Saved Category')
    return redirect('/list-category')


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

@app.route('/list-seller')
def list_seller():
    final_list = list_sellers()
    save_log('Listed Seller')
    return render_template('list_seller.html', list=final_list)


@app.route('/list-category')
def list_category():
    final_list = list_categories()
    save_log('Listed Category')
    return render_template('list_category.html', list=final_list)

@app.route('/list-log')
def list_log():
    final_list = list_logs()
    return render_template('list_log.html', list=final_list)

app.debug = True

app.run()