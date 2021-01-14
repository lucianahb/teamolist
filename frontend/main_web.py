from flask import Flask, render_template, request, redirect
import sys
sys.path.append('.')
from backend.controller.log import write_log, list_logs 
from backend.controller.marketplace_controller import MarketplaceController
from backend.controller.product_controller import ProductController
from backend.controller.seller import list_sellers, write_seller, list_seller_by_id, update_sel, del_sel 
from backend.controller.category import list_categories, write_category, get_category_by_id, update_category, delete_category 
from backend.models.product_model import Product
from backend.models.marketplace_model import Marketplace
from backend.models.category import Category
from backend.models.seller import Seller

app = Flask(__name__)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html', titulo='Marketplace Olist')


@app.route('/marketplace')
def form_mkp():
    return render_template('form-mkp.html', titulo='Marketplace')


@app.route('/product')
def form_product():
    return render_template('form-product.html', titulo='Product')


@app.route('/seller')
def form_seller():
    return render_template('form-seller.html', titulo='Seller')


@app.route('/category')
def form_category():
    return render_template('form-category.html', titulo='Category')


@app.route('/write-mkp')
def write_mkp():
    name = request.args.get('nome')
    description = request.args.get('descricao')
    controller = MarketplaceController()
    controller.create(Marketplace(name, description))
    return redirect('/list_mkp')


@app.route('/write-product')
def write_prod():
    name = request.args.get('nome')
    description = request.args.get('descricao')
    price = request.args.get('preco')
    controller = ProductController()
    controller.create(Product(name, description, price))
    return redirect('/list_product')


@app.route('/write-seller')
def write_sel():
    name = request.args.get('nome')
    email = request.args.get('email')
    telefone = request.args.get('telefone')
    seller = Seller(name,telefone,email)
    write_seller(seller)
    return redirect('/list_seller')


@app.route('/write-category')
def write_cat():
    name = request.args.get('nome')
    description = request.args.get('description')
    category = Category(name,description)
    write_category(category)
    return redirect('/list_category')

@app.route('/update-seller')
def updateseller():
    name = request.args.get('nome')
    email = request.args.get('email')
    phone = request.args.get('telefone')
    id = request.args.get('id')
    seller = Seller(name,phone,email,id)
    update_sel(seller)
    return redirect('list_seller')

@app.route('/update-marketplace')
def updatemarketplace():
    name = request.args.get('nome')
    description = request.args.get('descricao')
    id = request.args.get('id')
    marketplace = Marketplace(name,description,id)
    controller = MarketplaceController()
    controller.update(marketplace)
    return redirect('list_mkp')

@app.route('/update_marketplace')
def form_update_mkp():
    id = request.args.get('id')
    controller = MarketplaceController()
    marketplace = controller.read_by_id(id)
    return render_template('form-update-mkp.html', mkp= marketplace)

@app.route('/update_seller')
def form_update_seller():
    id = request.args.get('id')
    seller = list_seller_by_id(id)
    return render_template('form-update-seller.html', seller= seller)
    
@app.route('/deletemarketplace')
def deletemarketplace():
    id = request.args.get('id')
    controller = MarketplaceController()
    controller.delete(id)
    return redirect('list_mkp')

@app.route('/deleteseller')
def deleteseller():
    id = request.args.get('id')
    del_sel(id)
    return redirect('list_seller')

@app.route('/list_mkp')
def list_mkp():
    controller = MarketplaceController()
    final_list = controller.read_all()
    return render_template('list_mkp.html', list=final_list)


@app.route('/list_product')
def list_product():
    controller = ProductController()
    final_list = controller.read_all()
    return render_template('list_product.html', list=final_list, write_log=write_log)


@app.route('/list_seller')
def list_seller():
    final_list = list_sellers()
    return render_template('list_seller.html', list=final_list, write_log=write_log)


@app.route('/list_category')
def list_category():
    final_list = list_categories()
    return render_template('list_category.html', list=final_list, write_log=write_log)


@app.route('/list_log')
def list_log():
    final_list = list_logs()
    return render_template('list_log.html', list=final_list)


@app.route('/update_category')
def form_updatecategory():
    category = get_category_by_id(request.args.get('category_id'))
    return render_template('change-category.html', category = category)


@app.route('/update-category')
def u_category():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    category = Category(name,description, id)
    update_category(category)
    return redirect('/list-category')


@app.route('/delete_category')
def d_category():
    category = get_category_by_id(request.args.get('category_id'))
    delete_category(category)
    return redirect('/list-category')


@app.route('/update_product')
def form_updateproduct():
    controller = ProductController()
    product = controller.read_by_id(request.args.get('product_id'))
    return render_template('change-product.html', product = product)


@app.route('/update-product')
def u_product():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    product = Product(name,description, price, id)
    controller = ProductController()
    controller.update(product)
    return redirect('/list_product')


@app.route('/delete_product')
def d_product():
    controller = ProductController()
    controller.delete(request.args.get('product_id'))
    return redirect('/list_product')

app.debug = True

app.run()