# Raad eens

poging = 0
punten = 0

repeat = True
print('Als je wilt stoppen, type dan "quit".')
for i in range(20):
    import random
    nummer = random.randint(0,1000)
    while repeat:
        poging += 1
        invoer = input('Raad het getal, dit is je ' + str(poging) + 'e poging. ').lower()
        if invoer == 'quit':
            repeat = False
            break
        gok = int(invoer)
        verschil = gok-nummer

        # Geraden
        if gok == nummer:
            punten += 1
            print('Je hebt het nummer geraden! Je hebt nu ' + str(punten) + ' punten.')
            break
        # Te hoog   
        elif verschil > 0:
            if verschil <= 20:
                print('Je bent heel warm, maar je moet lager.')
            elif verschil <= 50:
                print('Je bent warm, maar je moet lager.')
            else:
                print('Je moet lager.')
        # Te laag
        elif verschil < 0:
            if verschil >= -20:
                print('Je bent heel warm, maar je moet hoger.')
            elif verschil >= -50:
                print('Je bent warm, maar je moet hoger.')
            else:
                print('Je moet hoger.')

        # Pogingen op
        if poging == 10:
            print('Je hebt hebt het maximaal aantal pogingen gehaald voor dit getal.' +
            '\nHet getal was ' + str(nummer) +
            '.\nEr wordt nu een nieuw nummer gegenereerd, als je niet meer wilt spelen, type dan "quit"')
            break
else:
    print('Gestopt')