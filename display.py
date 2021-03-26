
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def display(self):
    print("name-{}, age-{}".format(self.name,self.age))
    return

if __name__ == '__main__':
    p=Person("Aparna",30)

    p.display()
  
