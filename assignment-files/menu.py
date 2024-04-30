# Dit is de menu module, het startpunt van de applicatie.

import inspecteurs
import metingen

# Start de applicatie
if __name__ == "__main__":
    while True:
        print('Hoofdmenu')
        print('=========')
        print('1. Inlezen inspecteursbestand')
        print('2. Inlezen en tonen CO2 data')
        print('3. Overzicht inspecteurs')
        print('4. <invullen>')
        print('5. <invullen>')
        print('6. <invullen>')
        print('7. <invullen>')
        print('0. stoppen\n')

        try:
            keuze = int(input('Uw keuze : '))
        except ValueError:
            keuze = -1

        if keuze == 1:
            inspecteurs.lees_inspecteurs()
        elif keuze == 2:
            metingen.lees_gas_co2()
        elif keuze == 3:
            inspecteurs.toon_inspecteurs()
        elif keuze == 0:
            exit()
        else :
            print('ongeldige keuze')
        
        # Een newline
        print()
