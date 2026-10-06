from flask import jsonify


def resposta(dados, status=200):
    return jsonify(dados), status
