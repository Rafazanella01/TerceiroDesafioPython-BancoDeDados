from flask import Flask, jsonify
import requests

class Api:

    # INICIALIZA API DE FILMES
    def __init__(self):
        self.apiKey = '932e4d7335a59f02412b36b1fe88253e'
        self.urlBase = 'https://api.themoviedb.org/3'
        self.idioma = 'pt-BR'


    # FILTRA E OBTEM OS FILMES E RETORNA A LISTA
    def obterFilmes(self, tipoFilme):
        url = f"{self.urlBase}/movie/{tipoFilme}?api_key={self.apiKey}&language={self.idioma}"
        response = requests.get(url)
        dados = response.json()
        filmesFiltrados = [{'titulo': filme['title'], 'sinopse': filme['overview'], 'data': filme['release_date']} for filme in dados['results']]
        return filmesFiltrados

app = Flask(__name__)
api = Api()

#rota do flask localmente
@app.route('/filmes/populares', methods=['GET'])
def filmesPopulares():
        dados = api.obterFilmes('popular')
        return dados