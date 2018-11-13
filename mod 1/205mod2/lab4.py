def get_pic():
  return makePicture(pickAFile())
  
def mirrorLeft():
  pic = get_pic()
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (0, picWidth/2):
    for y in range (0, picHeight):
      pixelCurrent = getPixel(pic, x, y)
      newPix = getPixel(pic, (picWidth - x - 1), y)
      pixelColor = getColor(pixelCurrent)
      setColor(newPix, pixelColor)
  
  repaint(pic)

def mirrorRight():
  pic = get_pic()
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (picWidth/2, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, (picWidth - x), y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  repaint(pic)
  
def mirrorTop():
  pic = get_pic()
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (0, picWidth):
    for y in range (0, picHeight/2):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, x, picHeight - y - 1)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
      
  repaint(pic)
  
def mirrorBottom():
  pic = get_pic()
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (0, picWidth):
    for y in range (picHeight/2, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, x, picHeight - y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
      
  repaint(pic)
  
def doubleMirror():
  pic = get_pic()
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  # mirror bottom half first
  for x in range (0, picWidth):
    for y in range (picHeight/2, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, x, picHeight - y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  # then mirror right half of new image
  for x in range (picWidth/2, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, (picWidth - x), y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  repaint(pic)
