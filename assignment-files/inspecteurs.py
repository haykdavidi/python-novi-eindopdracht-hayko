"""Inspecteurs module"""

# constanten
INSPECTEURSBESTAND = 'inspecteurs.txt'

lijst_inspecteurs = []   # lijst met alle inspecteur objecten

def lees_inspecteurs():
    """Inlezen van het tekstbestand met de inspecteursgegevens"""
    try:
        with open(INSPECTEURSBESTAND, mode='r') as inspecteurs:
            for record in inspecteurs :
                code = record[0:3]
                naam = record[4:24]
                standplaats = record[24:44]
                lijst_inspecteurs.append(Inspecteur(code, naam, standplaats))
        print('Bestand', INSPECTEURSBESTAND, 'ingelezen')
        return 0
    except FileNotFoundError:
        print('Bestand', INSPECTEURSBESTAND, 'niet gevonden')
        return 1


def toon_inspecteurs():
    """Maak een overzicht van alle inspecteursgegevens"""
    print("        Overzicht inspecteurs")
    print("        =====================\n")
    print("Code Naam                 Standplaats")
    print("---- -------------------- --------------------")
       
    for inspecteur in lijst_inspecteurs:
        inspecteur.toon()


class Inspecteur:
    """Deze class representeert een Inspecteur"""
    def __init__(self, code, naam='', standplaats=''):
        self.__code = code
        self.__naam = naam
        self.__standplaats = standplaats
        self.__bezoekrapporten = []

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_naam(self):
        return self.__naam

    def set_naam(self, naam):
        self.__naam = naam

    def get_standplaats(self):
        return self.__standplaats

    def set_standplaats(self, standplaats):
        self.__standplaats = standplaats

    def add_bezoekrapport(self, bezoekrapport):
        self.__bezoekrapporten.append(bezoekrapport)

    def toon(self):
        print(self.__code + ' ', self.__naam, self.__standplaats)
