from config.conexao import conectar


class Filme:
    def consultar_tudo(self):
        con = conectar()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Filmes")
        filmes = cursor.fetchall()
        for f in filmes:
            f["nota"] = float(f["nota"])
        cursor.close()
        con.close()
        return filmes

    def consultar_por_id(self, id):
        con = conectar()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Filmes WHERE id = %s", (id,))
        filme = cursor.fetchone()
        if filme:
            filme["nota"] = float(filme["nota"])
        cursor.close()
        con.close()
        return filme

    def cadastrar(self, dados):
        con = conectar()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO Filmes (titulo, diretor, genero, ano, duracao, nota) VALUES (%s, %s, %s, %s, %s, %s)",
            (dados["titulo"], dados["diretor"], dados["genero"], dados["ano"], dados["duracao"], dados["nota"])
        )
        con.commit()
        novo_id = cursor.lastrowid
        cursor.close()
        con.close()
        return novo_id

    def atualizar(self, id, dados):
        con = conectar()
        cursor = con.cursor()
        cursor.execute(
            "UPDATE Filmes SET titulo=%s, diretor=%s, genero=%s, ano=%s, duracao=%s, nota=%s WHERE id=%s",
            (dados["titulo"], dados["diretor"], dados["genero"], dados["ano"], dados["duracao"], dados["nota"], id)
        )
        con.commit()
        cursor.close()
        con.close()

    def excluir(self, id):
        con = conectar()
        cursor = con.cursor()
        cursor.execute("DELETE FROM Filmes WHERE id = %s", (id,))
        con.commit()
        cursor.close()
        con.close()
