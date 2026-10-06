from flask import Flask
from flasgger import Swagger
from controller import filme_controller

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/filmes", methods=["GET"])
def consultar_tudo():
    """
    Consultar todos os filmes
    ---
    tags:
      - Filmes
    responses:
      200:
        description: Lista de filmes
    """
    return filme_controller.consultar_tudo()


@app.route("/filmes/<int:id>", methods=["GET"])
def consultar_por_id(id):
    """
    Consultar filme por ID
    ---
    tags:
      - Filmes
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Filme encontrado
      404:
        description: Filme nao encontrado
    """
    return filme_controller.consultar_por_id(id)


@app.route("/filmes", methods=["POST"])
def cadastrar():
    """
    Cadastrar filme
    ---
    tags:
      - Filmes
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            diretor:
              type: string
            genero:
              type: string
            ano:
              type: integer
            duracao:
              type: integer
            nota:
              type: number
    responses:
      201:
        description: Filme cadastrado
    """
    return filme_controller.cadastrar()


@app.route("/filmes/<int:id>", methods=["PUT"])
def atualizar(id):
    """
    Atualizar filme
    ---
    tags:
      - Filmes
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            diretor:
              type: string
            genero:
              type: string
            ano:
              type: integer
            duracao:
              type: integer
            nota:
              type: number
    responses:
      200:
        description: Filme atualizado
      404:
        description: Filme nao encontrado
    """
    return filme_controller.atualizar(id)


@app.route("/filmes/<int:id>", methods=["DELETE"])
def excluir(id):
    """
    Excluir filme
    ---
    tags:
      - Filmes
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Filme excluido
      404:
        description: Filme nao encontrado
    """
    return filme_controller.excluir(id)


if __name__ == "__main__":
    app.run(debug=True)
