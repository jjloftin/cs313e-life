from Life import Life, AbstractCell, ConwayCell, FredkinCell

l = Life(2,2)
c1 = FredkinCell(True)
c2 = FredkinCell(False)
c3 = FredkinCell(False)
c4 = FredkinCell(False)
l.addCell(0,0,c1)
l.addCell(0,1,c2)
l.addCell(1,0,c3)
l.addCell(1,1,c4)
l.populationEvolve()

print(str(l))