#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dice import roll, DiceException

class personaje:
    fuerza = 0
    inteligencia = 0
    sabiduria = 0
    destreza = 0
    constitucion = 0
    carisma = 0
    valid_classes = []
    mod_px_neg_20 = []
    mod_px_neg_10 = []
    mod_px_0 = []
    mod_px_5 = []
    mod_px_10 = []


    def __init__(self):
        self.fuerza = roll("3d6t")
        self.inteligencia = roll("3d6t")
        self.sabiduria = roll("3d6t")
        self.destreza = roll("3d6t")
        self.constitucion  = roll("3d6t")
        self.carisma = roll("3d6t")
        self.check_classes()

    def __str__(self):
        stringtoprint = "fuerza: " + str(self.fuerza) + "\n"
        stringtoprint = stringtoprint + "inteligencia: " + str(self.inteligencia) + "\n"
        stringtoprint = stringtoprint + "sabiduria: " + str(self.sabiduria) + "\n"
        stringtoprint = stringtoprint + "destreza: " + str(self.destreza) + "\n"
        stringtoprint = stringtoprint + "constitucion: " + str(self.constitucion) + "\n"
        stringtoprint = stringtoprint + "carisma: " + str(self.carisma) + "\n"
        stringtoprint = stringtoprint + "clases validas: " + str(self.valid_classes) + "\n"

        if self.mod_px_neg_20:
            stringtoprint = stringtoprint + "-20% px: " + str(self.mod_px_neg_20) + "\n"
        if self.mod_px_neg_10:
            stringtoprint = stringtoprint + "-10% px: " + str(self.mod_px_neg_10) + "\n"
        if self.mod_px_0:
            stringtoprint = stringtoprint + "+0% px: " + str(self.mod_px_0) + "\n"
        if self.mod_px_5:
            stringtoprint = stringtoprint + "5% px: " + str(self.mod_px_5) + "\n"
        if self.mod_px_10:
            stringtoprint = stringtoprint + "+10% px: " + str(self.mod_px_10) + "\n"

        return stringtoprint


    def check_classes(self):
        self.clerigo()
        self.elfo()
        self.enano()
        self.guerrero()
        self.ladron()
        self.mago()
        self.mediano()
        self.Acrobata()
        self.Asesino()
        self.Barbaro()
        self.Bardo()
        self.Caballero()
        self.Drow()
        self.Druida()
        self.Duergar()
        self.Gnomo()
        self.Guardabosques()
        self.Ilusionista()
        self.Paladin()
        self.Semielfo()
        self.Semiorco()
        self.Svirfneblin()

    def px_mod(self, characteristic1, characteristic2, characterclass):

        if characteristic2 != None:
            self.mod_px_0.append(characterclass)
            return

        if characteristic1 >= 3 and characteristic1 <= 5:
            self.mod_px_neg_20.append(characterclass)
            return
        if characteristic1 >= 6 and characteristic1 <= 8:
            self.mod_px_neg_10.append(characterclass)
            return
        if characteristic1 >= 9 and characteristic1 <= 12:
            self.mod_px_0.append(characterclass)
            return
        if characteristic1 >= 13 and characteristic1 <= 15:
            self.mod_px_5.append(characterclass)
            return
        if characteristic1 >= 16 and characteristic1 <= 18:
            self.mod_px_10.append(characterclass)
            return

        return

    def clerigo(self):
        self.valid_classes.append("Clerigo")
        self.px_mod(self.sabiduria, None, "Clerigo")
        return

    def elfo(self):
        if self.inteligencia >= 9:
            self.valid_classes.append("Elfo")
        self.px_mod(self.inteligencia, self.fuerza, "Elfo")
        return

    def enano(self):
        if self.constitucion >= 9:
            self.valid_classes.append("Enano")
        self.px_mod(self.fuerza, None, "Enano")
        return

    def ladron(self):
        self.valid_classes.append("ladron")
        self.px_mod(self.destreza, None, "ladron")
        return

    def guerrero(self):
        self.valid_classes.append("Guerrero")
        self.px_mod(self.fuerza, None, "guerrero")
        return

    def mago(self):
        self.valid_classes.append("Mago")
        self.px_mod(self.inteligencia, None, "mago")
        return

    def mediano(self):
        if self.constitucion >= 9 and self.destreza >= 9:
            self.valid_classes.append("Mediano")
        self.px_mod(self.destreza, self.fuerza, "mago")
        return

    def Acrobata(self):
        self.valid_classes.append("Acrobata")
        self.px_mod(self.destreza, None, "Acrobata")
        return

    def Asesino(self):
        self.valid_classes.append("Asesino")
        self.px_mod(self.destreza, None, "Asesino")
        return

    def Barbaro(self):
        if self.destreza >= 9:
            self.valid_classes.append("Barbaro")
        if self.constitucion >= 16 and self.fuerza > 16:
            self.mod_px_10.append("Barbaro")
            return
        if self.constitucion >= 13 or self.fuerza >= 13:
            self.mod_px_5.append("Barbaro")
            return
        return

    def Bardo(self):
        if self.destreza >= 9 and self.inteligencia >= 9:
            self.valid_classes.append("Bardo")
        self.px_mod(self.carisma, None, "Bardo")
        return

    def Caballero(self):
        if self.constitucion >= 9 and self.destreza >= 9:
            self.valid_classes.append("Caballero")
        self.px_mod(self.fuerza, None, "Caballero")
        return


    def Drow(self):
        if self.inteligencia >= 9:
            self.valid_classes.append("Drow")
        if self.fuerza >= 16 and self.sabiduria > 16:
            self.px_10.append("Drow")
            return
        if self.fuerza >= 13 or self.sabiduria >= 13:
            self.mod_px_5.append("Drow")
            return
        return

    def Druida(self):
        self.valid_classes.append("Druida")
        self.px_mod(self.sabiduria, None, "Druida")
        return

    def Duergar(self):
        if self.constitucion >= 9 and self.inteligencia >= 9:
            self.valid_classes.append("Duergar")
        self.px_mod(self.fuerza, None, "Duergar")
        return

    def Gnomo(self):
        if self.constitucion >= 9:
            self.valid_classes.append("Gnomo")
        if self.destreza >= 13 and self.inteligencia > 16:
            self.mod_px_10.append("Gnomo")
            return
        if self.destreza >= 13 or self.inteligencia >= 13:
            self.mod_px_5.append("Gnomo")
            return

    def Guardabosques(self):
        if self.constitucion >= 9 and self.sabiduria >= 9:
            self.valid_classes.append("Guardabosques")
        self.px_mod(self.fuerza, None, "Guardabosques")
        return

    def Ilusionista(self):
        if self.destreza >= 9:
            self.valid_classes.append("Ilusionista")
        self.px_mod(self.inteligencia, None, "Ilusionista")
        return

    def Paladin(self):
        if self.carisma >= 9:
            self.valid_classes.append("Paladin")
        if self.fuerza >= 16 and self.sabiduria > 16:
            self.px_10.append("Paladin")
            return
        if self.fuerza >= 13 or self.sabiduria >= 13:
            self.mod_px_5.append("Paladin")
            return
        return

    def Semielfo(self):
        if self.carisma >= 9 and self.constitucion >= 9:
            self.valid_classes.append("Semielfo")
        if self.inteligencia >= 16 and self.fuerza > 16:
            self.px_10.append("Semielfo")
            return
        if self.inteligencia >= 13 or self.fuerza >= 13:
            self.mod_px_5.append("Semielfo")
            return
        return

    def Semiorco(self):
        self.valid_classes.append("Semiorco")
        if self.destreza >= 16 and self.fuerza > 16:
            self.px_10.append("Semiorco")
            return
        if self.destreza >= 13 or self.fuerza >= 13:
            self.mod_px_5.append("Semiorco")
            return
        return

    def Svirfneblin(self):
        if self.constitucion >= 9:
            self.valid_classes.append("Svirfneblin")
        self.px_mod(self.fuerza, None, "Svirfneblin")
        return

print(personaje())

