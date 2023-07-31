import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'API esta no ar'

@app.route('/vendas')
def pegarvendas():
  tabela = pd.read_csv('advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)


# rodar API
app.run(host='0.0.0.0')

