# Duizelig4

repeat = True
while repeat:
    repeat = False
    dag = input('Welke dag van de week? ').lower()
    if dag == 'maandag':
        dagen = 'Ma.'
    elif dag == 'dinsdag':
        dagen = 'Ma. Di.'
    elif dag == 'woensdag':
        dagen = 'Ma. Di. Wo.'
    elif dag == 'donderdag':
        dagen = 'Ma. Di. Wo. Do.'
    elif dag == 'vrijdag':
        dagen = 'Ma. Di. Wo. Do. Vr.'
    elif dag == 'zaterdag':
        dagen = 'Ma. Di. Wo. Do. Vr. Za.'
    elif dag == 'zondag':
        dagen = 'Ma. Di. Wo. Do. Vr. Za. Zo.'
    else:
        print('Dat is geen mogelijk antwoord.')
        repeat = True

print(dagen)