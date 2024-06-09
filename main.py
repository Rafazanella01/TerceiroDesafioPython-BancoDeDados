from DataBase.Db import Db
from front import index
from app import Api, filmesPopulares

db = Db()
api = Api()  

filmes = filmesPopulares()
db.adicionarFilmesDaApi(filmes)

index()