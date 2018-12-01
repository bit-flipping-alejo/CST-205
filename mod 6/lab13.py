class MadLib(object):

  def __init__(self):
    self._text = ""
    self._descriptors = dict()
    
  def getInputs(self):
    self._inputs = dict()
    
    for k, v in self._descriptors.items():
      self._inputs[k] = str(input("I need " + v + ": "))
      
  def printResults(self):
    try:
      print(self._text.format(**self._inputs))
    #except Exception as e:
      raise AssertionError("You should get some words first!")
      
class NewsMadLib(MadLib):
  def __init__(self):
    self._text = " ".join(["The field of {noun1} is fast-growing. {noun2} can now {verb1} ",
                           "complicated movements with {adjective1} -- back-{verb2}ing, practicing",
                           "parkour moves, even \"carving\" classical {noun3}. Then there's",
                           "{noun4}, a robot whose widespread appeal lies not in {adjective2}, dramatic",
                           "actions (her {noun5} is often fixed to a rolling base), but rather an",
                           "unsettling human-like appearance, compounded with the complex ability",
                           "to express emotions. AI-produced artwork sells for $433K, smashing",
                           "expectations \"We're not fully there yet, but Sophia can represent",
                           "a number of emotional states, and she can also see emotional",
                           "expressions on a human face as well,\" explains David Hanson,",
                           "the founder of Hanson Robotics. The firm has developed a number",
                           "of Sophias at their small research and design laboratory in Hong",
                           "Kong, where parts and pieces of Sophia 20, 21 and 22 remain strewn",
                           "across the facility."])
    self._descriptors = {"noun1": "a field of science",
                         "noun2": "an object",
                         "noun3": "a object you can create",
                         "noun4": "a name",
                         "noun5": "a body part",
                         "verb1": "a verb",
                         "verb2": "a verb",
                         "adjective1": "an adjective",
                         "adjective2": "an adjective",
                         
