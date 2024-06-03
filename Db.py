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