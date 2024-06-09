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


    def adicionarFilme(self, titulo, sinopse, data_lancamento, locado=False):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO filmes (titulo, sinopse, data_lancamento, locado) VALUES (%s, %s, %s, %s)",
                    (titulo, sinopse, data_lancamento, locado)
                )
                self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise e

    def lerFilmes(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT id, titulo, sinopse, data_lancamento, locado FROM filmes")
                return cursor.fetchall()
        except psycopg2.Error as e:
            raise e

    def atualizarFilme(self, filme_id, titulo, sinopse, data_lancamento):
            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(
                        "UPDATE filmes SET titulo = %s, sinopse = %s, data_lancamento = %s WHERE id = %s",
                        (titulo, sinopse, data_lancamento, filme_id)
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

    def adicionarFilmesDaApi(self, listaFilmes):
        for filme in listaFilmes:
            titulo = filme.get('titulo')
            sinopse = filme.get('sinopse')
            dataLancamento = filme.get('data')
            if titulo and dataLancamento and sinopse:
                if not self.filmeExiste(titulo): #verifica se o filme ja esta adicionado no banco
                    self.adicionarFilme(titulo, sinopse, dataLancamento)

    def filmeExiste(self, titulo):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT EXISTS(SELECT 1 FROM filmes WHERE titulo = %s)", (titulo,)) #SELECT EXISTS retorna um valor booleano
                return cursor.fetchone()[0]  #Retorna True se o filme existe
        except psycopg2.Error as e:
            raise e

    def atualizarStatusLocacao(self, filme_id, locado):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE filmes SET locado = %s WHERE id = %s",
                    (locado, filme_id)
                )
                self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise e