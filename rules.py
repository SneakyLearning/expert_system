def rules(material1,material2,thickness):
    chamfer = 'butt'
    if material1 == 'al' or material2 == 'al':
        meathod = 'tig'
    else:meathod = 'gaw'

    if meathod == 'tig':
        gas = 'ar'
        if thickness<=8:
            current = 250
            voltage = 25
        elif 8<thickness<=14:
            current = 300
            voltage = 30
        else:
            current=450
            voltage=30
    if meathod == 'gaw':
        gas = 'co2'
        if thickness<=4:
            current = 80
            voltage = 19
        elif 4<thickness<=8:
            current = 140
            voltage = 22
        elif 8<thickness<=10:
            current = 200
            voltage = 24
        else:
            current=240
            voltage=25

    return meathod,chamfer,current,voltage,gas
