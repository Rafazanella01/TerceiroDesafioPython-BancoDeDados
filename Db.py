import psycopg2 

class Db:
    def __init__(self):
        self.conn = self.conectar()

    def verificaConexao(self):
        if not self.conn or self.conn.closed:
            self.conn = self.conectar

    def conectar(self):
        try:
            return psycopg2.connect(
                dbname="locadora",
                user="root",
                password="root",
                host="localhost",
                port="5432"
            )
        except psycopg2.Error as e:
            raise e


    def adicionarFilme(self, titulo, diretor, ano, genero):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO filmes (titulo, diretor, ano, genero) VALUES (%s, %s, %s, %s)",
                    (titulo, diretor, ano, genero)
                )
                self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise e

    def lerFilmes(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT id, titulo, diretor, ano, genero FROM filmes")
                return cursor.fetchall()
        except psycopg2.Error as e:
            raise e

    def atualizarFilme(self, filme_id, titulo, diretor, ano, genero):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE filmes SET titulo = %s, diretor = %s, ano = %s, genero = %s WHERE id = %s",
                    (titulo, diretor, ano, genero, filme_id)
                )
                self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise e

    def excluirFilme(self, filme_id):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("DELETE FROM filmes WHERE id = %s", (filme_id,))
                self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise e