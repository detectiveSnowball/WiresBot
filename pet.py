from datetime import date, datetime, timedelta



today = date.today()
now = datetime.now()
print("todays date is: ", today)
print("the time is: ", now)


class pet:


  # Default 
  def __init__(self, petName):
    self.name =  "PET"
    # Stats for the Pet, these will be used to trigger events
    self.hunger = 0 # Hunger level, if low, that pet is hungry, 100 is highest
    self.energy = 0 # Energy Level, if low, pet is sleepy
    self.emotion = 0 #Emotional State
    self.health = 50 # 50 is good health

  """
  Checks the hunger levels of the pet and prints its status
  """
  def isHungry(self, checkFlag):

    if (checkFlag == 0):
      if (self.hunger < 20):
        print(self.name + " is starving!!!!")
    elif (checkFlag == 1):
      if (self.hunger <= 20):
        print(self.name + " is starving!!!")
      elif (self.hunger > 20 and self.hunger <= 50):
        print(self.name + " is kinda hungry")
      elif (self.hunger >= 51 and self.hunger <= 80):
        print(self.name + " is kinda full")
      elif (self.hunger >= 81):
        print(self.name + " is extremely full!!!")


  

  


    








  
