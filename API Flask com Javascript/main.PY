# pip install flask pandas flask-cors

from flask import Flask, jsonify, request
import pandas as pd
import json
import os
from flask_cors import CORS

# montando dados via pandas
# tabela = pd.read_csv('./pratica_pandas/municipios.csv')
tabela = pd.read_csv('./municipios.csv')

# criando novo JSON -> todas capitais
selecao_capital = tabela.query('is_capital == True')
todas_capitais_ordem_alfabetica = selecao_capital.sort_values(by='uf_code').reset_index(drop=True)
todas_capitais_ordem_alfabetica['id'] = todas_capitais_ordem_alfabetica.index
capitais_json = todas_capitais_ordem_alfabetica.to_json(orient='records')

# buscar cidade e gerar JSON
def gerar_json_pesquisa(cidade):
    resultado_busca = tabela[tabela['slug_name'].str.contains(cidade, na=False)]
    resultado_busca = resultado_busca.to_json(orient='records')
    return resultado_busca

def gerar_cidades_estado(estado):
    resultado_busca = tabela.query(f'uf_code == "{estado}"')
    resultado_busca = resultado_busca.to_json(orient='records')
    return resultado_busca

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # consultar todas capitais:
    @app.route('/cidade', methods=['GET'])
    def obter_dados_cidade():
        json_limpo = json.loads(capitais_json)
        return json_limpo

    # busca cidade:
    @app.route('/cidade/<cidade>', methods=['GET'])
    def obter_dados_cidade_por_id(cidade):
        cidade = cidade.lower(); print(cidade)
        json_resultado = json.loads(gerar_json_pesquisa(cidade))
        return json_resultado
    
    # busca por estado:
    @app.route('/estado/<estado>', methods=['GET'])
    def obter_dados_ciades_estado(estado):
        json_resultado = json.loads(gerar_cidades_estado(estado))
        return json_resultado

    app.run(port=5000,host='localhost',debug=True)

# inicia a página.
os.system('start chrome %cd%\\index.html')

# monta a API
montar_API()
