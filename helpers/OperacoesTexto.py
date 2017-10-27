# -*- coding: utf-8 -*-
from unicodedata import normalize

STOPWORDS_DIRETORIO = "helpers/stopwords.txt"
simbolos   = "\"\'\\/|’‘’“”•$&@%!?#§*(){}[]<>_–+±=ªº~^`´¨£¢¬,.¡¿:;1234567890"
stopwords  = open(STOPWORDS_DIRETORIO, 'r', encoding="utf8").readline().lower().split(' ')

class OperacoesTexto(object):

    def limpar(texto):
        # Remover simbolos e separar palavras
        for s in simbolos:
            texto = texto.replace(s, ' ')
        texto = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
        palavras = texto.lower().split()
        # Remover StopWords
        temp = []
        for p in palavras:
            if p not in stopwords:
                temp.append(p)
        return temp
