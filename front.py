from Db import Db

db = Db()

def index():
    try:
        escolha = 0
        while escolha != 6:
            print("""
                |-----------------------------|
                        Seja bem vindo!   
                
                Selecione o indice:

                1 - Locar filme
                2 - Devolver filmer
                3 - Incluir filme
                4 - Manutenir filme
                5 - Excluir filme
                6 - Sair

                """)


            escolha = (input("-->"))

            match escolha:
                case "1":
                    locarFilme()
                case "2":
                    devolverFilme()
                case "3":
                    addFilme()
                case "4":
                    editFilme()
                case "5":
                    removerFilme()   
            
    except ValueError as error:
        print(error)

def addFilme():
    titulo = (input("Qual o nome do filme? "))
    diretor = (input("Qual o nome do diretor? "))
    ano = int(input("Qual o ano de lançamento? "))
    genero = (input("Qual o genero do filme? "))

    db.adicionarFilme(titulo, diretor, ano, genero)

    print("Filme adicionado!")


def locarFilme():
    db.lerFilmes()



def devolverFilme():
    print()

def editFilme():
    db.lerFilmes()

    id = int(input("Qual o id do filme que deseja editar? "))

    titulo = (input("Qual o novo nome do filme? "))
    diretor = (input("Qual o novo nome do diretor? "))
    ano = int(input("Qual o novo ano de lançamento? "))
    genero = (input("Qual o novo genero do filme? "))

    db.atualizarFilme(id, titulo, diretor, ano, genero)


def removerFilme():
    db.lerFilmes()

    id = int(input("Qual o id do filme que deseja remover? "))

    db.excluirFilme(id)