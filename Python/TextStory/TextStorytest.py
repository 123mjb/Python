import TextstoryBasis as tsb
names = ["Health", "Damage", "Defence", "Magic"]
Values = [100, 20, 50, 0]
upgrade1vals = [10, 30, 5, 0] # beserker
upgrade2vals = [10, -5, 5, 20] # wizard
upgrade3vals = [40, 5, 5, 5] # healer
upgrade4vals = [15, 15, 30, 0] # tank
while True:
    tsb.printvalues(names, Values)
    Values = tsb.chooseupgrade(Values, upgrade1vals, upgrade2vals, upgrade3vals, upgrade4vals)

