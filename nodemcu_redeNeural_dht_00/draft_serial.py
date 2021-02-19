#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:29:30 2019

@author: pedrocnf
"""

import serial
import time


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
             umidade = ''.join(dados[0:5])
             temperatura = ''.join(dados[5:10])
         print umidade
         print temperatura
     except:
         print "falha ao receber"
         conexao.close()
         break
         
         
 
        
    