from flask import Flask, render_template, url_for, redirect, jsonify
from flask import request, Response

from flask_cors import CORS

import json

import requests

import pandas as pd

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(__name__)
CORS(app)

@app.route('/v1.0/')
def home():
    return render_template("/home.html")

@app.route('/v1.0/alunos/')
def alunos():

    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/alunos/"

    alunos_request = requests.get(url_inicial + url_final)

    alunos = alunos_request.json()

    return render_template("/alunos/alunos.html", alunos = alunos)

@app.route('/v1.0/alunos/delete/<int:aluno_id>')
def alunos_delete_get(aluno_id):

    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/aluno/" + str(aluno_id)

    aluno_request = requests.get(url_inicial + url_final)

    aluno = aluno_request.json() 

    return render_template("/alunos/delete.html", aluno = aluno)

@app.route('/v1.0/alunos/update/<int:aluno_id>')
def aluno_update_get(aluno_id):
    
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/aluno/" + str(aluno_id)

    aluno_request = requests.get(url_inicial + url_final)

    aluno = aluno_request.json() 

    return render_template('/alunos/update.html', aluno = aluno)

@app.route('/v1.0/alunos/insert/')
def aluno_insert_get():
    return render_template('/alunos/insert.html')

@app.route('/v1.0/perguntas/')
def perguntas():
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/perguntas/"

    perguntas_request = requests.get(url_inicial + url_final)

    perguntas = perguntas_request.json()

    return render_template("/perguntas/perguntas.html", perguntas = perguntas)

@app.route('/v1.0/perguntas/pergunta/<int:pergunta_id>')
def perguntas_pergunta(pergunta_id):
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/perguntas/" + str(pergunta_id)

    pergunta_request = requests.get(url_inicial + url_final)

    pergunta = pergunta_request.json()

    #pergunta_id = pergunta['pergunta_id']

    url_final = "/v1.0/pergunta_has_tabela/" + str(pergunta_id)

    pergunta_has_tabela_request = requests.get(url_inicial + url_final)

    pergunta_has_tabelas = pergunta_has_tabela_request.json()

    print("ANTES DE ENTRAR NO LOOP")
    print("##################################################")
    print(pergunta_has_tabelas)

    tabelas = []
    for each in pergunta_has_tabelas:
        print("EACH: ", each)
        url_final = "/v1.0/tabela/" + str(each['tabela_Tabela_id'])

        tabela_request = requests.get(url_inicial + url_final)

        tabela = tabela_request.json()

        tabelas.append(tabela)

    return render_template('/perguntas/pergunta.html', pergunta = pergunta, tabelas= tabelas) 

@app.route('/v1.0/perguntas/delete/<int:pergunta_id>')
def perguntas_delete_get(pergunta_id):
    
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/perguntas/" + str(pergunta_id)

    pergunta_request = requests.get(url_inicial + url_final)

    pergunta = pergunta_request.json() 

    return render_template("/perguntas/delete.html", pergunta = pergunta)

@app.route('/v1.0/perguntas/update/<int:pergunta_id>')
def perguntas_update_get(pergunta_id):
    
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/perguntas/" + str(pergunta_id)

    pergunta_request = requests.get(url_inicial + url_final)

    pergunta = pergunta_request.json()

    return render_template('/perguntas/update.html', pergunta = pergunta)    

@app.route('/v1.0/perguntas/insert/')
def pergunta_insert_get():
    return render_template('/perguntas/insert.html')

@app.route('/v1.0/respostas/')
def respostas():

    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/respostas/" 

    respostas_request = requests.get(url_inicial + url_final)

    respostas = respostas_request.json()

    return render_template('/respostas/respostas.html', respostas = respostas)

@app.route('/v1.0/respostas/resposta/<int:resposta_id>')
def respostas_resposta(resposta_id):
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/respostas/" + str(resposta_id)

    resposta_request = requests.get(url_inicial + url_final)

    resposta = resposta_request.json()

    url_final = "/v1.0/resposta_has_tabela/" + str(resposta_id) + "/" + str(resposta['aluno_aluno_id'])+ "/" + str(resposta['pergunta_pergunta_id']) + "/"

    print("respostas_resposta: url_inicial + url_final: ", url_inicial + url_final)

    resposta_has_tabela_request = requests.get(url_inicial + url_final)

    print("respostas_resposta: respostas_has_tabela_request: ", resposta_has_tabela_request)
    print("respostas_resposta: dir(respostas_has_tabela_request)", dir(resposta_has_tabela_request))
    print("respostas_resposta: respostas_has_tabela_request.json", resposta_has_tabela_request.json)


    resposta_has_tabelas = resposta_has_tabela_request.json()

    tabelas = []
    for each in resposta_has_tabelas:
        print("EACH: ", each)
        url_final = "/v1.0/tabela/" + str(each['tabela_Tabela_id'])

        tabela_request = requests.get(url_inicial + url_final)

        tabela = tabela_request.json()

        tabelas.append(tabela)

    return render_template('/respostas/resposta.html', resposta = resposta, tabelas= tabelas)

@app.route('/v1.0/respostas/insert/')
def resposta_insert_get():
    return render_template('/respostas/insert.html')

@app.route('/v1.0/respostas/update/<int:resposta_id>')
def resposta_update_get(resposta_id):
        
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/respostas/" + str(resposta_id)

    resposta_request = requests.get(url_inicial + url_final)

    resposta = resposta_request.json()

    return render_template('/respostas/update.html', resposta = resposta)

@app.route('/v1.0/respostas/delete/<int:resposta_id>')
def resposta_delete_get(resposta_id):
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/respostas/" + str(resposta_id)

    resposta_request = requests.get(url_inicial + url_final)

    resposta = resposta_request.json()

    return render_template('/respostas/delete.html', resposta = resposta)

@app.route('/v1.0/resultados/')
def resultados():

    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/resultados/" 

    resultados_request = requests.get(url_inicial + url_final)

    resultados = resultados_request.json()

    return render_template('/resultados/resultados.html', resultados = resultados)

@app.route('/v1.0/resultados/insert/')
def resultado_insert_get():
    return render_template('/resultados/insert.html')

@app.route('/v1.0/resultados/update/<int:resultado_id>')
def resultado_update_get(resultado_id):
        
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/resultados/" + str(resultado_id)

    resultado_request = requests.get(url_inicial + url_final)

    resultado = resultado_request.json()

    return render_template('/resultados/update.html', resultado = resultado)

@app.route('/v1.0/resultados/delete/<int:resultado_id>')
def resultado_delete_get(resultado_id):
    url_inicial = "http://127.0.0.1:80"

    url_final = "/v1.0/resultados/" + str(resultado_id)

    resultado_request = requests.get(url_inicial + url_final)

    resultado = resultado_request.json()

    return render_template('/resultados/delete.html', resultado = resultado)

@app.route('/v1.0/tabelas/')
def tabelas():
    return 

@app.route('/v1.0/tabela/<int:tabela_id>')
def tabelas_tabela(tabela_id):
    url_inicial = "http://127.0.0.1:80"

    url_final_tabela = "/v1.0/tabela/" + str(tabela_id)

    tabela_request = requests.get(url_inicial + url_final_tabela)

    tabela = tabela_request.json()

    return render_template('/tabelas/tabela.html', tabela = tabela)

if __name__ == '__main__':
    app.run(port=3000,debug=True)