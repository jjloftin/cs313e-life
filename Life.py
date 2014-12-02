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
    
    self.world = i*[j*['']]
    self.livesCount = i*[j*[0]]
    self.neighbhors = 0
    
  def addCell(self,cell,i,j):
    assert type(cell) is AbstractCell
    self.world[i][j] = cell  
      
  def countLives(self):
    '''
    Go through the board. Count the number of living neighbors.
    '''
    return
    
  def giveNeighbhors(self,i,j):
    '''
    Give the number of neighbhors of a living cell.
    '''
  
  def cellExecute(self, i,j):
    '''
    Executes a cell. Will figure out how many live neighbhors there are for this cell to tell the cell if necessary.
    '''
    
  def proceedGeneration(self):
    '''
    Goes through the world. Tells each AbstractCell to execute a generation.
    '''
    return

  def __str__(self):
    '''
    Returns a pictoral representation of the Life board.
    '''
    return ''
  
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
    
  def getNeighbhors(self):
    '''
    Return the set of neighbhors
    '''
    return self.neighbors
    
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
    pass

  def str(self):
    return 'Dogs'
    
class FredkinCell(AbstractCell):
  def __init__self(self,alive = False):
    AbstractCell.__init__(self, alive)
    self.age = 0   
    self.neighbhors = [2,4,5,7]    
  
  def evolve(self):
    return
  
  def __str__(self):
    return 'Cats'