#! /usr/bin/python2

import sys
import extraer_palabra
import lemario
import operator


def help():
    print "%s <input-1> <input-2> ... <input-n>" % (sys.argv[0])

def computarScore(lem, path):
    archivo = extraer_palabra.ExtraerPalabras(path)

    cantidadDeCaracteres = archivo.obtenerCantidadDeCaracteres()
    palabrasParseadas = archivo.obtenerPalabras()

    cantidadDeCaracteresValidos = 0
    cantidadDePalabrasBuenas = 0
    cantidadDePalabrasMalas = 0
    for palabra in palabrasParseadas:
        if lem.check_word(palabra):
            cantidadDeCaracteresValidos += len(palabra)
            cantidadDePalabrasBuenas = cantidadDePalabrasBuenas + 1
        else:
            cantidadDePalabrasMalas = cantidadDePalabrasMalas + 1

    cantidadDeCaracteresInvalidos = cantidadDeCaracteres - cantidadDeCaracteresValidos
    cantidadDePalabrasInvalidas = cantidadDeCaracteresValidos / 12

    score = float(cantidadDePalabrasBuenas) / (cantidadDePalabrasMalas + cantidadDePalabrasInvalidas)

    return score

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Argumentos invalidos"
        exit(1)

    if ["-help", "--help", "-h", "--h"].count(sys.argv[1].lower()) > 0:
        help()
        exit(0)

    lem = lemario.Lemario()

    scores = {}
    for file in sys.argv[1:]:
        scores.update({file: computarScore(lem, file)})

    scores_ordenados = sorted(scores.iteritems(), key=operator.itemgetter(1))
    scores_ordenados.reverse()

    for x in scores_ordenados:
        print x[0], x[1]
