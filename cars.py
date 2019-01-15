# Create a single class that implements all functionality.

class GetData:
  def __init__(self):
    self.info = self.get_info()


# Create a method for reading the car makes file.
  def get_makes(self):
    with open("data/car-makes.txt", "r") as car_makes:
      self.makes = car_makes.readlines()


# Create a method for reading the car models file.
  def get_models(self):
    self.models = open("data/car-models.txt", "r").readlines()

# Create a method that invokes the previous two methods and generates a dictionary.
  def get_info(self):
    makes = self.get_makes()
    models = self.get_models()


# The dictionary keys will be the make names.
# The value for each key will be a list of model names.
  def make_dict(self):
    self.makes_models = {}
    for mks in self.makes:
      mks = mks.strip()
      mods = []
      for mds in self.models:
        if mks[0] == mds[0]:
          mds = mds.strip().split("=")
          mds = mds[1].strip()
          mods.append(mds)
          self.makes_models.update({mks: mods})

  def makeNmodel(self):
    info = self.makes_models.copy()
    myMks = []
    myMods = []
    for x in info.keys():
      myMks.append(x)
    for y in info.values():
      myMods.append(y)
    i = 0
    while i < len(myMks):
      print("\n")
      print(f"----{myMks[i]}----")
      for x in myMods[i]:
        print(x)
      # for item in key.values():
      #   print(item)
      i = i + 1


auto = GetData()
auto.make_dict()

print()
auto.makeNmodel()
