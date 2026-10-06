from flask import request
from model.filme import Filme
from view.filme_view import resposta

filme = Filme()


def consultar_tudo():
    return resposta(filme.consultar_tudo())


def consultar_por_id(id):
    resultado = filme.consultar_por_id(id)
    if resultado is None:
        return resposta({"erro": "Filme nao encontrado"}, 404)
    return resposta(resultado)


def cadastrar():
    dados = request.get_json()
    novo_id = filme.cadastrar(dados)
    return resposta({"mensagem": "Filme cadastrado", "id": novo_id}, 201)


def atualizar(id):
    if filme.consultar_por_id(id) is None:
        return resposta({"erro": "Filme nao encontrado"}, 404)
    dados = request.get_json()
    filme.atualizar(id, dados)
    return resposta({"mensagem": "Filme atualizado"})


def excluir(id):
    if filme.consultar_por_id(id) is None:
        return resposta({"erro": "Filme nao encontrado"}, 404)
    filme.excluir(id)
    return resposta({"mensagem": "Filme excluido"})
