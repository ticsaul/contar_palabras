#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:44:30 2017

@author: saul

Función para contar las palabras dentro de un texto.

Pasar como parametro el vector que almacena el texto
Nota: El texto no debe tener letras con acento.

"""
def contarPalabras(vector):
    l = 0 # longitud del vector
    j = 0 # apuntador
    nPal = 0 # numero de palabras
    iniCad = False # cuando inicia una palabra
    finCad = False # cuando termina la palabra
    tamVec = len(vector)
    
    while(l < len(vector)):
            # recorrer el vector de letras
        for i in range(j, tamVec):
            # letras mayusculas
            if ord(vector[i]) >= 65 and ord(vector[i]) <= 90:
                iniCad = True
            # letras minusculas
            elif ord(vector[i]) >= 97 and ord(vector[i]) <= 122:
                iniCad = True
            else:
                if iniCad == True:
                    finCad = True
            
            # se evalua si es la ultima palabra
            if l == tamVec:
                if iniCad == True:
                    finCad = True
            
            l = l + 1 # incrementar
            
            # si se encontro una palabra
            if iniCad == True and finCad == True:
                nPal = nPal + 1 # se contabiliza la palabra
                # resetear variables de apoyo
                iniCad = False
                finCad = False
                j = i
                break # salir del for
    
    return nPal
