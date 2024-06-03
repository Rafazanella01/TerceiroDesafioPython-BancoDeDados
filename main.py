from Db import Db

db = Db()
    
# Criar um novo filme
#db.adicionarFilme("A volta dos que não foram", "Léo Reutter", 2023, Fantasia")

# Ler todos os filmes
filmes = db.lerFilmes()
for filme in filmes:
    print(filme)

# Atualizar um filme
#db.atualizarFilme(1, "Star Wars: Episódio IV - Uma Nova Esperança", "George Lucas", 1977, "Aventura, Fantasia")

#Excluir um filme
#db.excluirFilme(1)
