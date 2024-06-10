# IMPORTA OS ARQUVIOS USADOS NO PROJETO
from DataBase.Db import Db
from front import index
from app import Api, filmesPopulares


#INSTANCIA AS FUNÇÕES
db = Db()
api = Api()  

filmes = filmesPopulares()
db.adicionarFilmesDaApi(filmes)


# EXECUTA O MENU
index()