# -*- coding: utf-8 -*-
'''
Created on 26 ene 2022

@author: willi
'''
from collections import namedtuple
import csv
import statistics
from collections import Counter
from parsers import *

Jugador = namedtuple('Jugador', 'nombre,ranking,puntuacion,compañero,posicion,lugar_nacimiento,fecha_nacimiento,altura,partidos_jugados,partidos_ganados,partidos_perdidos,racha,circuito')

def lee_fichero(fichero):
    with open(fichero, encoding= 'utf-8') as f:
        lector= csv.reader(f, delimiter= ";")
        next(lector)
        res=[]
        for nombre,ranking,puntuacion,compañero,posicion,lugar_nacimiento,fecha_nacimiento,altura,partidos_jugados,partidos_ganados,partidos_perdidos,racha,circuito in lector:
            tupla_juegos = Jugador(nombre,int(ranking),int(puntuacion),compañero,posicion,lugar_nacimiento,parsea_fecha(fecha_nacimiento),float(altura),int(partidos_jugados),int(partidos_ganados),int(partidos_perdidos),int(racha),circuito)
            res.append(tupla_juegos)
    return res

def top_fecha_nacimiento(registros,posicion,fecha,n):
    res = [(t.nombre,t.ranking)for t in registros if t.ranking>posicion and t.fecha_nacimiento > fecha]
    lista_ordenada = sorted(res, key = lambda x:x[1])
    if len(lista_ordenada)>n:
        lista_ordenada = lista_ordenada[:n]
    return res
    
def ratio_ganados_perdidos_circuito(registros,circuito=None):
    res =[(t.nombre, t.partidos_ganados/t.partidos_perdidos) for t in registros if (t.circuito == circuito or t.circuito == None) and t.partidos_perdidos != 0]
    maximo = max(res, key=lambda x:x[1])
    return maximo
def agrupa_n_jugadores_mejores_por_posicion(registros,altura,n=5):
    dicc = agrupa_por_posicion_altura(registros, altura)
    res={}
    for clave, valor in dicc.items():
        lista = sorted(valor, key=lambda x:x.partidos_ganados-x.partidos_perdidos,reverse=True)
    if len(lista)>n:
        lista=lista[:n]
    res[clave]=[t.nombre for t in lista]
    return res
    
def agrupa_por_posicion_altura(registros,altura):
    dicc={}
    for t in registros:
        if t.altura>altura:
            clave=t.posicion
            if clave in dicc:
                dicc[clave].append(t)
            else:
                dicc[clave] = [t]
    return dicc

def parejas_top_racha(registros,n):
    d_parejas = diccionario_parejas(registros)
    lista = sorted(d_parejas.items(), key= lambda x:x[1],reverse = True)
    if len(lista)>n:
        lista =lista[:n]
    return [t[0] for t in lista]

def get_dict_rachas(registros):
    dicc = {}
    for t in registros:
        clave=t.nombre
        if clave not in dicc:
            dicc[clave]=t.racha
    return dicc
def diccionario_parejas(registros):
    res ={}
    dict_rachas = get_dict_rachas(registros)
    for t in registros:
        if(t.nombre,t.compañero) not in res and (t.compañero,t.nombre) not in res:
            racha_1 = dict_rachas.get(t.nombre)
            racha_2 = dict_rachas.get(t.nombre, 0)
            res [(t.nombre,t.compañero)] = racha_1 + racha_2

    