import os
from DataBase.Db import Db

db = Db()

def index():
    try:
        escolha = 0
        while escolha != "6":
            print("\n" * os.get_terminal_size().lines)
            print("""
                |-----------------------------|
                        Seja bem vindo!   
                
                Selecione o indice:

                1 - Locar filme
                2 - Devolver filme
                3 - Incluir filme
                4 - Manutenir filme
                5 - Excluir filme
                6 - Sair

                """)


            escolha = (input("-->"))

            print("\n" * os.get_terminal_size().lines)

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
    sinopse = (input("Qual a sinopse do filme? "))
    ano = (input("Qual a data de lançamento? "))

    db.adicionarFilme(titulo, sinopse, ano)


    print("\n" * os.get_terminal_size().lines)
    print("Filme adicionado com sucesso!")

    input("\n\nInfome qualquer tecla...")



def locarFilme():

    # CRIA UMA LISTA COM OS FILMES DO BD
    filmes = db.lerFilmes()

    Disponiveis = True

    # EXECUTA UM LAÇO PASSANDO POR CADA FILME
    for filme in filmes:
        id, titulo, sinopse, dataLancamento, locado = filme
        if not locado: # VERIFICA SE ESTA LOCADO
            print(f"ID: {id}\nTítulo: {titulo}\nSinopse: {sinopse}\nData de Lançamento: {dataLancamento}\n{'='*30}")
            Disponiveis = False

    if Disponiveis == True: # SE NÃO HOUVER NENHUM FILME DISPONIVEL
        print("Não há filmes disponíveis!")
        return

    idLocacao = int(input("Qual o ID do filme que será locado?"))

    VerificaId = [filme[0] for filme in filmes] # VERIFICA SE O ID INFORMADO EXISTE NO BD
    if idLocacao not in VerificaId:
        print("\n" * os.get_terminal_size().lines)
        print("ID inválido! Por favor, insira um ID válido.")     
        input("\n\nInfome qualquer tecla...")
        return

    try:
        # ATUALIZA O VALOR BOOLEANO NO BD
        db.atualizarStatusLocacao(idLocacao, True)
        print("\n" * os.get_terminal_size().lines)
        print("Filme locado com sucesso!")
        input("\n\nInfome qualquer tecla...")
    except Exception as e:
        # CASO ACONTEÇA ALGUM ERRO EVITA DE QUEBRAR A EXECUÇÃO
        print("\n" * os.get_terminal_size().lines)
        print(f"Erro ao locar o filme: {e}")
        input("\n\nInfome qualquer tecla...")



def devolverFilme():

    # CRIA UMA LISTA COM OS FILMES DO BD
    filmes = db.lerFilmes()

    Locados = False

    for filme in filmes: # EXECUTA UM LAÇO PASSANDO POR CADA FILME
        id, titulo, sinopse, dataLancamento, locado = filme
        if locado == True: # VERIFICA SE ESTA LOCADO
            print(f"ID: {id}\nTítulo: {titulo}\nSinopse: {sinopse}\nData de Lançamento: {dataLancamento}\n{'='*30}")
            Locados = True

    if not Locados:
        print("Não há filmes locados!")
        return

    idDevolucao = int(input("Qual o ID do filme que será devolvido?"))

    VerificaId = [filme[0] for filme in filmes] # PASSA PELO BD VERIFICANDO SE HÁ O ID INFORMADO PELO USUÁRIO
    if idDevolucao not in VerificaId:
        print("\n" * os.get_terminal_size().lines)
        print("ID inválido! Por favor, insira um ID válido.")     
        input("\n\nInfome qualquer tecla...")
        return

    try:

        # ATUALIZA O VALOR BOOLEANO NO BD
        db.atualizarStatusLocacao(idDevolucao, False)
        print("\n" * os.get_terminal_size().lines) 
        print("Filme devolvido com sucesso!")   
        input("\n\nInfome qualquer tecla...")
    except Exception as e:
        print("\n" * os.get_terminal_size().lines)
        print(f"Erro ao devolver o filme: {e}")
        input("\n\nInfome qualquer tecla...")
    


def editFilme():

    # CRIA UMA LISTA COM OS FILMES DO BD
    filmes = db.lerFilmes()

    for filme in filmes:
        id, titulo, sinopse, dataLancamento, locado = filme
        print(f"ID: {id}\nTítulo: {titulo}\nSinopse: {sinopse}\nData de Lançamento: {dataLancamento}\n{'='*30}")

    idEdit = int(input("Qual o ID do filme que será editado?"))

    VerificaId = [filme[0] for filme in filmes] # FAZ A VERIFICAÇÃO DO ID INFORMADO
    if idEdit not in VerificaId:
        print("\n" * os.get_terminal_size().lines)
        print("ID inválido! Por favor, insira um ID válido.")     
        input("\n\nInfome qualquer tecla...")
        return

    titulo = (input("Qual o novo nome do filme? "))
    sinopse = (input("Qual a nova sinopse do filme? "))
    ano = (input("Qual a nova data de lançamento? "))

    db.atualizarFilme(idEdit, titulo, sinopse, ano) # CHAMA A FUNÇÃO DE APP.PY PASSANDO AS NOVAS INFORMAÇÕES

    print("\n" * os.get_terminal_size().lines)     
    print("Atualizado com sucesso!")
    input("\n\nInfome qualquer tecla...")



def removerFilme():

    # CRIA UMA LISTA COM OS FILMES DO BD
    filmes = db.lerFilmes()

    for filme in filmes: # EXIBE OS FILMES CADASTRADOS
        id, titulo, sinopse, dataLancamento, locado = filme
        print(f"ID: {id}\nTítulo: {titulo}\nSinopse: {sinopse}\nData de Lançamento: {dataLancamento}\n{'='*30}")

    idDelete = int(input("Qual o id do filme que deseja remover? "))

    VerificaId = [filme[0] for filme in filmes] #VERIFICA O ID, SE EXISTE NO BD
    if idDelete not in VerificaId:
        print("\n" * os.get_terminal_size().lines)
        print("ID inválido! Por favor, insira um ID válido.")     
        input("\n\nInfome qualquer tecla...")
        return

    db.excluirFilme(idDelete) # EXCLUI O ID INFORMADO DO BANCO
    print("\n" * os.get_terminal_size().lines)     
    print("Excluido com sucesso!")
    input("\n\nInfome qualquer tecla...")