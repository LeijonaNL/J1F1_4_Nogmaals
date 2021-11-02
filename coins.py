# name of student: Lennert
# number of student:99069054
# purpose of program: Het berekenen van wisselgeld
# function of program:if en while?
# structure of program: ???

toPay = int(float(input('Amount to pay: '))* 100) # Een input voor hoeveel je moet betalen.
paid = int(float(input('Paid amount: ')) * 100) # Een input voor hoeveel er is betaald.
change = paid - toPay # Betaald - betalen = wisselbedrag.

if change > 0: # Herkent of al het wisselgeld is gegeven en of er nog wisselgeld gegeven moet worden.
  coinValue = 50 # De waarde van een munt.
  
  while change > 0 and coinValue > 0: # Een while die blijft werken tot er geen change of value meer over is.
    nrCoins = change // coinValue # Dit weet ik niet te beschrijven.

    if nrCoins > 0: # Als er wisselgeld gegeven moet worden zal het onderstaande in werking gaan.
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Hier wordt aangegeven hoeveel munten je van een muntsoort kunt geven.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Hierin moet je invullen hoeveel van de hierboven aangegeven munten je hebt gegeven als wisselgeld.
      change -= nrCoinsReturned * coinValue # Een formule voor hoeveel wisselgeld je hebt gegeven bij de bovenstaande vraag.

# comment on code below: Door deze code zul de vraag voor meerdere muntsoorten de vragen stellen.
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # Als je niet genoeg hebt teruggegeven wordt dat aangegeven, als je genoeg hebt teruggegeven zegt het dat je klaar bent.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')