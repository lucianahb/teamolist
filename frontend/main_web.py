from flask import Flask, render_template, request, redirect
import sys
sys.path.append('.')

from backend.models.category import Category
from backend.models.seller import Seller
from backend.controller.log import write_log, list_logs # pylint: disable=import-error 
from backend.controller.marketplace import list_mkplaces, write_mkplace # pylint: disable=import-error 
from backend.controller.product import list_products, write_product # pylint: disable=import-error 
from backend.controller.seller import list_sellers, write_seller # pylint: disable=import-error 
from backend.controller.category import list_categories, write_category # pylint: disable=import-error 

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


@app.route('/write-mkp')
def write_mkp():
    name = request.args.get('nome')
    description = request.args.get('descricao')
    
    write_mkplace(name, description)
    operation_type = 1 #1=write and 2=list
    write_log('writen Marketplace', operation_type)
    return redirect('/list-mkp')


@app.route('/write-product')
def write_prod():
    data = []
    data.append([request.args.get('nome'),request.args.get('descricao'),request.args.get('preco')])
    write_product(data[0])
    operation_type = 1 #1=write and 2=list
    write_log('writen Product', operation_type)
    return redirect('/list-product')


@app.route('/write-seller')
def write_sel():
    name = request.args.get('nome')
    email = request.args.get('email')
    telefone = request.args.get('telefone')
    seller = Seller(name,telefone,email)
    write_seller(seller)
    return redirect('/list-seller')


@app.route('/write-category')
def write_cat():
    name = request.args.get('nome')
    description = request.args.get('nome')
    category = Category(name,description)
    write_category(category)
    return redirect('/list-category')


@app.route('/list-mkp')
def list_mkp():
    final_list = list_mkplaces()
    operation_type = 2 #1=write and 2=list
    write_log('Listed Marketplace', operation_type)
    return render_template('list_mkp.html', list=final_list, write_log=write_log)


@app.route('/list-product')
def list_product():
    final_list = list_products()
    operation_type = 2 #1=write and 2=list
    write_log('Listed Product', operation_type)
    return render_template('list_product.html', list=final_list, write_log=write_log)


@app.route('/list-seller')
def list_seller():
    final_list = list_sellers()
    print('aaaaaaaaaaaaaaa')
    print(final_list)
    return render_template('list_seller.html', list=final_list, write_log=write_log)


@app.route('/list-category')
def list_category():
    final_list = list_categories()
    return render_template('list_category.html', list=final_list, write_log=write_log)


@app.route('/list-log')
def list_log():
    final_list = list_logs()
    return render_template('list_log.html', list=final_list)

app.debug = True

app.run()