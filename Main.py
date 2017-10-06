# -*- coding: utf-8 -*-
from helpers.Index import *
docs = []
for i in range(10):
    index = Index(str(i+1)+".txt")
    index.indexar()
    #print("TITULO: " + index.titulo)
    #print("AUTOR: " + index.autor)
    d = []
    d.append(index.titulo)
    d.append(index.autor)
    d.append("...")
    docs.append(d)

'''
Buscador Web - Flask
    -Instalação: pip3 install flask
    -Documentação- http://flask.pocoo.org/docs/0.12/
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', docs=docs)

if __name__ == "__main__":
    app.run()
