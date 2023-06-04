# Пользователь вводит обьем бака и расход по городу.
# Вывести сколько километров он проедет по трассе с учётом
#   - уменьшения расхода в теплую погоду на  30%
#   - уменьшения расхода в холодную погоду на  23%

ratioWarm: float = 0.3
ratioCold: float = 0.23

tankVol = abs(float(input("\n Enter tank volume, litre -> ")))
print(" Enter city consume:")
consumeVol = abs(float(input("\t\t\tlitre ->\t")))
consumeDist = abs(float(input("\t\t\tper km ->\t")))

if tankVol == 0 or consumeVol == 0 or consumeDist == 0:
    tf: bool = True
else:
    tf: bool = False

#checking the entered data
if tf:
    print("\n Data are UNCORRECTED!", end='')
    print(" \tModify data:")
    if tankVol == 0:
        print("\t\tTank volume = ", tankVol)
    if consumeVol == 0:
        print("\t\tConsume litre = ", consumeVol)
    if consumeDist == 0:
        print("\t\tDistance km = ", consumeDist)
else:
    print("\n Data:")
    print("\tTank volume ->\t{} litre".format(tankVol))
    print("\tCity consume -> {} litre / {} km".format(consumeVol, consumeDist))

#calculation of distance
if tf:
    print("\tDistance is not calculated!")
else:
    distWarm = round(float(tankVol/((consumeVol/consumeDist)*(1-ratioWarm))),3)
    distCold = round(float(tankVol/((consumeVol/consumeDist)*(1-ratioCold))),3)
    print("\n Distance of drive in city:")
    if distWarm < 1 or distCold < 1:
        print("\tWarm wheather -> {} km".format(distWarm))
        print("\tCold wheather -> {} km".format(distCold))
    else:
        print("\tWarm wheather -> {} km".format(int(distWarm)))
        print("\tCold wheather -> {} km".format(int(distCold)))
