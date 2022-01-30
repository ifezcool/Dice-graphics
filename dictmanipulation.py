import random
thisdict = {
  "roll1": """               _____________
              |            |
              |     _      |
              |    |_|     |
              |            |
              |____________|
  """
  ,
  "roll2": """               _____________
              |  _         |
              | |_|        |
              |         _  |
              |        |_| |
              |____________|
  """
  ,
  "roll3": """               _____________
              |  _         |
              | |_|  _     |
              |     |_| _  |
              |        |_| |
              |____________|
  """
  ,
  "roll4": """               _____________
              |  _       _ |
              | |_|     |_||
              |  _       _ |
              | |_|     |_||
              |____________|
  """
  ,
  "roll5": """               _____________
              |  _      _  |
              | |_| _  |_| |
              |  _ |_|  _  |
              | |_|    |_| |
              |____________|
  """
    ,
    "roll6": """               _____________
              |  _      _  |
              | |_|    |_| |
              | |_|    |_| |
              | |_|    |_| |
              |____________|
  """
  
  
}
#code will draw the side of the dice the dice landed on
diceroll = random.randint(0,6)
if diceroll == 1:
    print(thisdict["roll1"])
elif diceroll == 2:
    print(thisdict["roll2"])
elif diceroll == 3:
    print(thisdict["roll3"])
elif diceroll == 4:
    print(thisdict["roll4"])
elif diceroll == 5:
    print(thisdict["roll5"])
elif diceroll == 6:
    print(thisdict["roll6"])