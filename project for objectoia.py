class fruit:
  # class variable
  taste = 'sweet'

  # instance variable
  def __init__(self, name, color):
    self.name = name
    self.color = color
# object creation
orange = fruit('orange','Orange')
Banana = fruit('Banana','Yellow')

print(orange.taste)
print()