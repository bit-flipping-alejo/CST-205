def simplePic():
  pic = makePicture(pickAFile())
    
  newPic = simpleCopy(pic)

  show(newPic)
  
def simpleCopy(pic):
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  
  newPic = makeEmptyPicture(picWidth, picHeight)
  
  for x in range (0, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(newPic, x, y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  return newPic
