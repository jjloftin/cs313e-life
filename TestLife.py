#TestLife.py#

from io       import StringIO
from unittest import main, TestCase

from Life import Life, AbstractCell, FredkinCell, ConwayCell

#====#
#Life#
#====#
class TestLife(TestCase):

  #__init__#
  def test_life__1(self):
    l = Life(0,0)
    assert l.world == []
  def test_life__2(self):
    l = Life(1,1)
    assert l.world == [['']]
  def test_life__3(self):
    l = Life(2,2)
    assert l.world == [['',''],['','']]
  
  #addCell#
  def test_life__4(self):
    l = Life(1,1)
    c = FredkinCell(True)
    l.addCell(0,0,c)
    str(l) == '0'
  def test_life_5(self):
    l = Life(2,2)
    c1 = FredkinCell(True)
    c2 = FredkinCell(True)
    c3 = FredkinCell(True)
    c4 = FredkinCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    
    assert str(l) == '00\n00'
  def test_life_6(self):
    l = Life(2,2)
    c1 = ConwayCell(True)
    c2 = ConwayCell(False)
    c3 = FredkinCell(True)
    c4 = FredkinCell(False)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    
    assert str(l) == '0-\n*.'

  #countLives#
  def test_life_7(self):
    l = Life(2,2)
    c1 = ConwayCell(True)
    c2 = ConwayCell(True)
    c3 = ConwayCell(True)
    c3 = ConwayCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    
    l.countLives()
    l.livesCount == [[3,3],[3,3]]
    
  def test_life_8(self):
    l = Life(2,2)
    c1 = FredkinCell(True)
    c2 = FredkinCell(True)
    c3 = FredkinCell(True)
    c4 = FredkinCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    
    l.countLives()
    l.livesCount = [[2,2],[2,2]]
    
  def test_life_9(self):
    l = Life(1,1)
    c1 = FredkinCell()
    l.addCell(0,0,c1)
    l.countLives()
    l.livesCount = [[0]]

  #popularionEvolve#
  def test_life_10(self):
    l1 = Life(1,1)
    c1 = FredkinCell(True)
    l1.addCell(0,0,c1)
    l1.populationEvolve()
    
    l2 = Life(1,1)
    c2 = ConwayCell(True)
    l2.addCell(0,0,c2)
    l2.populationEvolve()
    
    assert str(l1) == '-' and str(l2) == '.'
    
  def test_life_11(self):
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
    
    assert str(l) == '--\n--'
    
  def test_life_12(self):
    l = Life(2,2)
    c1 = ConwayCell(True)
    c2 = ConwayCell(True)
    c3 = ConwayCell(False)
    c4 = ConwayCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    l.populationEvolve()
    
    assert str(l) == '**\n**'
    
   #giveNeighbhors#
  def test_life_40(self):
    l = Life(2,2)
    c1 = ConwayCell(True)
    c2 = ConwayCell(False)
    c3 = ConwayCell(False)
    c4 = ConwayCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    
    assert l.giveNeighbhors(0,0) == 0
  
  def test_life_41(self):
    l = Life(2,2)
    c1 = ConwayCell(True)
    c2 = ConwayCell(False)
    c3 = ConwayCell(False)
    c4 = ConwayCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    
    l.countLives()
    
    assert l.giveNeighbhors(0,0) == 1
    
  def test_life_42(self):
    l = Life(2,2)
    c1 = ConwayCell(True)
    c2 = ConwayCell(True)
    c3 = FredkinCell()
    c4 = FredkinCell()
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    
    l.countLives()
    
    assert l.giveNeighbhors(1,1) == 1
  #============#
  #AbstractCell
  #============#

  #__init__#
  def test_life_13(self):
    k = AbstractCell()
    assert k.neighbors == []
  def test_life_14(self):
    k = AbstractCell(True)
    assert k.alive
  def test_life_15(self):
    k = AbstractCell()
    assert not k.alive
 
  #evolve#
  def test_life_16(self):
    k = AbstractCell()
    l = Life(1,1)
    l.addCell(0,0,k)
    k.evolve(l)
    assert k.alive
  def test_life_17(self):
    k = AbstractCell()
    l = Life(1,1)
    l.addCell(0,0,k)
    k.evolve(l)
    assert not k.alive
  def test_life_18(self):
    k = AbstractCell(True)
    l = Life(1,1)
    l.addCell(0,0,k)
    k.evolve(l)
    k.evolve(l)
    k.evolve(l)
    assert k.alive
  
  #getNeigbors#
  def test_life_19(self):
    k = AbstractCell()
    assert k.neighbors == []
  
  #str#
  def test_life_20(self):
    k = AbstractCell()
    assert str(k) == '^'
  def test_life_21(self):
    k = AbstractCell()
    l = Life(1,1)
    l.addCell(1,1,k)
    assert str(l) == '^'
    
  #===========#
  #FredkinCell#
  #===========#
  
  #init#
  def test_life_22(self):
    k = FredkinCell(True)
    assert k.age == 0
  def test_life_23(self):
    k = FredkinCell()
    assert k.age == 0
  def test_life_24(self):
    k = FredkinCell()
    assert k.neighbhors == [2,4,5,7]
    
  #evolve#
  def test_life_25(self):
    k = FredkinCell(True)
    l = Life(1,1)
    l.addCell(0,0,k)
    l.countLives()
    k.evolve()
    
    assert k.alive == False
    
  def test_life_26(self):
    k1 = FredkinCell(True)
    k2 = FredkinCell(True)
    l = Life(2,2)
    l.addCell(0,0,k1)
    l.addCell(1,0,k2)
    l.countLives()
    k1.evolve()
    
    assert k1.alive == True
  def test_life_27(self):
    k1 = FredkinCell(True)
    k2 = FredkinCell(True)
    l = Life(2,2)
    l.addCell(0,0,k1)
    l.addCell(1,0,k2)
    l.countLives()
    k1.age = 1
    k1.evolve()
        
    assert isinstance(k1,ConwayCell)    
  
  #getNeighbors#  
  def test_life_28(self):
    k = FredkinCell()
    assert k.getNeighbors() == [2,4,5,7]
    
  #str#  
  def test_life_29(self):
    k = FredkinCell()
    assert str(k) == '-'
  def test_life_30(self):
    k = FredkinCell(True)
    k.age = 11
    assert str(k) == '+'
    
  #==========#
  #ConwayCell#
  #==========#

  #init#
  def test_life_31(self):
    c = ConwayCell()
    assert c.alive == False
  def test_life_32(self):
    c = ConwayCell(True)
    assert c.alive == False
  def test_life_33(self):
    c = ConwayCell()
    assert c.neighbors == [1,2,3,4,5,6,7,8]
    
  #evolve#
  def test_life_34(self):
    l = Life(2,2)
    c1 = ConwayCell()
    c2 = FredkinCell(True)
    c3 = ConwayCell(True)
    c4 = FredkinCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(1,0,c3)
    l.addCell(1,1,c4)
    
    l.countLives()
    c1.evolve()
    
    assert c1.alive == True
    
  def test_life_35(self):
    l = Life(1,3)
    c1 = ConwayCell(True)
    c2 = ConwayCell(True)
    c3 = ConwayCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(0,2,c3)
    
    l.countLives()
    c3.evolve()
    
    assert c3.alive == False
  def test_life_36(self):
    l = Life(1,3)
    c1 = ConwayCell(True)
    c2 = ConwayCell(True)
    c3 = ConwayCell(True)
    l.addCell(0,0,c1)
    l.addCell(0,1,c2)
    l.addCell(0,2,c3)
    
    l.countLives()
    c2.evolve()
    
    assert c2.alive == True  
  
  #getNeighbors#  
  def test_life_37(self):
    c = ConwayCell()
    
  #str#  
  def test_life_38(self):
    c = ConwayCell()
    assert str(c) == '.'
  def test_life_39(self):
    c = ConwayCell(True)
    assert str(c) == '*'

#====#
#main#
#====#
main()
