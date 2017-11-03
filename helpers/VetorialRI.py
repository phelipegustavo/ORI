# -*- coding: utf-8 -*-
from math import log, pow, sqrt
"""
    Modelo de Espaço Vetorial de Recuperacção da Informação
"""

class VetorialRI(object):
    def __init__(self, consulta, tfs):
        self.consulta   = consulta.split();
        self.Ds         = []
        self.Q          = []
        self.IDF        = []
        self.TFDs       = []
        self.WDs        = []
        self.TFQ        = []
        self.WQ         = []
        self.SIM        = []

        keys = []
        for c in self.consulta:
            if c not in keys:
                keys.append(c)
                self.Q.append(consulta.count(c))
        for tf in tfs:
            D = []
            for k in keys:
                find = False
                for t in tf:
                    termo,freq = t.split(':')
                    if termo == k:
                        find = True
                        D.append(int(freq))
                if not find: D.append(0)
            self.Ds.append(D)
        pass

    def calcularIDF(self):
        N = len(self.Ds)
        for c in range(len(self.Q)):
            n = 0
            for d in range(len(self.Ds)):
                if self.Ds[d][c]: n+=1
            if n: self.IDF.append(1+log(N/n,2))
            else: self.IDF.append(0)

    def calcularTF(self):
        maxD = [0] * len(self.Ds)
        print(self.Q)
        maxQ = sorted(self.Q, reverse=True)[0]
        for d in range(len(self.Ds)):
            maxD[d] = sorted(self.Ds[d], reverse=True)[0]
        for d in range(len(self.Ds)):
            TFD = []
            for c in range(len(self.Q)):
                if maxD[d]: TFD.append(self.Ds[d][c]/maxD[d])
                else: TFD.append(0)
            self.TFDs.append(TFD)
        for c in range(len(self.Q)):
            self.TFQ.append(self.Q[c]/maxQ)

    def calcularW(self):
        for t in range(len(self.TFDs)):
            WD = []
            for c in range(len(self.Q)):
                WD.append(self.TFDs[t][c]*self.IDF[c])
            self.WDs.append(WD)

        for c in range(len(self.Q)):
            self.WQ.append((self.Q[c])*self.IDF[c])

    def calcularSIM(self):
        for w in range(len(self.WDs)):
            nsum  = 0
            dsumW = 0
            dsumQ = 0
            for c in range(len(self.Q)):
                nsum  += self.WDs[w][c]*self.WQ[c]
                dsumW += pow(self.WDs[w][c],2)
                dsumQ += pow(self.WQ[c],2)
            dnum = sqrt(dsumW)*sqrt(dsumQ)
            if dnum == 0: self.SIM.append(0)
            else: self.SIM.append(nsum/dnum)

    def executar(self):
        if(self.Q):
            self.calcularIDF()
            self.calcularTF()
            self.calcularW()
            self.calcularSIM()
        return self.SIM
