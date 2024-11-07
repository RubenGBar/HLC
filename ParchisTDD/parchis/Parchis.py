from random import *

class Parchis:
    TAM_TABLERO = 10
    dado1 = 0
    dado2 = 0

    def __init__(self, nombreJ1, nombreJ2):
        self.fichaJ1 = 7
        self.fichaJ2 = 5
        self.nombreJ1 = nombreJ1
        self.nombreJ2 = nombreJ2

    @staticmethod
    def tiraDados():
        Parchis.dado1 = randint(1,6)
        Parchis.dado2 = randint(1,6)

    @staticmethod
    def pintaTablero(self):
        cad = ""
        i = 0
        j = 0
        k = 0

        while i <= Parchis.TAM_TABLERO:
            if i == 0:
                cad+=("\t" + "\tI")
            elif i == Parchis.TAM_TABLERO:
                cad+=("\t" + "F\n")
            else:
                cad+=("\t" + str(i))
            i += 1

        cad+=(self.nombreJ1 + "\tI")
        while j <= Parchis.TAM_TABLERO:
            if j == self.fichaJ1:
                cad+= "\tO"
            elif j == Parchis.TAM_TABLERO:
                cad+= "F\n"
            else:
                cad+= "\t"
            j += 1

        cad+=(self.nombreJ2 + "\tI")
        while k <= Parchis.TAM_TABLERO:
            if k == self.fichaJ2:
                cad+="\tO"
            elif k == Parchis.TAM_TABLERO:
                cad+="F\n"
            else:
               cad+= "\t"
            k += 1

        return cad