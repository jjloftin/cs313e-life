#Life.py#

class Life:
  '''
  #Contains cells and tells them to evolve. Generally Conway and Fredkin Cells but can acommodate non-standard  cell structures.
  Data: world - a grid that contains live and dead cells. 
  '''
  def __init__(self,i,j):
    '''
    Initialize the environment for cells to evolve in. 
    Initialize a grid equal to the size of the environment for cells to count lives.
    '''
    
    self.world = (i+2)*[(j+2)*['']]
    self.livesCount = (i+2)*[(j+2)*[0]]
    self.neighbhors = 0
    
  def addCell(self,cell,i,j):
    assert isinstance(cell,AbstractCell)
    self.world[i+1][j+1] = cell  
      
  def countLives(self):
    '''
    Go through the board. Count the number of living neighbors.
    '''
    for i in range(1,len(self.world)-1):
      for j in range(1,len(self.world[i])-1):
        if isinstance(self.world[i][j],AbstractCell):
          
          neighbors = self.world[i][j].getNeighbors()
          self.neighbors = 0
          
          if 1 in neighbors:
            if isinstance(self.world[i-1][j-1], AbstractCell):
              if self.world[i-1][j-1].getAlive():
                self.neighbors += 1
          if 2 in neighbors:
            if isinstance(self.world[i-1][j], AbstractCell):
              if self.world[i-1][j].getAlive():
                self.neighbors += 1
          if 3 in neighbors:
            if isinstance(self.world[i-1][j+1], AbstractCell):
              if self.world[i-1][j+1].getAlive():
                self.neighbors += 1
          if 4 in neighbors:
            if isinstance(self.world[i][j-1], AbstractCell):
              if self.world[i][j-1].getAlive():
                self.neighbors += 1  
          if 5 in neighbors:
            if isinstance(self.world[i][j+1], AbstractCell):
              if self.world[i-1][j+1].getAlive():
                self.neighbors += 1                
          if 6 in neighbors:
            if isinstance(self.world[i+1][j-1], AbstractCell):
              if self.world[i+1][j-1].getAlive():
                self.neighbors += 1
          if 7 in neighbors:
            if isinstance(self.world[i+1][j], AbstractCell):
              if self.world[i+1][j].getAlive():
                self.neighbors += 1
          if 8 in neighbors:
            if isinstance(self.world[i+1][j+1], AbstractCell):
              if self.world[i+1][j+1].getAlive():
                self.neighbors += 1
          self.livesCount[i][j] = self.neighbors
            
    
  def liveNeighbhors(self):
    '''
    Give the number of neighbhors of a living cell.
    '''
    return self.neigbors
  
  def cellExecute(self, i,j):
    '''
    Executes a cell. Will figure out how many live neighbhors there are for this cell to tell the cell if necessary.
    '''
    c = self.world[i][j]
    self.neighbors = self.livesCount[i][j]
    if isinstance(c,AbstractCell):
      c.evolve()
    
  def populationEvolve(self):
    '''
    Goes through the world. Tells each AbstractCell to execute a generation.
    '''
    l.countLives()
    for i in range(1,len(self.world)-1):
      for j in range(1,len(self.world[i]) - 1):
        self.cellExecute(i,j)

  def __str__(self):
    '''
    Returns a pictoral representation of the Life board.
    '''
    s = ''
    
    for i in range(1,len(self.world)-1):
      for j in range(1,len(self.world[0]) - 1):
        s += str(self.world[i][j])
      s += '\n'
    return s
  
class AbstractCell:

  '''
  123
  4^5
  678
  
  Each integer represents a possible neighbor. Cell Types have their own set of "neighbors" they will be fed this to Life.
  Life will return number of live neighbors.
  '''


  def __init__(self, alive = False):
    '''
    Data Members:
    alive - boolean
    neigbhors - list of ints (which represent positions relative to the cell)
    '''
    assert type(alive) is bool
    self.alive = alive
    self.neighbors = []
    
  def getNeighbhors():
    '''
    Return the set of neighbhors. Only called when a cell is executing.
    '''
    return self.neighbors
  
  def getAlive(selg):
    '''
    Return if cell is alive or not
    '''
    return self.alive
    
  def evolve(self, life):
    '''
    Evolve the cell according to its rules. Does nothing otherwise. 
    '''
    return 
  
  def __str__(self):
    return '^'

class ConwayCell(AbstractCell):
  def __init__(self,alive = False):
    AbstractCell.__init__(self, alive)
    self.neighbhors = [1,2,3,4,5,6,7,8]
  
  def evolve(self, life):
    u = l.giveNeighbors()
    
    #if alive with less than 2 or more than 3 neigbhors make dead
    if self.alive:
      if u < 2 or u > 3:
        self.alive = False
    #if dead with exactly three neighbors make live
    else:
      if u == 3:
        self.alive = True

  def str(self):
    if self.alive:
      return '*'
    else:
      return '.'
    
class FredkinCell(AbstractCell):
  def __init__self(self,alive = False):
    AbstractCell.__init__(self, alive)
    self.age = 0   
    self.neighbhors = [2,4,5,7]    
  
  def evolve(self):
    u = l.liveNeighbors()
    
    #if live with 0, 2, or 4 live neighbhors stay alive, if 1 or 3 live neighbhors it dies
    if self.alive and u in [0,2,4]:
      self.age += 1
    elif self.alive:
      self.alive = False
    #if dead with 1 or 3 live neighbors stay alive
    elif self.alive == False and u in [1,3]:
      self.alive = True
  
  def __str__(self):
    if self.alive:
      return str(self.age)
    else:
      return '-'