from flask import Flask, jsonify
import json
from flask_cors import CORS
from database import Funcs

class Util():
    def buildAPI(): 
        # Build API Flask
        app = Flask(__name__)
        CORS(app)

        # insert new user:
        @app.route('/get/<nome>/<idade>', methods=['GET'])
        def insert_user(nome,idade):
            funcs = Funcs()
            mensagem = funcs.insert_user(nome,idade)
            return jsonify(mensagem)
        
        # get all users
        @app.route('/', methods=['GET'])
        def get_all_users():
            funcs = Funcs()
            array_all_users = funcs.get_all_user_database()
            return jsonify(array_all_users)     

        # get all users
        @app.route('/delete/<id>', methods=['GET'])
        def delete_one_user(id):
            funcs = Funcs()
            mensagem = funcs.delete_user(id)
            return jsonify(mensagem)      

        # get information OLNY one user
        @app.route('/get-one-user/<id>', methods=['GET'])
        def get_one_user(id):
            funcs = Funcs()
            usuario = funcs.get_one_user(id)
            return jsonify(usuario)   
        
        # update one user
        @app.route('/update/<id>/<nome>/<idade>', methods=['GET'])
        def update_one_user(id, nome, idade):
            funcs = Funcs()
            mensagem = funcs.update_one_user(id,nome,idade)
            return jsonify(mensagem)   
        
        app.run(port=5000,host='localhost',debug=True)