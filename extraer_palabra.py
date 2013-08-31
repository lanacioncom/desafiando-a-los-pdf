# -*- coding: utf-8 -*-

import sys
import re

def obtenerPalabras(file):
    with open(file,'r') as myfile:
        data=myfile.read().replace('\n', '')

    data = re.sub(r'\.',' ',data)
    data = re.sub(r'[^a-zA-Z\s]','',data)
    data = re.split('\s|\t|,', data)

    return data


def obtenerCantidadDeCaracteres(file):
    with open(file,'r') as myfile:
        data=myfile.read().replace('\n', '')

    return len(data)

if __name__ == "__main__":
    for file in sys.argv[1:]:
        cantidadDeCaracteres = obtenerCantidadDeCaracteres(file)
        data = obtenerPalabras(file)
        for palabra in data:
            if 1 < len(palabra) < 20 and palabra.lower() != palabra.upper():
                print(palabra.lower().strip())

        print "# caracteres total: ", cantidadDeCaracteres
        print "# palabras extraídas: ", len(data)
        print "Ratio entre # caracteres total y # palabras extraídas: ", "%f"%(cantidadDeCaracteres / len(data))
