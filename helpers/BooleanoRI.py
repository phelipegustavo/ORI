# -*- coding: utf-8 -*-
"""
    Modelo Booleano de Recuperacção da Informação
"""

class BooleanoRI(object):
    def __init__(self, consulta, tfs):
        self.q      = consulta.split(' ');
        self.tfs    = tfs
        self.termos = []
        for tf in self.tfs:
            termos = []
            for t in tf:
                termos.append(t.split(':')[0])
            self.termos.append(termos)
        pass

    def AND(self, tf):
        for q in self.q:
            if q not in tf:
                return False
        return True

    def OR(self, tf):
        for q in self.q:
            if q in tf:
                return True
        return False

    def executar(self, tipo):
        docs = []
        for tf in self.termos:
            if tipo == 'AND':
                r = self.AND(tf)
            elif tipo == 'OR':
                r = self.OR(tf)
            if r:
                docs.append(self.termos.index(tf))
        return docs
