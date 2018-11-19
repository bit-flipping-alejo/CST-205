# Ivan Alejandre

def get_sound():
  return makeSound(pickAFile())
  
def decreaseVolume():
  sound = get_sound()
  sample = getSamples(sound)
  
  for s in sample:
    currentSample = getSampleValue(s)
    setSampleValue(s, int(currentSample/2))
  explore(sound)
  #writeSoundTo(sound, r"C://temp/halved.wav")
  
def changeVolume():
  sound = get_sound()
  sample = getSamples(sound)
  
  incDec = raw_input("Enter increase or decrease to change the volume. ")
  modifier = input("Now enter the value to change the volume by (0-100): ")
  
  
  if incDec == "increase":
    finalMod = 1 + modifier/100.0
  elif incDec == "decrease":
    finalMod = 1 - modifier/100.0
  else:
    print("Invalid input, terminating program.")
    return
  
  print finalMod
  
  for s in sample:
    currentSample = getSampleValue(s)
    setSampleValue(s, int(currentSample*finalMod))
    
  explore(sound)
  
def maxSample(sound):
  sample = getSamples(sound)
  list = []
  
  for s in sample:
    list.append(abs(getSampleValue(s)))
    
  maxValue = max(list)
  
  return maxValue

def maxVolume():
  sound = get_sound()
  
  largestSample = maxSample(sound)
  sample = getSamples(sound)
  factor = float(32767/largestSample)
  
  for s in sample:
    currentValue = getSampleValue(s)
    setSampleValue(s, currentValue*factor)
    
  explore(sound)
  
def goToEleven(sound):
  sample = getSamples(sound)
  
  for s in sample:
    if getSampleValue(s) > 0:
      setSampleValue(s, 32767)
    elif getSampleValue(s) < 0:
      setSampleValue(s, -32767)
    else:
      setSampleValue(s, 0)
  
  return sound
