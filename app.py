from flask import Flask, jsonify
import requests

app = Flask(__name__)

banco_de_dados = {}
relacao_ids = 0

def gerador_de_id():
    relacao_ids += 1
    return relacao_ids

@app.route('/users', methods=['GET'])
def get_users():
    dados = banco_de_dados
    return jsonify(dados), 200

@app.route('/users/create', methods=['POST'])
def create_users():
    current_id = gerador_de_id()
    nome = input("Nome? ")
    email = input("e-mail? ")

if __name__ == '__main__':
    app.run(debug=True)