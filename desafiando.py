#! /usr/bin/python2

import sys
import extraer_palabra
import lemario
import operator


def help():
    print "%s <input-1> <input-2> ... <input-n>" % (sys.argv[0])

def procesarArchivo(path):
    cantidadDeCaracteres = extraer_palabra.obtenerCantidadDeCaracteres(file)
    data = extraer_palabra.obtenerPalabras(file)
    validas = 0
    lem = lemario.Lemario()
    caracteresValidos = 0
    caracteres = 0
    for palabra in data:
        if len(palabra) < 2:
            continue
        #print "palabra %s" % palabra
        palabraLen = len(palabra)
        caracteres += palabraLen
        if lem.check_word(palabra):
            caracteresValidos += palabraLen

    return score(caracteresValidos, cantidadDeCaracteres)

def score(caracteresValidos, cantidadDeCaracteres):
    return float(caracteresValidos) / cantidadDeCaracteres


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Argumentos invalidos"
        exit(1)

    if ["-help", "--help", "-h", "--h"].count(sys.argv[1].lower()) > 0:
        help()
        exit(0)

    scores = {}
    for file in sys.argv[1:]:
        scores.update({file: procesarArchivo(file)})


    sorted_x = sorted(scores.iteritems(), key=operator.itemgetter(1))
    print sorted_x
