#! /usr/bin/python2

import sys
import extraer_palabra
import lemario
import operator


def help():
    print "%s <input-1> <input-2> ... <input-n>" % (sys.argv[0])

class ProcesadorDeTxt:
    def __init__(self, path, lemario=lemario.Lemario()):
        self.path = path;
        self.cantidadDecaracteres = 0
        self.validas = 0
        self.lemario = lemario
        self.caracteres = 0
        self.cantidad = extraer_palabra.ExtraerPalabras(path)
        self.caracteresValidos = 0

    def procesar(self):
        self.cantidadDeCaracteres = self.cantidad.obtenerCantidadDeCaracteres()
        data = self.cantidad.obtenerPalabras()

        for palabra in data:
            if len(palabra) < 2:
                continue

            palabraLen = len(palabra)
            self.caracteres += palabraLen
            if self.lemario.check_word(palabra):
                self.caracteresValidos += palabraLen


    def score(self):
        return float(self.caracteresValidos) / self.cantidadDeCaracteres

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

    scores = {}
    for file in sys.argv[1:]:
        #scores.update({file: procesarArchivo(file)})
        score = ProcesadorDeTxt(file)
        score.procesar()
        scores.update({file: score.score()})


    sorted_x = sorted(scores.iteritems(), key=operator.itemgetter(1))
    sorted_x.reverse()

    for x in sorted_x:
        print x[0], x[1]
