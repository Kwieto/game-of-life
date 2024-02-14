import random

class Grid:
  length = 5
  width = 5
  grid = []

  def __init__(self, length, width):
    self.length = length
    self.width = width
    self.grid = []

    for i in range(0, length):
      self.grid.append([])
      for j in range(0, width):
        if random.random() <= 0.5:
          self.grid[i].append('.')
        else:
          self.grid[i].append('*')


  def draw(self):
    for i in range(len(self.grid)):
      print(''.join(str(x) for x in self.grid[i]))

  def generateNewGeneration(self):
    newGeneration = []
    for i in range(0, self.length):
      newGeneration.append([])
      for j in range(0, self.width):
        currentValue = self.decideCellValue(self.getCell(i, j))
        neighbourValue = self.getNeighbourValue(i, j)

        if currentValue == 0:
          if neighbourValue == 3:
            newGeneration[i].append('*')
          else:
            newGeneration[i].append('.')
        elif currentValue == 1:
          if neighbourValue < 2:
            newGeneration[i].append('.')
          elif neighbourValue == 2 or neighbourValue == 3:
            newGeneration[i].append('*')
          elif neighbourValue >= 4:
            newGeneration[i].append('.')

    self.grid = newGeneration

  def getNeighbourValue(self, lengthPosition, widthPosition):
    neighbourValue = 0

    neighbourValue += self.decideCellValue(self.getCell(lengthPosition, widthPosition - 1))
    neighbourValue += self.decideCellValue(self.getCell(lengthPosition, widthPosition + 1))
    neighbourValue += self.decideCellValue(self.getCell(lengthPosition - 1, widthPosition))
    neighbourValue += self.decideCellValue(self.getCell(lengthPosition + 1, widthPosition))

    return neighbourValue


  def getCell(self, lengthPosition, widthPosition):
    try:
      if lengthPosition < 0 or widthPosition < 0:
        return None
      else:
        return self.grid[lengthPosition][widthPosition]
    except:
      return None
    
  def decideCellValue(self, cell):
    if cell == None:
      return 0
    elif cell == '.':
      return 0
    elif cell == '*':
      return 1
    else:
      raise Exception('Unknown value: ' + cell)