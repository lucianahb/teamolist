from flask import Flask, render_template, request
from funcoes import escrever_arquivo


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('base.html', titulo='Marketplace Olist')
