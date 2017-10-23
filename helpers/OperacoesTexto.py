# -*- coding: utf-8 -*-
from unicodedata import normalize

class OperacoesTexto(object):

    STOPWORDS_DIRETORIO = "helpers/stopwords.txt"

    def __init__(self, texto):
        self.simbolos   = "\"\'\\/|’‘’“”•$&@%!?#§*(){}[]<>_–+±=ªº~^`´¨£¢¬,.¡¿:;1234567890"
        self.stopwords  = open(self.STOPWORDS_DIRETORIO, 'r', encoding="utf8").readline().lower().split(' ')
        self.texto      = texto
        self.palavras   = []


    def limpar(self):
        # Remover simbolos e separar palavras
        for s in self.simbolos:
            self.texto = self.texto.replace(s, ' ')
        self.texto = normalize('NFKD', self.texto).encode('ASCII', 'ignore').decode('ASCII')
        self.palavras = self.texto.lower().split()
        # Remover StopWords
        temp = []
        for p in self.palavras:
            if p not in self.stopwords:
                temp.append(p)
        return temp
