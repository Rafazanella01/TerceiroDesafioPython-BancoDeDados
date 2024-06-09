from DataBase.Db import Db
from front import index
from app import Api, filmesPopulares

db = Db()
api = Api()  
   
# Criar um novo filme
#db.adicionarFilme("A volta dos que não foram", "Léo Reutter", 2023, Fantasia")

# Ler todos os filmes
#filmes = db.lerFilmes()
#for filme in filmes:
#    print(filme)

# Atualizar um filme
#db.atualizarFilme(1, "Star Wars: Episódio IV - Uma Nova Esperança", "George Lucas", 1977, "Aventura, Fantasia")

#Excluir um filme
#db.excluirFilme(1)

#index()

filmes = api.obterFilmesPopulares()

db.adicionarFilmesDaApi(filmes)