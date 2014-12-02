#RunLife.py#

import sys

from Life import Life,FredkinCell,ConwayCell
'''
Conway Cells 21 by 13 - 12 generations w/ all grids
'''
print('***Life<ConwayCell> 21 x 13***')
print()
iMax = int(sys.stdin.readline())
jMax = int(sys.stdin.readline())

l = Life(iMax,jMax)
for i in range(iMax):
  line = sys.stdin.readline().strip()
  for j in range(jMax):
    if line[j] == '.':
      l.addCell(i,j,ConwayCell())
    else:
      l.addCell(i,j,ConwayCell(True))


for k in range(13):
  print('Generation =',k,end=', ')
  print('Population = ' + str(l.getPopulation()) + '.')
  
  print(l)
  print()
  l.populationEvolve()

sys.stdin.readline()

'''
Conway Cells 20 by 29 - 28 generations w/ every 4th grid
'''
print("*** Life<ConwayCell> 20x29 ***")
iMax = int(sys.stdin.readline())
jMax = int(sys.stdin.readline())

l = Life(iMax,jMax)
for i in range(iMax):
  line = sys.stdin.readline().strip()
  for j in range(jMax):
    if line[j] == '.':
      l.addCell(i,j,ConwayCell())
    else:
      l.addCell(i,j,ConwayCell(True))

for k in range(29):
  if(k % 4 == 0):
    print('Generation =',k,end=', ')
    print('Population = ' + str(l.getPopulation()) + '.')
  
    print(l)
    print()
  l.populationEvolve()
  
sys.stdin.readline()

'''
Conway Cells 109 by 69. 283 evolutions. Print the first 10. 0 - 9
Print the 283rd grid.
Print the 323rd grid
Print the 2500th grid.
'''
print('*** Life<ConwayCell> 109x69 ***')
print()

iMax = int(sys.stdin.readline())
jMax = int(sys.stdin.readline())

l = Life(iMax,jMax)
for i in range(iMax):
  line = sys.stdin.readline().strip()
  for j in range(jMax):
    if line[j] == '.':
      l.addCell(i,j,ConwayCell())
    else:
      l.addCell(i,j,ConwayCell(True))

for k in range(2501):
  if(k < 10 or k ==283 or k == 323 or k == 2500):
    print('Generation =',k,end=', ')
    print('Population = ' + str(l.getPopulation()) + '.')
  
    print(l)
    print()
  l.populationEvolve()

sys.stdin.readline()

'''
FredkinCells  20 by 20. Do 5 simulations and print every grid.
''' 
print('*** Life<FredkinCell> 20x20 ***')
print()
     
iMax = int(sys.stdin.readline())
jMax = int(sys.stdin.readline())

l = Life(iMax,jMax)
for i in range(iMax):
  line = sys.stdin.readline().strip()
  for j in range(jMax):
    if line[j] == '-':
      l.addCell(i,j,FredkinCell())
    else:
      l.addCell(i,j,FredkinCell(True))

for k in range(6):
  print('Generation =',k,end=', ')
  print('Population = ' + str(l.getPopulation()) + '.')
  
  print(l)
  if k < 5:
    print()
  l.populationEvolve()