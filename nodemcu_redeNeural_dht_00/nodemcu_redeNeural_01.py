#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:29:30 2019

@author: pedrocnf
"""

import serial
import time
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

dataset = SupervisedDataSet(2,1)

dataset.addSample([0.5,0.32],[0])
dataset.addSample([0.6,0.33],[1])
dataset.addSample([0.8,0.30],[2])
dataset.addSample([0.8,0.34],[3])

network = buildNetwork(dataset.indim, 4, dataset.outdim, bias=True)

trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.99)

for epoch in range(0, 1000): 
    print trainer.train()
resultado = []
porta_serial = "com3" 

conexao = serial.Serial(porta_serial, 9600, timeout = 30) 

dados = range(12) 

while True :
     i = 0
     try:
         time.sleep(1)
         if conexao.inWaiting():
             valor = conexao.readline() 
         #temperatura = ''.join(dados[0:5])
         #umidade = ''.join(dados[0:5])
         #print umidade
         for letra in valor:
             dados[i] = letra
             i = i + 1
         print dados
         if dados[0] != 'e':
             umidade = float(''.join(dados[0:5]))
             temperatura = float(''.join(dados[5:10]))
         print 'umidade:',umidade
         print 'temperatura',temperatura
         resultado.append(network.activate([umidade/10.0,temperatura/10.0]))
         
     except:
         print "falha ao receber"
         conexao.close()
         break
         
         
 
        
    