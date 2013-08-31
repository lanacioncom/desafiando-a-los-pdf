#! /usr/bin/python2

import sys
import extraer_palabra
import lemario
import operator


def help():
    print "%s <input-1> <input-2> ... <input-n>" % (sys.argv[0])

class ProcesadorDeTxt:
    def __init__(self, path, lemario=lemario.Lemario()):
        self.lemario = lemario
        self.archivo = extraer_palabra.ExtraerPalabras(path)
        self.cantidadDeCaracteres = self.archivo.obtenerCantidadDeCaracteres()
        self.palabrasParseadas = self.archivo.obtenerPalabras()
        self.cantidadDeCaracteresValidos = 0
        self.cantidadDePalabrasBuenas = 0
        self.cantidadDePalabrasMalas = 0
        self.cantidadDeCaracteresInvalidos = 0
        self.cantidadDePalabrasInvalidas = 0

    def procesar(self):
        self.cantidadDeCaracteresValidos = 0
        self.cantidadDePalabrasBuenas = 0
        self.cantidadDePalabrasMalas = 0
        for palabra in self.palabrasParseadas:
            if self.lemario.check_word(palabra):
                self.cantidadDeCaracteresValidos += len(palabra)
                self.cantidadDePalabrasBuenas = self.cantidadDePalabrasBuenas + 1
            else:
                self.cantidadDePalabrasMalas = self.cantidadDePalabrasMalas + 1

        self.cantidadDeCaracteresInvalidos = self.cantidadDeCaracteres - self.cantidadDeCaracteresValidos
        self.cantidadDePalabrasInvalidas = self.cantidadDeCaracteresValidos / 12

    def score(self):
        score = 10 * float(self.cantidadDePalabrasBuenas) / (self.cantidadDePalabrasMalas + self.cantidadDePalabrasInvalidas)
        return score


#def procesarArchivo(path):
#    cantidad = extraer_palabra.ExtraerPalabras(path)
#    #cantidadDeCaracteres = extraer_palabra.obtenerCantidadDeCaracteres(file)
#    cantidadDeCaracteres = cantidad.obtenerCantidadDeCaracteres()
#    #data = extraer_palabra.obtenerPalabras(file)
#    data = cantidad.obtenerPalabras()
#    validas = 0
#    lem = lemario.Lemario()
#    caracteresValidos = 0
#    caracteres = 0
#    for palabra in data:
#        if len(palabra) < 2:
#            continue
#        #print "palabra %s" % palabra
#        palabraLen = len(palabra)
#        caracteres += palabraLen
#        if lem.check_word(palabra):
#            caracteresValidos += palabraLen
#
#    return score(caracteresValidos, cantidadDeCaracteres)
#
#def score(caracteresValidos, cantidadDeCaracteres):
#    return float(caracteresValidos) / cantidadDeCaracteres

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
        score = ProcesadorDeTxt(file)
        score.procesar()
        scores.update({file: score.score()})

    scores_ordenados = sorted(scores.iteritems(), key=operator.itemgetter(1))
    scores_ordenados.reverse()

    for x in scores_ordenados:
        print x[0], x[1]
