# Duizelig5


i = 1
repeat = True
while repeat:
    repeat = False
    answer = input('Type iets. ').lower()
    if answer == 'quit':
        print('Goed geantwoord! Dit was Uw ' + str(i) + 'e input.')
    else:
        print('Dat is geen goed antwoord. Dit was Uw ' + str(i) + 'e input.')
        i = i + 1
        repeat = True