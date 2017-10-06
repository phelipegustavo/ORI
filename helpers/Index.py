# -*- coding: utf-8 -*-
from operator import itemgetter

"""
Etapa 1: Indexação
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

    STOPWORDS_DIRETORIO = "helpers/stopwords.txt"
    TF_DIRETORIO        = "tf/"

    def __init__(self, arquivo):
        self.simbolos   = "\"\'\\/|’‘’“”•$&@%!?#§*(){}[]<>_–+±=ªº~^`´¨£¢¬,.¡¿:;1234567890"
        self.texto      = ""
        self.palavras   = []
        self.indice     = {}
        self.arquivo    = arquivo

        self.stopwords  = open(self.STOPWORDS_DIRETORIO, 'r', encoding="utf8").readline().lower().split(' ')

        if arquivo:
            self.texto  = open('docs/'+arquivo, 'r', encoding="utf8").readlines()
            self.titulo = self.texto[0]
            self.autor  = self.texto[1]
        pass

    def limparTexto(self):
        #Remover Titulo e Autor
        self.texto.pop(0)
        self.texto.pop(0)
        self.texto = "".join(self.texto)
        # Remover simbolos e separar palavras
        for s in self.simbolos:
            self.texto = self.texto.replace(s, ' ')
        self.palavras = self.texto.lower().split()
        # Remover StopWords
        temp = []
        for p in self.palavras:
            if p not in self.stopwords:
                temp.append(p)
        self.palavras = temp

    def criarListaTF(self):
        # Criar indice<Termo,Frequencia>
        for p in self.palavras:
            if p in self.indice:
                self.indice[p] += 1
            else:
                self.indice[p] = 1
        # Ordenar por frequencias mais altas
        self.indice = sorted(self.indice.items(), key=itemgetter(1))
        self.indice.sort(key=itemgetter(1), reverse=True)

    def gerarRegistro(self):
        # Criar Arquivo Indice<Termo,Frequencia>
        arquivo_indice = open(self.TF_DIRETORIO+self.arquivo, 'w', encoding="utf8")
        for i in self.indice:
            arquivo_indice.write(str(i[0]) + ":" + str(i[1])+"\n")
        arquivo_indice.close()

    def indexar(self):
        self.limparTexto()
        self.criarListaTF()
        self.gerarRegistro()
