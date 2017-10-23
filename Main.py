# -*- coding: utf-8 -*-
from helpers.Index import *
from helpers.BooleanoRI import *
from helpers.OperacoesTexto import *
from helpers.VetorialRI import *
from flask import Flask, render_template, request

app     = Flask(__name__)
QNT     = 10    # Quantidade de Documentos
indices = []    # List de objetos Indices
tfs     = []    # List de Arquivos Termo Frequencia

for i in range(QNT):
    arquivo = str(i+1)+".txt"
    indice = Index(arquivo)
    indice.indexar()
    indices.append(indice)
    tfs.append(open('tf/' + str(i+1) + '.txt', 'r', encoding='utf8').readlines())

vetorial = VetorialRI('muscular joelho', tfs)
vetorial.calcularIDF()
print(vetorial.idf)
vetorial.calcularTF()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET'])
def search():
    if request.method == 'GET':
        consulta = request.args['search']
        docsR = []
        if consulta:
            ot = OperacoesTexto(consulta)
            consulta = (' ').join(ot.limpar())
            booleanoRI = BooleanoRI(consulta, tfs)
            docsRI = booleanoRI.executar(request.args['tipo'])
            for d in docsRI:
                docsR.append(indices[d])
            return render_template('view_result.html', docs=docsR, consulta=consulta)
        return render_template('index.html')

@app.route('/doc/<filename>')
def open_doc(filename):
    doc = indices[int(filename.split(".txt")[0])-1]
    return render_template('view_doc.html', doc=doc)

if __name__ == "__main__":
    app.run ()
