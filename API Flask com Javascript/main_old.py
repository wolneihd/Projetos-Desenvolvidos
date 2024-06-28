# pip install flask pandas flask-cors

from flask import Flask, jsonify, request
import pandas as pd
import json
import os
from flask_cors import CORS


# montando dados via pandas
# tabela = pd.read_csv('./pratica_pandas/municipios.csv')
tabela = pd.read_csv('./municipios.csv')
selecao_capital = tabela.query('is_capital == True')
mask = selecao_capital.sort_values(by='uf_code').reset_index(drop=True)

# criando novo JSON
qtd_dados = len(mask.index)
dict_todas_cidades = []
for index in range(0,qtd_dados):
    cidade_nova = {
        'id': index,
        'municipio': str(mask.iloc[index]['municipio']),
        'uf': str(mask.iloc[index]['uf']),
        'uf_code': str(mask.iloc[index]['uf_code']),
        'name': str(mask.iloc[index]['name']),
        'mesoregion': str(mask.iloc[index]['mesoregion']),
        'microregion': str(mask.iloc[index]['microregion']),
        'rgint': str(mask.iloc[index]['rgint']),
        'rgi': str(mask.iloc[index]['rgi']),
        'osm_relation_id': str(mask.iloc[index]['osm_relation_id']),
        'wikidata_id': str(mask.iloc[index]['wikidata_id']),
        'is_capital': str(mask.iloc[index]['is_capital']),
        'wikipedia_pt': str(mask.iloc[index]['wikipedia_pt']),
        'lon': str(mask.iloc[index]['lon']),
        'lat': str(mask.iloc[index]['lat']),
        'no_accents': str(mask.iloc[index]['no_accents']),
        'slug_name': str(mask.iloc[index]['slug_name']),
        'alternative_names': str(mask.iloc[index]['alternative_names']),
        'pop_21': str(mask.iloc[index]['pop_21'])
    }
    dict_todas_cidades.append(cidade_nova)

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # consultar todas cidades:
    @app.route('/cidade', methods=['GET'])
    def obter_dados_cidade():
        return jsonify(dict_todas_cidades)

    # consultar uma cidade:
    @app.route('/cidade/<int:id>', methods=['GET'])
    def obter_dados_cidade_por_id(id):
        for data in dict_todas_cidades:
            if data['id'] == id:
                cidade_id = json.dumps(data)
                return jsonify(data)

    app.run(port=5000,host='localhost',debug=True)

# inicia a página.
os.system('start chrome %cd%\\index.html')

# monta a API
montar_API()
