def simplePic():
  pic = makePicture(pickAFile())
    
  newPic = rotatePic(pic)

  show(newPic)
  
# rotates image 90 degress to the left
def rotatePic(pic):
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  
  rotatedPic = makeEmptyPicture(picHeight, picWidth)
  
  for x in range (0, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, (picWidth - x - 1), y)
      newPixel = getPixel(rotatedPic, y, x)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  return rotatedPic
