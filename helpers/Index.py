# -*- coding: utf-8 -*-
from operator import itemgetter
from helpers.OperacoesTexto import *
"""
    Indexação
    1. Separação de palavras:
        Extrair do início do documento o título, autor.
        Varrer todo texto e sempre quando encontrar um espaço ou um símbolo especial considera uma palavra encerrada; (Obs. O hífen ‘-‘ é considerado uma letra)
        Cada palavra encontrada é normalizada para todas letras minúsculas (mantendo-se a acentuação);
        É criada uma lista de todas palavras encontradas, mantendo-se a ordem original;
    A lista resultante é ordenada em ordem alfabética, ou outra técnica. É criado um arquivo com registros de dois campos, o primeiro contém o termo e o segundo o número de ocorrências.

    2. Eliminação de stop-words: A lista obtida no passo anterior é confrontada com uma lista de stop words eliminando-se todas stop-words da lista.

    3. Cria a lista (TF) final de pares <termo, frequência> das palavras.

    4. Passa a lista TF e o registro dos dados do novo documento para o módulo de armazenamento.
"""

class Index(object):

    TF_DIRETORIO        = "tf/"

    def __init__(self, arquivo):
        self.texto      = ""
        self.palavras   = []
        self.tf         = {}
        self.arquivo    = arquivo


        if arquivo:
            self.texto  = open('docs/'+arquivo, 'r', encoding="utf8").readlines()
            self.titulo = self.texto[0].upper()
            self.autor  = self.texto[1]
            #Remover Titulo e Autor
            self.texto.pop(0)
            self.texto.pop(0)
        pass

    def limparTexto(self):
        self.texto = "".join(self.texto)
        self.palavras = OperacoesTexto.limpar(self.texto)

    def criarListaTF(self):
        # Criar tf<Termo,Frequencia>
        for p in self.palavras:
            if p in self.tf:
                self.tf[p] += 1
            else:
                self.tf[p] = 1
        # Ordenar por frequencias mais altas
        self.tf = sorted(self.tf.items(), key=itemgetter(1))
        self.tf.sort(key=itemgetter(1), reverse=True)

    def gerarRegistro(self):
        # Criar Arquivo tf<Termo,Frequencia>
        arquivo_tf = open(self.TF_DIRETORIO+self.arquivo, 'w', encoding="utf8")
        for i in self.tf:
            arquivo_tf.write(str(i[0]) + ":" + str(i[1])+"\n")
        arquivo_tf.close()

    def indexar(self):
        self.limparTexto()
        self.criarListaTF()
        self.gerarRegistro()
