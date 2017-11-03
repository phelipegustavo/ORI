# -*- coding: utf-8 -*-
from helpers.Index import *
from helpers.BooleanoRI import *
from helpers.OperacoesTexto import *
from helpers.VetorialRI import *
from flask import Flask, render_template, request
from operator import itemgetter
import webbrowser

app     = Flask(__name__)
QNT     = 10    # Quantidade de Documentos
indices = []    # Lista de objetos Indices
tfs     = []    # Lista de Arquivos Termo Frequencia

for i in range(QNT):
    arquivo = str(i+1)+".txt"
    indice = Index(arquivo)
    indice.indexar()
    indices.append(indice)
    tfs.append(open('tf/' + str(i+1) + '.txt', 'r', encoding='utf8').readlines())

webbrowser.open('http://localhost:5000')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET'])
def search():
    consulta = request.args['search']
    docsR = []
    if consulta:
        consulta = (' ').join(OperacoesTexto.limpar(consulta))

        if request.args['metodo'] == "Booleano":
            booleanoRI = BooleanoRI(consulta, tfs)
            docsRI = booleanoRI.executar(request.args['tipo'])
            for d in docsRI:
                docsR.append(indices[d])

        elif request.args['metodo'] == "Vetorial":
            vetorialRI = VetorialRI(consulta, tfs)
            sim = vetorialRI.executar()
            r = []
            for i in range(len(sim)):
                r.append((sim[i], indices[i]))
            r = sorted(r, key=itemgetter(0), reverse=True)
            for i in range(len(r)):
                if r[i][0]!=0: docsR.append(r[i][1])

        return render_template('view_result.html', docs=docsR, n=len(docsR))
    return render_template('index.html')

@app.route('/doc/<filename>')
def open_doc(filename):
    doc = indices[int(filename.split(".txt")[0])-1]
    return render_template('view_doc.html', doc=doc)

if __name__ == "__main__":
    app.run ()
