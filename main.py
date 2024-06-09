from DataBase.Db import Db
from front import index
from app import Api, filmesPopulares

db = Db()
api = Api()  

filmes = filmesPopulares()
db.adicionarFilmesDaApi(filmes)

index()

"""
filmes = db.lerFilmes()

for filme in filmes:
    id, titulo, sinopse, dataLancamento = filme
    print(f"ID: {id}\nTítulo: {titulo}\nSinopse: {sinopse}\nData de Lançamento: {dataLancamento}\n{'='*30}")

"""
#db.excluirFilme(3)

