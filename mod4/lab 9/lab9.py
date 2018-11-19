# Ivan Alejandre
# Lab 9
# 11/17/18

def get_sound():
  return makeSound(pickAFile())
  
def clip(source, start, end):
  sampleSize = end - start
  
  clippedSound = makeEmptySound(sampleSize)
  
  for index in range(0, sampleSize):
    currentSample = getSampleValueAt(source, index + start)
    setSampleValueAt(clippedSound, index, currentSample)
    
  return clippedSound
  
def copy(source, target, start)

  sourceSamples = getSamples(source)
  
  targetSamples = getSamples(target)
  
  for s in range(0, getNumSamples(source)):
    currentSample = getSampleValueAt(source, s)
    setSampleValueAt(target, (s + start), currentSample)
  
  return target
  
def soundCollage():
  target = makeEmptySoundBySeconds(10)
  x = 0
  start = 0
  while x < 5:
    
      
    sound = get_sound()
    half = getNumSamples(sound)/2
    source = clip(sound, 0, half)
    
    copy(source, target, start)
    start = half
    
