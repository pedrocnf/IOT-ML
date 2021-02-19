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

dados = range(13) 

while True :
     
    i = 0
    #quantidade_leituras = quantidade_leituras + 1
   # computarEnergia(carga_baterias_nodos,quantidade_leituras,taxa_amostral,leituras_temporario)
    #try:
        #carga_baterias_nodos[0,:] = carga_baterias_nodos[0,:] - (0,0464 * taxa_amostral[0,:])/2
    #except:
        #print "Nao foi possivel calcular carga da bateria"
    try:
        time.sleep(1)
       
        if conexao.inWaiting():
        
         valor = conexao.readline() 
         print valor
         for letra in valor:
            dados[i] = letra
            i = i + 1
    except:
        print "falha ao receber"
        conexao.close()
        break
 
        
    