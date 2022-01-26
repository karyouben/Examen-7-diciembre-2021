# -*- coding: utf-8 -*-
'''
Created on 26 ene 2022

@author: willi
'''
from jugadores import *

def test_lee_fichero(fichero):
    print("="*20+"test_lee_fichero"+"="*20)
    print("")
    res = lee_fichero(fichero)
    print(f"Los tres primeros registros son: {res[:3]}")
    print("")
    print(f"Los tres primeros registros son: {res[-3:]}")
    print("")
    


def main():
    fichero =('../date/World.Padel.Tour.csv')
    test_lee_fichero(fichero)
if __name__=="__main__":
    main()